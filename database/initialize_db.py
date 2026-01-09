import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import Base
from database import engine

def init_db():
    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()