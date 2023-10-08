from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import Base


load_dotenv()


def create_tables():
    engine = create_engine(
        "postgresql://doadmin:AVNS_rSKdh9wwhtjvaDX5Dpa@db-postgresql-nyc3-54555-do-user-14774506-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"
    )
    Base.metadata.create_all(engine)
    return "ok"


def get_db():
    engine = create_engine(
        "postgresql://doadmin:AVNS_rSKdh9wwhtjvaDX5Dpa@db-postgresql-nyc3-54555-do-user-14774506-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"
    )
    session_gen = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_gen()
    try:
        yield db
    finally:
        db.close()
