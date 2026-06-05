from fastapi import APIRouter
from pydantic import BaseModel

from agents.orchestrator import route_task

router = APIRouter()


class VoiceRequest(BaseModel):
    text: str


@router.post("/voice")

async def voice_chat(req: VoiceRequest):

    response = await route_task(req.text)

    return {
        "response": response
    }