from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn

from database.database import engine, get_db
from database.models import Base
from routes import users, trainings

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Training Database API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(trainings.router, prefix="/trainings", tags=["trainings"])

@app.get("/")
async def root():
    return {"message": "Training Database API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)