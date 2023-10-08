from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers.pages import router as router_view

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/views/static"), name="static")
app.include_router(router_view)
