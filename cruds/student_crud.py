from conf.db import session
from conf.models import Student

def create_student(fullname, group_id):
    student = Student(fullname=fullname, group_id=group_id)
    session.add(student)
    session.commit()
    print(f"Student '{fullname}' created with ID {student.id}")

def list_students():
    students = session.query(Student).all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.fullname}, Group ID: {student.group_id}")

def update_student(student_id, fullname, group_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.fullname = fullname
        student.group_id = group_id
        session.commit()
        print(f"Student ID {student_id} updated to '{fullname}'")
    else:
        print("Student not found.")

def remove_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student ID {student_id} removed.")
    else:
        print("Student not found.")

