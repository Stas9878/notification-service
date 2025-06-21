import logging
import aio_pika
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from app.core.settings import settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def get_rabbitmq_connection() -> AsyncGenerator[aio_pika.Connection, None]:
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
    try:
        yield connection
    except Exception as err:
        logger.critical(f'[x] RabbitMQ connection error: {err}')
        raise err
