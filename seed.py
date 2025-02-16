import random
from datetime import datetime, timedelta

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher, Group, Student, Subject, Grade

fake = Faker('uk-UA')

subjects_list = [
    "Mathematics", "Physics", "Chemistry", "Biology", "History",
    "Literature", "Geography", "Computer Science"
]

def insert_students():
    for _ in range(50):
        student = Student(
            fullname=fake.name(),
            group_id=random.randint(1, 3))
        session.add(student)

def insert_teachers():
    for _ in range(5):
        teacher = Teacher(fullname=fake.name())
        session.add(teacher)

def insert_groups():
    for _ in range(3):
        group = Group(name=fake.bs())
        session.add(group)

def insert_subjects():
    for subject in subjects_list:
        subject = Subject(
            name=subject,
            teacher_id=random.randint(1, 5))
        session.add(subject)

def insert_grades():
    for student_id in range(1, 51):
        for _ in range(20):
            grade = Grade(
                grade=random.randint(1, 100),
                grade_date=fake.date_between(start_date='-3M'),
                student_id=student_id,
                subject_id=random.randint(1, 8)
            )
            session.add(grade)


if __name__ == '__main__':
    try:
        insert_groups()
        insert_students()
        insert_teachers()
        insert_subjects()
        insert_grades()
        session.commit()

    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()