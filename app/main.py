import asyncio
from contextlib import asynccontextmanager

import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from app.common.exceptions import TokenAbsentException
from app.config import settings
from app.controllers.appointments import router as router_appointments
from app.controllers.auth import router as router_auth
from app.controllers.pages import router as router_view
from app.controllers.pneumonia import router as router_pneumonia
from app.controllers.users import router as router_user
from app.middlewares.i18n import I18nMiddleware
from app.middlewares.logging import LoggerMiddleware
from app.services.schedule.tasks import set_actual_schedule


@asynccontextmanager
async def lifespan(_: FastAPI):
    asyncio.ensure_future(set_actual_schedule())
    yield


sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI(title="Clinic API", lifespan=lifespan)

main_router = APIRouter()
main_router.include_router(router_view)
main_router.include_router(router_auth)
main_router.include_router(router_pneumonia)
main_router.include_router(router_appointments)
main_router.include_router(router_user)

app.include_router(main_router)
app.mount("/static", StaticFiles(directory="app/views/static"), name="static")

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)
app.add_middleware(I18nMiddleware)
app.add_middleware(LoggerMiddleware)


@app.exception_handler(TokenAbsentException)
async def unicorn_exception_handler(request: Request, exc: TokenAbsentException):
    return RedirectResponse(url="/login")
