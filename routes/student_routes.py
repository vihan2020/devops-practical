
from fastapi import APIRouter, HTTPException
from models.student_model import Student, StudentCreate, StudentUpdate
from controllers import student_controller
from controllers.student_controller import students

router = APIRouter()


@router.post("/students/", response_model=Student)
def create_student(student: StudentCreate):
    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "course": student.course,
        "marks": student.marks
    }

    students.append(new_student)

    return new_student


@router.get("/students/", response_model=list[Student])
def get_students():
    return students


@router.get("/course/{course}")
def get_students_by_course(course: str):
    return student_controller.getStudentsByCourse(course)


@router.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


@router.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate):
    for existing_student in students:
        if existing_student["id"] == student_id:
            existing_student["name"] = student.name
            existing_student["course"] = student.course
            existing_student["marks"] = student.marks

            return existing_student

    raise HTTPException(status_code=404, detail="Student not found")


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")
