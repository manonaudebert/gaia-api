import os
from datetime import datetime
from typing import Annotated

import requests
from fastapi import Depends, Header, HTTPException, status

from api import config, database, models

