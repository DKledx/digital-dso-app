from fastapi import FastAPI
from src.shared.core.request_id_middleware import RequestIDMiddleware
from src.components.initiative_room.interface.initiative_router import router
from src.shared.core.config import settings

app = FastAPI()
app.add_middleware(RequestIDMiddleware)
app.include_router(router)

print(f"🔧 App running in {settings.ENV} mode on port {settings.APP_PORT}")