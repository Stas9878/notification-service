import logging

logger = logging.getLogger(__name__)


async def send_notification(user_id: int, event_type: str, data: dict):
    logger.info(f'[x] Processing notification for user {user_id}, type: {event_type}, data: {data}')
    logger.info('[x] Notification sent')