from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд авторизация"]
)

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/registration")
async def get_registration_page(request: Request):
    return templates.TemplateResponse(name="registration.html", context={"request": request})


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse(name="login.html", context={"request": request})


@router.get("/me")
async def get_user_page(request: Request):
    return templates.TemplateResponse(name="me.html", context={"request": request})
