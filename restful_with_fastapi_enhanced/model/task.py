from pydantic import BaseModel


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
