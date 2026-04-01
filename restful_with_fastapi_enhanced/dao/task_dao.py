from typing import List

from model.task import Task, TaskInput, TaskUpdate

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


class TaskDAO:
    @classmethod
    def get_tasks(cls) -> List[Task] | None:
        return tasks

    @classmethod
    def get_task(cls, task_id: int) -> Task:
        task = [task for task in tasks if task.id == task_id]
        if len(task) == 0:
            return None
        return task[0]

    @classmethod
    def create_task(cls, task: TaskInput) -> Task:
        new_task: Task = Task(
            id=tasks[-1].id + 1,
            title=task.title,
            description=task.description,
            done=False,
        )
        tasks.append(new_task)
        return new_task

    @classmethod
    def update_task(cls, task_id: int, task_update: TaskUpdate) -> Task | None:
        found_tasks = [task for task in tasks if task.id == task_id]
        if len(found_tasks) == 0:
            return None
        task = found_tasks[0]
        task.title = task_update.title if task_update.title else task.title
        task.description = (
            task_update.description if task_update.description else task.description
        )
        task.done = task_update.done if task_update.done is not None else task.done
        return task

    @classmethod
    def delete_task(cls, task_id: int) -> bool | None:
        found_tasks = [task for task in tasks if task.id == task_id]
        if len(found_tasks) == 0:
            return None
        tasks.remove(found_tasks[0])
        return True
