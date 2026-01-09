from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL базы данных (используем SQLite для простоты)
DATABASE_URL = "sqlite:///./training.db"

# Создаем движок базы данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для моделей
Base = declarative_base()

# Функция получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()