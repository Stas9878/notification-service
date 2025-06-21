import uvicorn
from fastapi import FastAPI
from app.core.logging import setup_logging


setup_logging()

app = FastAPI()


if __name__ == '__main__':
    uvicorn.run(
        app='app.main:app',
        host='127.0.0.1',
        port=8000,
        reload=True,
        log_config=None
    )
