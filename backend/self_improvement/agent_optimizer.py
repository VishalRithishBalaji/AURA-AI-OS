from self_improvement.failure_analyzer import (
    analyze_failures
)

from self_improvement.improvement_generator import (
    generate_improvement
)

from self_improvement.strategy_memory import (
    save_strategy
)


def optimize_agents():

    failures = (
        analyze_failures()
    )

    improvements = []

    for failure in failures:

        strategy = (

            generate_improvement(
                failure
            )
        )

        save_strategy(

            failure[
                "category"
            ],

            strategy
        )

        improvements.append({

            "task":
            failure[
                "task"
            ],

            "strategy":
            strategy
        })

    return improvements