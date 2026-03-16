from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    done: bool = False

tasks = [ 
    Task(id=1, 
         title="Buy groceries", 
         description="Milk, Cheese, Pizza, Fruit, Tyleno", 
         done=False),     
    Task(id=2, 
         title="Learn Python", 
         description="Need to find a good Python tutorial on the Web", 
         done=False
         )
    ]

@app.get("/todo/api/tasks")
def get_tasks()->list[Task]:
    return tasks

@app.get("/todo/api/tasks/{task_id}")
def get_task(task_id: int)->Task:
    task = [task for task in tasks if task.id == task_id]
    if len(task) == 0:
        raise HTTPException(404, f"Not found task with id {task_id}")
    return task[0]