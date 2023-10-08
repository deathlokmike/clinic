from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/auth',
    tags=["Фронтенд авторизация"]
)

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/registration")
async def get_registration_page(request: Request):
    return templates.TemplateResponse(name='registration.html', context={"request": request})
