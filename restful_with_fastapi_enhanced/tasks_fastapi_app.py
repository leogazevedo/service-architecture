from fastapi import FastAPI
from router.task_router import task_router

app = FastAPI()

app.include_router(task_router)
