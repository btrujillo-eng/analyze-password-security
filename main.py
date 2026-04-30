from app.api.v1.routers import analyze_password_security, health

from fastapi import FastAPI

app = FastAPI(
    title="Analyze Password security API",
    version="1.0.0"
)

app.include_router(analyze_password_security.router)
app.include_router(health.router)