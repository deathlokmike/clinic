from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers.pages import router as router_view
from app.controllers.pneumonia import router as router_pneumonia
from app.controllers.auth import router as router_auth

app = FastAPI(title="Clinic API")
app.mount("/static", StaticFiles(directory="app/views/static"), name="static")
app.include_router(router_view)
app.include_router(router_auth)
app.include_router(router_pneumonia)
