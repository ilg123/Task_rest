from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import Task

class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(Task))
        return result.scalars().all()

    async def get_by_id(self, task_id: int) -> Task | None:
        result = await self.session.execute(select(Task).filter(Task.id == task_id))
        return result.scalar_one_or_none()

    async def create(self, task_data: dict) -> Task:
        task = Task(**task_data)
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def update(self, task: Task, task_data: dict) -> Task:
        for key, value in task_data.items():
            setattr(task, key, value)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete(self, task: Task) -> None:
        await self.session.delete(task)
        await self.session.commit()