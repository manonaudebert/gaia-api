import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()


def get_db():
    engine = create_engine("postgresql://doadmin:AVNS_rSKdh9wwhtjvaDX5Dpa@db-postgresql-nyc3-54555-do-user-14774506-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require")
    session_gen = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    

    try:
        yield session_gen
    finally:
        session_gen.close()
