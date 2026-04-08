from fastapi import FastAPI
from router.task_router import task_router
from dao.database import init_db

app = FastAPI()

app.include_router(task_router)

init_db()
