from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from api.routers import post, vote, user, location,comment

from api import dependencies


app = FastAPI(
    title="Gaia API",
    version="0.1.0",
)


@app.get("/")
async def root():
    return "hello"

