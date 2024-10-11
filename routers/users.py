from fastapi import APIRouter, Depends
from database.db import get_db
import schemas
from sqlalchemy.orm import Session
from database import crud

router = APIRouter(
    prefix='/users'
)


@router.post('/', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.get('/{user_id}')
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, user_id)


@router.get('/{email}')
async def read_user_by_email(email: str, db: Session = Depends(get_db)):
    return crud.get_user_by_email(db, email)


@router.get('/', response_model=list[schemas.User])
async def read_users(db: Session = Depends(get_db),
                     skip: int = 0, limit: int =100):
    return crud.get_users(db, skip, limit)
