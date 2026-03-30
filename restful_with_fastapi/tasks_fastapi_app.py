from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    done: bool = False


class TaskInput(BaseModel):
    title: str
    description: str | None = None
    done: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool = False


tasks = [
    Task(
        id=1,
        title="Buy groceries",
        description="Milk, Cheese, Pizza, Fruit, Tyleno",
        done=False,
    ),
    Task(
        id=2,
        title="Learn Python",
        description="Need to find a good Python tutorial on the Web",
        done=False,
    ),
]


@app.get("/todo/api/tasks")
def get_tasks() -> list[Task]:
    return tasks


@app.get("/todo/api/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    task = [task for task in tasks if task.id == task_id]
    if len(task) == 0:
        raise HTTPException(404, f"Not found task with id {task_id}")
    return task[0]


@app.post("/todo/api/tasks")
def create_task(task: TaskInput) -> Task:
    new_task: Task = Task(
        id=tasks[-1].id + 1,
        title=task.title,
        description=task.description,
        done=False,
    )
    tasks.append(new_task)
    return new_task


@app.put("/todo/api/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate) -> Task:
    found_tasks = [task for task in tasks if task.id == task_id]
    if len(found_tasks) == 0:
        raise HTTPException(404, f"Not found task with id {task_id}")
    task = found_tasks[0]
    task.title = task_update.title if task_update.title else task.title
    task.description = (
        task_update.description if task_update.description else task.description
    )
    task.done = task_update.done if task_update.done else task.done
    return task


@app.delete("/todo/api/tasks/{task_id}")
def delete_task(task_id: int) -> bool:
    found_tasks = [task for task in tasks if task.id == task_id]
    if len(found_tasks) == 0:
        raise HTTPException(404, f"Not found task with id {task_id}")
    tasks.remove(found_tasks[0])
    return True
