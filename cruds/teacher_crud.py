from conf.db import session
from conf.models import Teacher

def create_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' created with ID {teacher.id}")

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.fullname}")

def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        teacher.fullname = name
        session.commit()
        print(f"Teacher ID {teacher_id} updated to '{name}'")
    else:
        print("Teacher not found.")

def remove_teacher(teacher_id):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher ID {teacher_id} removed.")
    else:
        print("Teacher not found.")
