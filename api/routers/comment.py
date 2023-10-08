from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import dependencies, models, database, schemas

router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
    dependencies=[Depends(database.get_db)],
)


@router.get("/", response_model=list[schemas.Comment])
async def get_all_comments(
    commons: Annotated[dict, Depends(dependencies.common_parameters)],
    db: Session = Depends(database.get_db),
):
    return (
        db.query(models.Comment).offset(commons["skip"]).limit(commons["limit"]).all()
    )
