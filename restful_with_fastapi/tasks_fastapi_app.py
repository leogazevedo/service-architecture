from fastapi import FastAPI
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