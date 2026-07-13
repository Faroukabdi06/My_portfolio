from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(
    database_url,
    echo=True,
    pool_pre_ping=True
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()