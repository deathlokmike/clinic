from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.routing import APIRouter
from app.controllers.pages import router as router_view
from app.controllers.pneumonia import router as router_pneumonia
from app.controllers.auth import router as router_auth
from app.controllers.appointments import router as router_appointments
from fastapi.middleware.cors import CORSMiddleware
from app.common.exceptions import TokenAbsentException
from fastapi import Request

from starlette.responses import RedirectResponse

app = FastAPI(title="Clinic API")
app.mount("/static", StaticFiles(directory="app/views/static"), name="static")

main_router = APIRouter()
main_router.include_router(router_view)
main_router.include_router(router_auth)
main_router.include_router(router_pneumonia)
main_router.include_router(router_appointments)

app.include_router(main_router)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)

@app.exception_handler(TokenAbsentException)
async def unicorn_exception_handler(request: Request, exc: TokenAbsentException):
    return RedirectResponse(url='/login')