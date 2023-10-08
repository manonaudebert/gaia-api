import json
import re
from datetime import date, datetime,time
from typing import Union


from fastapi import HTTPException, status
from pydantic import BaseModel, validator

from api import dependencies

class _BaseModel(BaseModel):
    class Config:
        from_attributes=True

class UserCreate(_BaseModel):
    username : str
    phone : str
    datetime : datetime
    
class User(_BaseModel):
    id : int
    username : str
    phone : str
    datetime : datetime

class CommentCreate(_BaseModel):
    text : str
    postId : int
    userId : int
    datetime : datetime
    

class Comment(_BaseModel):
    id : int
    text : str
    postId : int
    user : User
    datetime : datetime
    
class VoteCreate(_BaseModel):
    up : bool
    postId : int
    userId : int
    datetime : datetime
    
class Vote(_BaseModel):
    id : int
    up : bool
    postId : int
    userId : int
    datetime : datetime
    
class PictureCreate(_BaseModel):
    url : str
    postId : int
    
class Picture(_BaseModel):
    id : int
    url : str
    postId : int
    
class LocationCreate(_BaseModel):
    longUpper : float
    longLower : float
    latUpper : float
    latLower : float
    name : str

class Location(_BaseModel):
    id : int
    longUpper : float
    longLower : float
    latUpper : float
    latLower : float
    name : str
    
class PostCreate(_BaseModel):
    title : str
    text : str
    locationId : int
    userId : int
    pictures : list[PictureCreate]
    datetime : datetime
    
class Post(_BaseModel):
    id : int
    title : str
    text : str
    location : Location
    user : User
    pictures : list[Picture]
    comments : list[Comment]
    votes : list[Vote]
    datetime : datetime




