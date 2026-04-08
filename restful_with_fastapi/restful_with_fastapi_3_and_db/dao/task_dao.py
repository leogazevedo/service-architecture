from typing import List

from dao.database import get_connection
from model.task import Task, TaskInput, TaskUpdate


class TaskDAO:
    @classmethod
    def get_tasks(cls) -> List[Task]:
        with get_connection() as conn:
            rows = conn.execute("SELECT id, title, description, done FROM task").fetchall()
        return [Task(id=row["id"], title=row["title"], description=row["description"], done=bool(row["done"])) for row in rows]

    @classmethod
    def get_task(cls, task_id: int) -> Task | None:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT id, title, description, done FROM task WHERE id = ?", (task_id,)
            ).fetchone()
        if row is None:
            return None
        return Task(id=row["id"], title=row["title"], description=row["description"], done=bool(row["done"]))

    @classmethod
    def create_task(cls, task: TaskInput) -> Task:
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO task (title, description, done) VALUES (?, ?, ?)",
                (task.title, task.description, int(task.done)),
            )
            conn.commit()
            task_id = cursor.lastrowid
        return Task(id=task_id, title=task.title, description=task.description, done=task.done)

    @classmethod
    def update_task(cls, task_id: int, task_update: TaskUpdate) -> Task | None:
        existing = cls.get_task(task_id)
        if existing is None:
            return None
        new_title = task_update.title if task_update.title else existing.title
        new_description = task_update.description if task_update.description else existing.description
        new_done = task_update.done if task_update.done is not None else existing.done
        with get_connection() as conn:
            conn.execute(
                "UPDATE task SET title = ?, description = ?, done = ? WHERE id = ?",
                (new_title, new_description, int(new_done), task_id),
            )
            conn.commit()
        return Task(id=task_id, title=new_title, description=new_description, done=new_done)

    @classmethod
    def delete_task(cls, task_id: int) -> bool | None:
        if cls.get_task(task_id) is None:
            return None
        with get_connection() as conn:
            conn.execute("DELETE FROM task WHERE id = ?", (task_id,))
            conn.commit()
        return True
