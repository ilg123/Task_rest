from fastapi import HTTPException, status
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def get_all_tasks(self) -> list[TaskResponse]:
        return await self.repository.get_all()

    async def get_task(self, task_id: int) -> TaskResponse:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return task

    async def create_task(self, task_data: TaskCreate) -> TaskResponse:
        return await self.repository.create(task_data.dict())

    async def update_task(self, task_id: int, task_data: TaskUpdate) -> TaskResponse:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return await self.repository.update(task, task_data.dict())

    async def delete_task(self, task_id: int) -> None:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        await self.repository.delete(task)