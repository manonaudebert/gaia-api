import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import ( Boolean, Column, DateTime, Float,
                        ForeignKey, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
load_dotenv()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80),unique=True)
    phone = Column(String(120), unique=True)
    comments = relationship("Comment",back_populates='user' )
    votes = relationship("Vote",back_populates='user' )
    posts= relationship("Post",back_populates='user' )
    datetime = Column(DateTime, default=datetime.utcnow)

class Picture(Base):
    __tablename__ = "picture"
    id = Column(Integer, primary_key=True, autoincrement=True)
    postId =  Column(Integer, ForeignKey("post.id"))
    post = relationship("Post",back_populates="pictures")
    url = Column(String(500))
    urlMetadata  = Column(String(500))
    
    

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User",back_populates='comments' )
    postId = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post",back_populates='comments' )
    text= Column(String(500))
    datetime = Column(DateTime, default=datetime.utcnow)

    


class Vote(Base):
    __tablename__ = "vote"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User",back_populates='votes' )
    up = Column(Boolean)
    postId = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post",back_populates='votes' )
    datetime = Column(DateTime, default=datetime.utcnow)
    
class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    posts = relationship("Post",back_populates='location' )
    longUpper = Column(Float)
    longLower = Column(Float)
    latUpper = Column(Float)
    latLower = Column(Float)
    name = Column(String)
    
    

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User",back_populates='posts' )
    votes = relationship("Vote",back_populates='post' )
    comments = relationship("Comment",back_populates='post' )
    pictures = relationship("Picture",back_populates='post' )
    locationId = Column(Integer, ForeignKey("location.id"))
    location = relationship("Location", back_populates="posts")
    datetime = Column(DateTime, default=datetime.utcnow)
    title = Column(String(120),nullable=False)
    text = Column(String(2000),nullable=False)
    
    
    