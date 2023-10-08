
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import dependencies, models,database,schemas

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
    dependencies=[
        Depends(database.get_db)
    ],
)

@router.get("/", response_model=list[schemas.Post])
async def get_all_comment(
    commons: Annotated[dict, Depends(dependencies.common_parameters)],
    db: Session = Depends(database.get_db)
):
    return (
        db.query(models.Post)
        .offset(commons["skip"])
        .limit(commons["limit"])
        .all()
    )
