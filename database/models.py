from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    training_type_1 = Column(String)
    training_type_2 = Column(String)
    training_type_3 = Column(String)
    goal = Column(String)
    location = Column(String)
    
    # Связь с тренировками
    trainings = relationship("Training", back_populates="user")

class Training(Base):
    __tablename__ = "trainings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    monday = Column(Text)
    tuesday = Column(Text)
    wednesday = Column(Text)
    thursday = Column(Text)
    friday = Column(Text)
    saturday = Column(Text)
    sunday = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Связь с пользователем
    user = relationship("User", back_populates="trainings")