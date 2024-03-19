from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app.controllers.appointments import get_patient_info_and_appointments
from app.lang.translator import Translator
from app.models.users.users import Users
from app.services.appointments.schemas import SPatientInfoWithAppointments
from app.services.users.dependencies import get_current_user

router = APIRouter(tags=["Фронтенд"])

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/", response_class=HTMLResponse)
async def get_index_page(request: Request, user: Users = Depends(get_current_user)):
    if user:
        return RedirectResponse(url="/me")
    else:
        return RedirectResponse(url="/login")


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


async def not_found_error(request: Request, exc: HTTPException):
    translator = Translator(request.state.locale)
    return templates.TemplateResponse(
        name="404.html",
        context={
            "request": request,
            **translator.get_translate("page_not_found")
        },
        status_code=404)


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
        name="me/main.html",
        context={
            "request": request,
            "appointments": patient.appointments,
            "personal_data": patient.personal_data,
            **translator.get_translate("header"),
            **translator.get_translate("appointments")
        },
    )
