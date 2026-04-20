import random
from datetime import datetime, timedelta

from faker import Faker

from database import SessionLocal
from models import Group, Teacher, Student, Subject, Grade

fake = Faker("uk_UA")


def random_date(start_days_ago: int = 180):
    start_date = datetime.now() - timedelta(days=start_days_ago)
    random_days = random.randint(0, start_days_ago)
    return (start_date + timedelta(days=random_days)).date()


def seed_database():
    session = SessionLocal()
    try:
        # Очищення таблиць
        session.query(Grade).delete()
        session.query(Student).delete()
        session.query(Subject).delete()
        session.query(Teacher).delete()
        session.query(Group).delete()
        session.commit()

        # Групи
        groups = [
            Group(name="Group A"),
            Group(name="Group B"),
            Group(name="Group C"),
        ]
        session.add_all(groups)
        session.commit()

        # Викладачі
        teachers = [Teacher(fullname=fake.name()) for _ in range(random.randint(3, 5))]
        session.add_all(teachers)
        session.commit()

        # Предмети
        subject_names = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "History",
            "Programming",
            "Databases",
            "English",
        ]
        random.shuffle(subject_names)
        selected_subjects = subject_names[: random.randint(5, 8)]

        subjects = []
        for subject_name in selected_subjects:
            teacher = random.choice(teachers)
            subjects.append(Subject(name=subject_name, teacher_id=teacher.id))

        session.add_all(subjects)
        session.commit()

        # Студенти
        students = []
        for _ in range(random.randint(30, 50)):
            student = Student(
                fullname=fake.name(),
                group_id=random.choice(groups).id,
            )
            students.append(student)

        session.add_all(students)
        session.commit()

        # Оцінки
        grades = []
        for student in students:
            num_grades = random.randint(10, 20)
            for _ in range(num_grades):
                subject = random.choice(subjects)
                grade = Grade(
                    student_id=student.id,
                    subject_id=subject.id,
                    grade=random.randint(60, 100),
                    date_received=random_date(),
                )
                grades.append(grade)

        session.add_all(grades)
        session.commit()

        print("Database seeded successfully!")

    except Exception as error:
        session.rollback()
        print(f"Error: {error}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()