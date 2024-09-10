from sqlmodel import Field
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base

class Role(Enum):
    admin = "admin"
    editor = "editor"
    user = "user"
    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role: Role = Field(default=Role.user)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")