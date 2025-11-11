# Conexión a SQLite con SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(
   settings.database_url,
   connect_args={"check_same_thread": False}  # necesario para SQLite en single-thread
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()