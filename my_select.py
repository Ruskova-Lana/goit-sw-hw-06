from sqlalchemy import func, desc, and_

from database import SessionLocal
from models import Student, Group, Teacher, Subject, Grade


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.fullname,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(5)
            .all()
        )
        return result
    finally:
        session.close()


def select_2(subject_id: int):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.fullname,
                Subject.name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Subject.id == subject_id)
            .group_by(Student.id, Subject.id)
            .order_by(desc("avg_grade"))
            .first()
        )
        return result
    finally:
        session.close()


def select_3(subject_id: int):
    """
    Знайти середній бал у групах з певного предмета.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Group.name,
                Subject.name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .select_from(Group)
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Subject.id == subject_id)
            .group_by(Group.id, Subject.id)
            .order_by(Group.name)
            .all()
        )
        return result
    finally:
        session.close()


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    session = SessionLocal()
    try:
        result = session.query(func.round(func.avg(Grade.grade), 2)).scalar()
        return result
    finally:
        session.close()


def select_5(teacher_id: int):
    """
    Знайти які курси читає певний викладач.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Teacher.fullname, Subject.name)
            .join(Subject, Subject.teacher_id == Teacher.id)
            .filter(Teacher.id == teacher_id)
            .all()
        )
        return result
    finally:
        session.close()


def select_6(group_id: int):
    """
    Знайти список студентів у певній групі.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Group.name, Student.fullname)
            .join(Student, Student.group_id == Group.id)
            .filter(Group.id == group_id)
            .order_by(Student.fullname)
            .all()
        )
        return result
    finally:
        session.close()


def select_7(group_id: int, subject_id: int):
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Group.name,
                Subject.name,
                Student.fullname,
                Grade.grade,
                Grade.date_received,
            )
            .select_from(Group)
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(and_(Group.id == group_id, Subject.id == subject_id))
            .order_by(Student.fullname, Grade.date_received)
            .all()
        )
        return result
    finally:
        session.close()


def select_8(teacher_id: int):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Teacher.fullname,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Subject, Subject.teacher_id == Teacher.id)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(Teacher.id == teacher_id)
            .group_by(Teacher.id)
            .first()
        )
        return result
    finally:
        session.close()


def select_9(student_id: int):
    """
    Знайти список курсів, які відвідує певний студент.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Student.fullname, Subject.name)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Student.id == student_id)
            .distinct()
            .all()
        )
        return result
    finally:
        session.close()


def select_10(student_id: int, teacher_id: int):
    """
    Список курсів, які певному студенту читає певний викладач.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Student.fullname, Teacher.fullname, Subject.name)
            .select_from(Student)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .join(Teacher, Teacher.id == Subject.teacher_id)
            .filter(and_(Student.id == student_id, Teacher.id == teacher_id))
            .distinct()
            .all()
        )
        return result
    finally:
        session.close()