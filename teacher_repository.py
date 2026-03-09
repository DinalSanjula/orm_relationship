from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from db_models import Teacher, TeacherProfile
from resoponse_models import TeacherCreate


class TeacherRepository:

    def __init__(self, db: AsyncSession):

        self.db = db

    async def create(self,data: TeacherCreate) -> Teacher :

        teacher = Teacher(name=data.name, email =data.email)

        if data.profile:
            teacher.profile = TeacherProfile(
                qualifications=data.profile.qualification,
                department=data.profile.department,
                office_number=data.profile.office_number,
                bio=data.profile.bio
            )

        self.db.add(teacher)
        await self.db.commit()
        await self.db.refresh(teacher)
        return teacher

    async def get_by_id(self, teacher_id:int) -> Teacher | None:

        query = (
            select(Teacher)
            .where(Teacher.id == teacher_id)
            .options(
                joinedload(Teacher.profile),
                selectinload(Teacher.courses)
            )
        )

        result = await self.db.execute(query)
        return result.unique().scalars().first()

