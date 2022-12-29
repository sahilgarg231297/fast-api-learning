from fastapi import FastAPI
from topics import router

app = FastAPI()

app.include_router(router, prefix="/topics")
