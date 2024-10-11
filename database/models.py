import sqlalchemy as sa
from .db import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)

    todos = relationship('Todo', back_populates='user')


class Todo(Base):
    __tablename__ = 'todos'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    is_finished = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now())
    updated_at = sa.Column(sa.DateTime, default=datetime.now())

    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    user = relationship('User', back_populates='todos')