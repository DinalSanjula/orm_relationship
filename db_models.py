from datetime import datetime
from typing import Optional

from sqlalchemy import String, false, func, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase): #DRY Principle - Dont Repeat Yourself
    pass

class Teacher(Base):

    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(255),nullable=False)
    email: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=datetime.now())

    profile:Mapped[Optional["TeacherProfile"]] = relationship(
        back_populates="teacher",
        uselist=False,#thi
        cascade="all, delete-orphan",
        lazy="joined"
    )

class TeacherProfile(Base):
    __tablename__ = "teacher_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey(column="teachers.id", ondelete="CASCADE"))
    qualifications: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
    department: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    office_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(Text,nullable=True)

    teacher: Mapped["Teacher"] = relationship(back_populates="profile")