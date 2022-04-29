import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("FRONTEND_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"
