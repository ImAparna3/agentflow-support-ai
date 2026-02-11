from loguru import logger
from app.config.settings import settings

logger.remove()
logger.add(
    "logs/app.log",
    level=settings.LOG_LEVEL,
    rotation="10 MB",
    retention="7 days",
    enqueue=True,
    backtrace=True,
    diagnose=True
)

logger.info("Logger initialized")
