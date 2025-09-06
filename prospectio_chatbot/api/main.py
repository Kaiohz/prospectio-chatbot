from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import ChainlitSettings
from api.auth.auth import auth_router

app = FastAPI()
settings = ChainlitSettings()
AUTH_PATH="/rest/v1/{}"

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix=AUTH_PATH.format("auth"), tags=["Auth"])
