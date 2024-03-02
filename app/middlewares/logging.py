import time

from starlette.middleware.base import (BaseHTTPMiddleware,
                                       RequestResponseEndpoint)
from starlette.requests import Request

from app.logger import logger


class LoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info("Request handling time", extra={
            "process_time": round(process_time, 4),
            "client_ip": request.client.host
        })
        return response
