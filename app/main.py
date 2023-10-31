from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers.pages import router as router_view
from app.controllers.pneumonia import router as router_pneumonia
from app.controllers.auth import router as router_auth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Clinic API")
app.mount("/static", StaticFiles(directory="app/views/static"), name="static")
app.include_router(router_view)
app.include_router(router_auth)
app.include_router(router_pneumonia)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)
