from fastapi import APIRouter, Depends
import schemas

from database.db import get_db
from database import crud
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/todos',
    tags=['todos']
)

@router.post('/', response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate,
                      user_id: int, db: Session =
                      Depends(get_db)
):
    return crud.create_user_todo(db, todo, user_id)

