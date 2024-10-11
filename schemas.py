# файл для моделей валидации данных

from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class TodoStatus(str, Enum):
    in_process = 'В процессе'
    finished = 'Завершено'


class Todo(BaseModel):
    todo_id: int
    title: str
    description: str | None = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    status: TodoStatus = TodoStatus.in_process


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    is_active: bool
    todos: list[Todo]

    class Config:
        orm_mode = True


