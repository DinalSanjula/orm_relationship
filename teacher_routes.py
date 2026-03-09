from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from database_config import get_db
from resoponse_models import TeacherCreate, TeacherResponse
from teacher_repository import TeacherRepository

router = APIRouter(prefix="/teachers",tags=["Teacher endpoints"])

@router.post("/",response_model=TeacherResponse,status_code=status.HTTP_201_CREATED)
async def  create_teacher(data:TeacherCreate, db: AsyncSession= Depends(get_db)):

    repo = TeacherRepository(db)

    teacher = await repo.create(data)

    return teacher

@router.get("/id/{id}",response_model= TeacherResponse,status_code=status.HTTP_200_OK)
async def get_teacher_by_id(teacher_id:int,db: AsyncSession= Depends(get_db)):
    repo = TeacherRepository(db)
    teacher = await repo.get_by_id(teacher_id)

    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Teacher not found")

    return teacher

@router.get("/",response_model= List[TeacherResponse],status_code=status.HTTP_200_OK)
async def get_all_teachers(offset:int=0,limit:int =20,db: AsyncSession= Depends(get_db)):
    repo = TeacherRepository(db)
    teachers = await repo.get_all_teachers(offset=offset,limit=limit)

    if not teachers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Teacher not found")

    return teachers



