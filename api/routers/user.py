from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import dependencies, models,database,schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[
        Depends(database.get_db)
    ],
)

@router.get("/", response_model=list[schemas.User])
async def get_all_comment(
    commons: Annotated[dict, Depends(dependencies.common_parameters)],
    db: Session = Depends(database.get_db)
):
    return (
        db.query(models.User)
        .offset(commons["skip"])
        .limit(commons["limit"])
        .all()
    )