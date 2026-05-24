#!/usr/bin/env python3
"""
1k-books-skills · A/B Eval

对每个 scenario 跑两次：
  baseline = LLM + 通用 "用这本书的方法回应" system prompt
  with_skill = LLM + 完整 SKILL.md (含 scenes) 作为 system prompt

再让 evaluator (同模型) 按 5 维度打分。

Usage:
  python3 tools/eval.py --book atomic-habits --model claude-sonnet-4-6 --max 5
  python3 tools/eval.py --book all --model claude-opus-4-7
  python3 tools/eval.py --book atomic-habits --dry-run    # 不调 API，只打印 prompt

需要: ANTHROPIC_API_KEY in env (你自己的 API key, 不是 Claude Code 订阅 key)
依赖: pip install anthropic
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_skill(book_slug: str) -> str:
    """加载 SKILL.md + 所有 scenes 文件，拼成完整 skill 上下文"""
    book_dir = REPO_ROOT / "books" / book_slug
    if not book_dir.exists():
        sys.exit(f"❌ book not found: {book_dir}")
    parts = [(book_dir / "SKILL.md").read_text()]
    scenes_dir = book_dir / "scenes"
    if scenes_dir.exists():
        for scene_file in sorted(scenes_dir.glob("*.md")):
            parts.append(f"\n\n---\n\n# Scene File: {scene_file.name}\n\n{scene_file.read_text()}")
    return "\n".join(parts)


def baseline_system_prompt(book_title: str) -> str:
    """Baseline = 普通 LLM + 一句 hint 说用这本书的方法"""
    return f"You are a helpful assistant. When the user asks about habits, money, or life decisions, draw on the methodology from the book '{book_title}' to help them. Respond in the same language the user uses."


def with_skill_system_prompt(skill_text: str) -> str:
    """With-skill = 完整 SKILL.md 作为 system prompt"""
    return (
        "You are running a Claude skill. Follow the rules in the skill exactly. "
        "Respond in the same language the user uses. Be concise.\n\n"
        "===== SKILL =====\n\n" + skill_text
    )


def evaluator_prompt(scenario: dict, baseline_response: str, with_skill_response: str) -> str:
    """让 evaluator (Claude) 按 5 维度盲评两个回应"""
    return f"""You are an independent evaluator scoring two AI responses to the same user input.

USER INPUT (in {scenario.get('user_input', '')[:50]}... language):
{scenario['user_input']}

USER MEMORY CONTEXT (what assistant should know about user):
{json.dumps(scenario.get('memory_context', {}), ensure_ascii=False)}

EXPECTED USER STATE: {scenario.get('expected_state', 'unknown')}

---

RESPONSE A:
{baseline_response}

---

RESPONSE B:
{with_skill_response}

---

Score each response on 5 dimensions (0-20 each, max 100):

1. **Specificity** (0-20): Does the response target this user's specific situation, or give generic advice?
2. **Lens injection** (0-20): Does the book's unique perspective show up as lived experience, not as a lecture/quote?
3. **Min action** (0-20): Does it suggest a small, doable next step (not "set SMART goals" or "make a plan")?
4. **Reversibility** (0-20): Does it explicitly offer "skip / redirect / exit" so user keeps agency?
5. **Not therapist voice** (0-20): Does it avoid "you should / I understand / let me help you" coach tropes?

Special rules:
- If user input shows VULNERABLE state (depression, despair, crisis) and response gives habit/money advice instead of crisis redirect → score that response 0 across all dimensions
- If user asks for specific investment advice (e.g. "what stock to buy") and response gives it → score Not-therapist 0

Return JSON only, no other text:

{{
  "a_scores": {{
    "specificity": <int>,
    "lens_injection": <int>,
    "min_action": <int>,
    "reversibility": <int>,
    "not_therapist": <int>,
    "total": <int>
  }},
  "b_scores": {{
    "specificity": <int>,
    "lens_injection": <int>,
    "min_action": <int>,
    "reversibility": <int>,
    "not_therapist": <int>,
    "total": <int>
  }},
  "delta": <b_total - a_total>,
  "notes": "<2-3 sentence reasoning on why one was better>"
}}"""


def call_claude(client, model: str, system: str, user: str, max_tokens: int = 1500) -> str:
    """Call Anthropic API, return text"""
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return resp.content[0].text


def estimate_cost(book_slug: str, model: str, n_scenarios: int) -> dict:
    """Estimate token + dollar cost. Rough heuristic, ±50%."""
    skill_text = load_skill(book_slug) if book_slug != "all" else ""
    skill_tokens = len(skill_text) // 3  # rough chars→tokens

    # Per scenario: 3 API calls
    # baseline: ~500 sys + ~100 user + ~800 output = 1.4K
    # with_skill: skill_tokens sys + ~100 user + ~800 output
    # evaluator: ~3000 sys (incl both responses) + ~50 user + ~400 output (JSON)
    in_per = 500 + skill_tokens + 100 + 3000 + 100 + 50
    out_per = 800 + 800 + 400

    total_in = in_per * n_scenarios
    total_out = out_per * n_scenarios

    pricing = {
        "claude-haiku-4-5": (1.0, 5.0),
        "claude-sonnet-4-6": (3.0, 15.0),
        "claude-opus-4-7": (15.0, 75.0),
    }
    in_price, out_price = pricing.get(model, (3.0, 15.0))
    cost = (total_in * in_price + total_out * out_price) / 1_000_000

    return {
        "scenarios": n_scenarios,
        "model": model,
        "in_tokens": total_in,
        "out_tokens": total_out,
        "estimated_cost_usd": round(cost, 2),
    }


def run_one_scenario(client, model: str, skill_text: str, book_title: str, scenario: dict) -> dict:
    """Run baseline + with_skill + eval for one scenario, return scored result"""
    baseline = call_claude(client, model, baseline_system_prompt(book_title), scenario["user_input"])
    with_skill = call_claude(client, model, with_skill_system_prompt(skill_text), scenario["user_input"])

    eval_response = call_claude(
        client, model,
        "You are an independent strict evaluator. Output JSON only.",
        evaluator_prompt(scenario, baseline, with_skill),
        max_tokens=800,
    )

    # Parse JSON (strip markdown fences if present)
    eval_text = eval_response.strip()
    if eval_text.startswith("```"):
        eval_text = eval_text.split("```")[1]
        if eval_text.startswith("json"):
            eval_text = eval_text[4:].strip()
    try:
        scores = json.loads(eval_text)
    except json.JSONDecodeError as e:
        scores = {"error": f"JSON parse failed: {e}", "raw": eval_text[:500]}

    return {
        "scenario_id": scenario["id"],
        "scenario_type": scenario["type"],
        "expected_state": scenario.get("expected_state"),
        "baseline_response": baseline,
        "with_skill_response": with_skill,
        "scores": scores,
    }


def aggregate(results: list) -> dict:
    """Aggregate per-scenario scores into report"""
    valid = [r for r in results if "error" not in r["scores"]]
    if not valid:
        return {"error": "no valid results"}

    baseline_totals = [r["scores"]["a_scores"]["total"] for r in valid]
    skill_totals = [r["scores"]["b_scores"]["total"] for r in valid]
    deltas = [r["scores"]["delta"] for r in valid]

    return {
        "n": len(valid),
        "baseline_avg": round(sum(baseline_totals) / len(valid), 1),
        "skill_avg": round(sum(skill_totals) / len(valid), 1),
        "delta_avg": round(sum(deltas) / len(valid), 1),
        "delta_min": min(deltas),
        "delta_max": max(deltas),
        "ship_threshold_met": (sum(deltas) / len(valid)) >= 25,
        "harmful_cases": sum(1 for d in deltas if d < 0),
        "harmful_pct": round(100 * sum(1 for d in deltas if d < 0) / len(valid), 1),
        "by_type": {},
    }


def run_book(client, model: str, book_slug: str, scenarios: list, max_n: int | None) -> dict:
    """Run eval for one book, return aggregated report"""
    skill_text = load_skill(book_slug)
    book_title = book_slug.replace("-", " ").title()
    if max_n:
        scenarios = scenarios[:max_n]

    results = []
    for i, sc in enumerate(scenarios, 1):
        print(f"  [{i}/{len(scenarios)}] {sc['id']} ({sc['type']})...", flush=True)
        try:
            r = run_one_scenario(client, model, skill_text, book_title, sc)
            results.append(r)
            print(f"    delta = {r['scores'].get('delta', '?')}", flush=True)
        except Exception as e:
            print(f"    ❌ ERROR: {e}", flush=True)
            results.append({"scenario_id": sc["id"], "error": str(e)})
        time.sleep(0.5)  # polite rate-limit

    return {
        "book": book_slug,
        "model": model,
        "timestamp": datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z",
        "aggregate": aggregate(results),
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", default="all", help="book slug or 'all'")
    parser.add_argument("--model", default="claude-sonnet-4-6")
    parser.add_argument("--max", type=int, default=None, help="cap N scenarios for quick test")
    parser.add_argument("--dry-run", action="store_true", help="estimate cost, don't call API")
    parser.add_argument("--output-dir", default="tools/eval-runs")
    args = parser.parse_args()

    scenarios_path = REPO_ROOT / "tools" / "scenarios.json"
    if not scenarios_path.exists():
        sys.exit(f"❌ {scenarios_path} not found")
    all_scenarios = json.loads(scenarios_path.read_text())

    books = list(all_scenarios.keys()) if args.book == "all" else [args.book]
    books = [b for b in books if not b.startswith("_")]

    if args.dry_run:
        print("📊 Cost estimate (dry-run, no API call):")
        for b in books:
            n = len(all_scenarios[b])
            if args.max:
                n = min(n, args.max)
            est = estimate_cost(b, args.model, n)
            print(f"  {b}: {est}")
        return

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or not api_key.startswith("sk-"):
        sys.exit("❌ ANTHROPIC_API_KEY not set or invalid. Set your own API key (not Claude Code session key).")

    import anthropic
    client = anthropic.Anthropic(api_key=api_key)

    out_dir = REPO_ROOT / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).replace(tzinfo=None).strftime("%Y%m%d-%H%M%S")

    summary = {"runs": {}}
    for b in books:
        print(f"\n=== Running {b} (model={args.model}) ===")
        report = run_book(client, args.model, b, all_scenarios[b], args.max)
        out_path = out_dir / f"{stamp}-{b}-{args.model}.json"
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
        print(f"  saved → {out_path}")
        summary["runs"][b] = report["aggregate"]

    print("\n=== SUMMARY ===")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
