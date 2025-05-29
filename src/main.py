from fastapi import FastAPI
from src.shared.core.request_id_middleware import RequestIDMiddleware
from src.components.initiative_room.interface.initiative_router import router
from src.shared.core.config import settings
from src.shared.core.request_id_middleware import RequestIDMiddleware

import sentry_sdk

if settings.ENV in ["staging", "production"]:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
    )


app = FastAPI()
app.add_middleware(RequestIDMiddleware)
app.include_router(router)

print(f"🔧 App running in {settings.ENV} mode on port {settings.APP_PORT}")


import sentry_sdk
try:
    raise ValueError("Simulate exception to test Sentry")
except Exception as e:
    sentry_sdk.capture_exception(e)