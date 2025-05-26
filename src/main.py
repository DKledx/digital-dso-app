from fastapi import FastAPI

from src.components.initiative_room.interface.initiative_router import \
    router as initiative_router

app = FastAPI()
app.include_router(initiative_router)
