import os
from datetime import datetime
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status

from api import models

async def common_parameters(skip: int = 0, limit: int = 20):
    return {"skip": skip, "limit": limit}

