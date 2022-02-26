from typing import Optional, List
from datetime import date
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class Patient(BaseModel):
    date: date
    name: str
    age: str
    province: str
    sex: str
    reason: str = None
    background_disease: str = None
    img_name: str
    point_1: int
    point_2: int
    point_3: int
    point_4: int
    point_5: int
    point_6: int
    point_7: int
    point_8: int