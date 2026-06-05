def board_vote(
    objective: str,
    departments: list
):

    votes = {}

    for department in departments:

        votes[
            department
        ] = "approve"

    approved = len(votes)

    return f"""
EXECUTIVE BOARD

Objective:
{objective}

Votes:
{votes}

Decision:

APPROVED

Approval Count:
{approved}
"""