from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request


class I18nMiddleware(BaseHTTPMiddleware):
    WHITE_LIST = ["ru-RU", "en-US", "sv-SV"]

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        locale = request.headers.get("Accept-Language", None) or "en-US"
        if locale not in self.WHITE_LIST:
            locale = "en-US"
        request.state.locale = locale
        return await call_next(request)
