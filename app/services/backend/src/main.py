from fastapi import FastAPI

from .routers import v1

app = FastAPI(title="Looking Glass Factory Take Home Test")

app.include_router(
    v1.router,
    prefix="/v1"
)
