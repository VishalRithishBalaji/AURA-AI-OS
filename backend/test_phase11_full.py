import asyncio

from multi_agent.autonomous_society_v2 import (
    autonomous_society_v2
)

from departments.autonomous_ceo_agent import (
    autonomous_ceo_agent
)


async def main():

    print(

        await autonomous_society_v2(

            "production deployment"
        )
    )

    print(
        "\n\n====================\n"
    )

    print(

        await autonomous_ceo_agent()
    )


asyncio.run(
    main()
)