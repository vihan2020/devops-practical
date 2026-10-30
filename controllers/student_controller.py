from models.student_model import Student, StudentCreate, StudentUpdate


students = []


def create_student(student: StudentCreate):
    new_id = len(students) + 1

    new_student = Student(
        id=new_id,
        name=student.name,
        course=student.course,
        marks=student.marks
    )

    students.append(new_student)
    return new_student


def get_all_students():
    return students


def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    return None


def update_student(student_id: int, student: StudentUpdate):
    for index, existing_student in enumerate(students):
        if existing_student.id == student_id:
            updated_student = Student(
                id=student_id,
                name=student.name,
                course=student.course,
                marks=student.marks
            )

            students[index] = updated_student
            return updated_student

    return None


def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return True

    return False

def getStudentsByCourse(course: str):
    result = []

    for student in students:
        if student["course"].lower() == course.lower():
            result.append(student)

    return result