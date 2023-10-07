from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse



app = FastAPI(
    title="Gaia API",
    version="0.1.0",
)


@app.get("/")
async def root():
    return "hello"

