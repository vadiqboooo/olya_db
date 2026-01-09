from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.database import get_db
from database.models import Training
from schemas import TrainingCreate, Training as TrainingSchema

router = APIRouter()

@router.post("/", response_model=TrainingSchema)
def create_training(training: TrainingCreate, db: Session = Depends(get_db)):
    db_training = Training(**training.model_dump())
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training

@router.get("/", response_model=List[TrainingSchema])
def read_trainings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trainings = db.query(Training).offset(skip).limit(limit).all()
    return trainings

@router.get("/{training_id}", response_model=TrainingSchema)
def read_training(training_id: int, db: Session = Depends(get_db)):
    training = db.query(Training).filter(Training.id == training_id).first()
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    return training

@router.put("/{training_id}", response_model=TrainingSchema)
def update_training(training_id: int, training_update: TrainingCreate, db: Session = Depends(get_db)):
    training = db.query(Training).filter(Training.id == training_id).first()
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    
    # Обновляем поля тренировки
    update_data = training_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(training, key, value)
    
    db.commit()
    db.refresh(training)
    return training

@router.delete("/{training_id}")
def delete_training(training_id: int, db: Session = Depends(get_db)):
    training = db.query(Training).filter(Training.id == training_id).first()
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    
    db.delete(training)
    db.commit()
    return {"message": "Training deleted successfully"}