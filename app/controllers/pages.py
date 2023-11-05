from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.appointments import get_patient_appointments


router = APIRouter(
    tags=["Фронтенд авторизация"]
)

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/registration", response_class=HTMLResponse)
async def get_registration_page(request: Request):
    return templates.TemplateResponse(name="registration.html", context={"request": request})


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse(name="login.html", context={"request": request})


@router.get("/user/me", response_class=HTMLResponse)
async def get_user_page(request: Request,
                        appointments=Depends(get_patient_appointments)):
    return templates.TemplateResponse(
        "me.html", 
        {
            "request": request,
            "appointments": appointments,
        },
    )
