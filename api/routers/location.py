from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import dependencies, models,database,schemas

router = APIRouter(
    prefix="/locations",
    tags=["Locations"],
    dependencies=[
        Depends(database.get_db)
    ],
)

@router.get("/", response_model=list[schemas.Location])
async def get_all_locations(
    commons: Annotated[dict, Depends(dependencies.common_parameters)],
    db: Session = Depends(database.get_db)
):
    return (
        db.query(models.Location)
        .offset(commons["skip"])
        .limit(commons["limit"])
        .all()
    )
