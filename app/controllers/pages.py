from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.appointments import get_patient_info_and_appointments


router = APIRouter(tags=["Фронтенд"])

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/registration", response_class=HTMLResponse)
async def get_registration_page(request: Request):
    return templates.TemplateResponse(
        name="auth.html",
        context={
            "request": request,
            "context": "Регистрация",
            "func_name": "registerUser()",
            "btn_name": "Подтвердить",
            "pre_redirect_text": "Уже зарегистрированы?",
            "redirect_url": "/login",
            "redirect_text": "Войти",
        },
    )


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse(
        name="auth.html",
        context={
            "request": request,
            "context": "Вход в систему",
            "func_name": "loginUser()",
            "btn_name": "Войти",
            "pre_redirect_text": "Не зарегистрированы?",
            "redirect_url": "/registration",
            "redirect_text": "Создать аккаунт",
        },
    )


@router.get("/me/appointments", response_class=HTMLResponse)
async def get_user_appointments_page(
    request: Request, info=Depends(get_patient_info_and_appointments)
):
    return templates.TemplateResponse(
        name="appointments.html",
        context={
            "request": request,
            "appointments": info["appointments"],
            "patient": info["patient"],
        },
    )


@router.get("/appointment", response_class=HTMLResponse)
async def get_new_appointment_page(request: Request):
    colors = ["Red", "Blue", "Black", "Orange"]
    return templates.TemplateResponse(
        name="new_appointment.html",
        context={"request": request, "colors": colors},
    )
