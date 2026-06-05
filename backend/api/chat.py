from fastapi import APIRouter
from pydantic import BaseModel

import json

from agents.orchestrator import (
    route_task
)

router = APIRouter()


class ChatRequest(BaseModel):

    message: str


@router.post("/chat")
async def chat(req: ChatRequest):

    response = await route_task(
        req.message
    )

    # =========================
    # SAFE SERIALIZATION
    # =========================

    if not isinstance(
        response,
        str
    ):

        try:

            response = json.dumps(

                response,

                indent=2,

                default=str
            )

        except Exception:

            response = str(
                response
            )

    return {

        "response":
        response
    }