from pydantic import BaseModel, EmailStr


class Student(BaseModel):
    id: int
    name: str
    course: str
    marks: float


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    course: str
    marks: float


class StudentUpdate(BaseModel):
    name: str
    email: EmailStr
    course: str
    marks: float