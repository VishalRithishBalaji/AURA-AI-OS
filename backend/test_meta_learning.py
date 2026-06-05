from multi_agent.society_learning_engine import (
    learn_from_execution
)

from self_improvement.agent_optimizer import (
    optimize_agents
)

from self_improvement.strategy_memory import (
    get_all_strategies
)


learn_from_execution(

    "docker deployment",

    "error: deployment failed",

    False
)

print(
    optimize_agents()
)

print(
    get_all_strategies()
)