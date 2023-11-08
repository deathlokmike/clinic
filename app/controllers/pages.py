from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.appointments import get_patient_info_and_appointments


router = APIRouter(
    tags=["Фронтенд"]
)

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/registration", response_class=HTMLResponse)
async def get_registration_page(request: Request):
    return templates.TemplateResponse(name="registration.html", context={"request": request})


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse(name="login.html", context={"request": request})


@router.get("/me/appointments", response_class=HTMLResponse)
async def get_user_appointments(
        request: Request,
        info=Depends(get_patient_info_and_appointments)):
    
    return templates.TemplateResponse(
        "appointments.html", 
        {
            "request": request,
            "appointments": info["appointments"],
            "patient": info["patient"],
        },
    )
