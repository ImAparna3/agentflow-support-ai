from fastapi import FastAPI
from app.api.routes import router
from app.utils.middleware import catch_exceptions_middleware
from app.utils.logging import logger
from app.config.settings import settings

app = FastAPI(
    title="AgentFlow Support AI",
    description="Multi-agent customer support system backend",
    version="0.1.0",
)

# Add middleware
app.middleware("http")(catch_exceptions_middleware)

# Include API router
app.include_router(router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI application started")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("FastAPI application shutdown")
