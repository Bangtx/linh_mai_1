from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    name = Column(String)
    age = Column(Integer)
    province = Column(String)
    sex = Column(String)
    reason = Column(String)
    background_disease = Column(String)
    img_name = Column(String)
    point_1 = Column(Integer)
    point_2 = Column(Integer)
    point_3 = Column(Integer)
    point_4 = Column(Integer)
    point_5 = Column(Integer)
    point_6 = Column(Integer)
    point_7 = Column(Integer)
    point_8 = Column(Integer)
