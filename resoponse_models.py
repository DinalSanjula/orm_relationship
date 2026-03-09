from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TeacherProfileBase(BaseModel):
    qualification : Optional[str] = Field(None, max_length=300)
    department : Optional[str] = Field(None, max_length=200)
    office_number : Optional[str] = Field(None, max_length=30)
    bio: Optional[str] = None

    class Config:
        from_attributes = True

class TeacherProfileCreate(TeacherProfileBase):
    pass

class TeacherProfileUpdate(TeacherProfileBase):
    pass

class TeacherProfileResponse(TeacherProfileBase):
    id:int
    teacher_id : int

class TeacherBase(BaseModel):
    name : str = Field(...,min_length=3, max_length=255)
    email:str

class TeacherCreate(TeacherBase):
    profile: Optional[TeacherProfileCreate] = None

class TeacherResponse(TeacherBase):
    id: int
    created_at: datetime
    profile: Optional[TeacherProfileCreate] = None

    class Config:
        from_attributes = True