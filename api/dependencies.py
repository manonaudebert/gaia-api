import os
from datetime import datetime
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status

from api import models

