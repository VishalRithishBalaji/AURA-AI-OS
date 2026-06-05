from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import asyncio

from cognition.autonomous_loop import (
    autonomous_loop
)

from api.chat import router as chat_router
from api.voice import router as voice_router


# WINDOWS FIX FOR PLAYWRIGHT
asyncio.set_event_loop_policy(
    asyncio.WindowsProactorEventLoopPolicy()
)

app = FastAPI(title="AURA AI")


@app.on_event("startup")
async def startup_event():

    print("🚀 Starting Autonomous Loop")

    asyncio.create_task(
        autonomous_loop()
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(voice_router)


@app.get("/")
def root():

    return {
        "message": "AURA AI Running Successfully"
    }