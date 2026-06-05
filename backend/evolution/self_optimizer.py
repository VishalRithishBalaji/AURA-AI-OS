from evolution.failure_detector import (
    detect_failures
)

from evolution.prompt_evolution import (
    evolve_prompt
)

from evolution.strategy_evolution import (
    improve_strategy
)

from multi_agent.agent_bus import (
    publish_event
)


def self_optimize():

    publish_event(

        "SelfOptimizer",

        "Starting recursive self-improvement"
    )

    failures = detect_failures()

    improvements = []

    # FAILURE ANALYSIS
    if failures:

        improvements.append(
            f"Detected {len(failures)} recurring failures"
        )

        evolve_prompt(
            "Be more resilient to API failures and rate limits."
        )

        improvements.append(
            "Prompt resilience upgraded"
        )

    # STRATEGY EVOLUTION
    strategy = improve_strategy()

    improvements.append(
        f"Strategy evolved: {strategy}"
    )

    publish_event(

        "SelfOptimizer",

        "Self-improvement completed"
    )

    return f"""
# 🧠 Recursive Self-Improvement

## Failures Detected
{len(failures)}

---

## Improvements

{chr(10).join([
f"• {item}"

for item in improvements
])}

---

## Updated Strategy
{strategy}
"""