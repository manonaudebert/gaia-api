from fastapi import FastAPI

from api.routers import post, vote, user, location, comment

app = FastAPI(
    title="Gaia API",
    version="0.1.0",
)
app.include_router(comment.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
app.include_router(location.router)


@app.get("/")
async def root():
    return "hello"
