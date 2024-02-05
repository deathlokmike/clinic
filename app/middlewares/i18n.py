from starlette.middleware.base import (BaseHTTPMiddleware,
                                       RequestResponseEndpoint)
from starlette.requests import Request


class I18nMiddleware(BaseHTTPMiddleware):
    WHITE_LIST = ["ru-RU", "en-US"]

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        locale = request.headers.get("Accept-Language", None) or "en-US"
        if locale[:5] not in self.WHITE_LIST:
            locale = "en-US"
        request.state.locale = locale[:5]
        return await call_next(request)
