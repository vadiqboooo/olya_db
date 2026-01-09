from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    user_id: str
    name: str
    training_type_1: Optional[str] = None
    training_type_2: Optional[str] = None
    training_type_3: Optional[str] = None
    goal: Optional[str] = None
    location: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

class TrainingBase(BaseModel):
    title: str
    type: str
    monday: Optional[str] = None
    tuesday: Optional[str] = None
    wednesday: Optional[str] = None
    thursday: Optional[str] = None
    friday: Optional[str] = None
    saturday: Optional[str] = None
    sunday: Optional[str] = None
    user_id: int

class TrainingCreate(TrainingBase):
    pass

class Training(TrainingBase):
    id: int
    
    class Config:
        from_attributes = True