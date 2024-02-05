from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.controllers.appointments import (get_available_appointments,
                                          get_patient_info_and_appointments)
from app.lang.translator import Translator
from app.services.appointments.schemas import SPatientInfoWithAppointments

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
            **translator.get_translate("header"),
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
            **translator.get_translate("header"),
        },
    )


@router.get("/me", response_class=HTMLResponse)
async def get_user_appointments_page(
        request: Request, patient: SPatientInfoWithAppointments = Depends(get_patient_info_and_appointments)
):
    translator = Translator(request.state.locale)
    if patient is None:
        return templates.TemplateResponse(
            name="personal_data.html",
            context={
                "request": request,
                **translator.get_translate("personal_data"),
                **translator.get_translate("header"),
            },
        )
    return templates.TemplateResponse(
        name="appointments.html",
        context={
            "request": request,
            "appointments": patient.appointments,
            "personal_data": patient.personal_data,
            **translator.get_translate("header"),
            **translator.get_translate("appointments")
        },
    )


@router.get("/book_appointment", response_class=HTMLResponse)
async def get_new_appointment_page(request: Request, available=Depends(get_available_appointments)):
    return templates.TemplateResponse(
        name="window.html",
        context={"request": request, "available": available},
    )
