from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.appointments import (
    get_patient_info_and_appointments,
    get_available_appointments,
)
from app.lang.translator import Translator


router = APIRouter(tags=["Фронтенд"])

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/registration", response_class=HTMLResponse)
async def get_registration_page(request: Request):
    translator = Translator(request.state.locale)
    return templates.TemplateResponse(
        name="auth.html",
        context={
            "request": request,
            "func_name": "registerUser()",
            "redirect_url": "/login",
            **translator.get_translate("registration"),
            **translator.get_translate("header")
        },
    )


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    translator = Translator(request.state.locale)
    return templates.TemplateResponse(
        name="auth.html",
        context={
            "request": request,
            "func_name": "loginUser()",
            "redirect_url": "/registration",
            **translator.get_translate("login"),
            **translator.get_translate("header")
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
            "personal_data": info["personal_data"],
        },
    )


@router.get("/book_appointment", response_class=HTMLResponse)
async def get_new_appointment_page(
    request: Request, available=Depends(get_available_appointments)
):
    return templates.TemplateResponse(
        name="window.html",
        context={"request": request, "available": available},
    )

