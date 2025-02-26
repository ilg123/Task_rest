from fastapi import APIRouter, Depends, status
from app.services.task import TaskService
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/tasks", tags=["tasks"])

async def get_task_service(db: AsyncSession = Depends(get_db)) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)

@router.get("/", response_model=list[TaskResponse])
async def read_tasks(service: TaskService = Depends(get_task_service)):
    return await service.get_all_tasks()

@router.get("/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int, service: TaskService = Depends(get_task_service)):
    return await service.get_task(task_id)

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate, service: TaskService = Depends(get_task_service)):
    return await service.create_task(task_data)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_data: TaskUpdate, service: TaskService = Depends(get_task_service)):
    return await service.update_task(task_id, task_data)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    await service.delete_task(task_id)