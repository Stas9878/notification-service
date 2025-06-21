import uvicorn
from fastapi import FastAPI

from app.core.logging import setup_logging
from app.routers.events import router as events_router


setup_logging()

app = FastAPI()
app.include_router(events_router, prefix='/events')


if __name__ == '__main__':
    uvicorn.run(
        app='app.main:app',
        host='127.0.0.1',
        port=8000,
        reload=True,
        log_config=None
    )
