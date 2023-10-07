from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse

from api import dependencies
from api.routers import post, vote, user, location,comment

app = FastAPI(
    title="Gaia API",
    version="0.1.0",
)




app.include_router(comment.router)
app.include_router(post.router)

@app.get("/")
async def root():
    return "hello"

