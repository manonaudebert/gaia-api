from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc

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

@router.get("/{location_id}/feed", response_model=list[schemas.Location])
async def get_feed_from_location(
    location_id: int,
    commons: Annotated[dict, Depends(dependencies.common_parameters)],
    db: Session = Depends(database.get_db)
):
    return (db.query(models.Post).filter_by(location_id=location_id)
            .order_by(desc(models.Post.datetime))
            .offset(commons["skip"])
        .limit(commons["limit"])
        .all())

