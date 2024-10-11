from fastapi import FastAPI
from schemas import Todo
from database.db import Session, engine
from database import models
import uvicorn
from routers.users import router as user_router
from routers.todos import router as todos_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(todos_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000)