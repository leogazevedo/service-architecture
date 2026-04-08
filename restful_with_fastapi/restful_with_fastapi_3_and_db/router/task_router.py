from dao.task_dao import TaskDAO
from fastapi import APIRouter, HTTPException
from model.task import Task, TaskInput, TaskUpdate

task_router = APIRouter(prefix="/todo/api/tasks", tags=["Tasks"])


@task_router.get("/")
def get_tasks() -> list[Task]:
    return TaskDAO.get_tasks()


@task_router.get("/{task_id}")
def get_task(task_id: int) -> Task:
    task = TaskDAO.get_task(task_id)
    if not task:
        raise HTTPException(404, f"Not found task with id {task_id}.")
    return task


@task_router.post("/")
def create_task(task_input: TaskInput) -> Task:
    return TaskDAO.create_task(task=task_input)


@task_router.put("/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate) -> Task:
    updated_task = TaskDAO.update_task(task_id=task_id, task_update=task_update)
    if not updated_task:
        raise HTTPException(404, f"Not found task with id {task_id}")
    return updated_task


@task_router.delete("/{task_id}")
def delete_task(task_id: int) -> bool:
    if not TaskDAO.delete_task(task_id=task_id):
        raise HTTPException(404, f"Not found task with id {task_id}")
    return True
