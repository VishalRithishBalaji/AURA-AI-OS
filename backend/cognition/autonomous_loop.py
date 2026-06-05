import asyncio

from cognition.long_term_goals import (
    load_goals
)

from cognition.objective_tracker import (
    set_objective,
    update_progress
)

from multi_agent.agent_bus import (
    publish_event
)


AUTONOMOUS_RUNNING = False


async def autonomous_loop():

    global AUTONOMOUS_RUNNING

    AUTONOMOUS_RUNNING = True

    publish_event(

        "AutonomousLoop",

        "Started"
    )

    while AUTONOMOUS_RUNNING:

        try:

            goals = load_goals()

            active_goals = [

                g

                for g in goals

                if g["status"] == "active"
            ]

            if active_goals:

                goal = active_goals[0]

                set_objective(
                    goal["goal"]
                )

                publish_event(

                    "AutonomousLoop",

                    f"Working on goal: {goal['goal']}"
                )

                update_progress(
                    50
                )

            await asyncio.sleep(
                300
            )

        except Exception as e:

            publish_event(

                "AutonomousLoop",

                f"Error: {str(e)}"
            )

            await asyncio.sleep(
                30
            )


def stop_autonomous_loop():

    global AUTONOMOUS_RUNNING

    AUTONOMOUS_RUNNING = False