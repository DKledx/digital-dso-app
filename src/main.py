from fastapi import FastAPI
from src.shared.core.request_id_middleware import RequestIDMiddleware
from src.components.initiative_room.interface.initiative_router import router

app = FastAPI()
app.add_middleware(RequestIDMiddleware)
app.include_router(router)