from database import SessionLocal
from models import Student, Group, Teacher, Subject, Grade
from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def print_title(title):
    print(f"\n{'=' * 60}")
    print(title)
    print(f"{'=' * 60}")


if __name__ == "__main__":
    session = SessionLocal()

    grade = session.query(Grade).first()

    if grade:
        student = session.query(Student).filter(Student.id == grade.student_id).first()
        subject = session.query(Subject).filter(Subject.id == grade.subject_id).first()
        teacher = session.query(Teacher).filter(Teacher.id == subject.teacher_id).first() if subject else None
        group = session.query(Group).filter(Group.id == student.group_id).first() if student else None

        student_id = student.id if student else None
        group_id = group.id if group else None
        teacher_id = teacher.id if teacher else None
        subject_id = subject.id if subject else None
    else:
        student_id = group_id = teacher_id = subject_id = None

    session.close()

    print_title("select_1")
    print(select_1())

    print_title("select_2")
    print(select_2(subject_id) if subject_id else "No subject found")

    print_title("select_3")
    print(select_3(subject_id) if subject_id else "No subject found")

    print_title("select_4")
    print(select_4())

    print_title("select_5")
    print(select_5(teacher_id) if teacher_id else "No teacher found")

    print_title("select_6")
    print(select_6(group_id) if group_id else "No group found")

    print_title("select_7")
    print(select_7(group_id, subject_id) if group_id and subject_id else "No group/subject found")

    print_title("select_8")
    print(select_8(teacher_id) if teacher_id else "No teacher found")

    print_title("select_9")
    print(select_9(student_id) if student_id else "No student found")

    print_title("select_10")
    print(
        select_10(student_id, teacher_id)
        if student_id and teacher_id
        else "No student/teacher found"
    )