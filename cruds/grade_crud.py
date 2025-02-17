from conf.db import session
from conf.models import Grade

def create_grade(grade, grade_date, student_id, subject_id):
    grade_record = Grade(grade=grade, grade_date=grade_date, student_id=student_id, subject_id=subject_id)
    session.add(grade_record)
    session.commit()
    print(f"Grade '{grade}' created for student ID {student_id} and subject ID {subject_id}")

def list_grades():
    grades = session.query(Grade).all()
    for grade in grades:
        print(f"ID: {grade.id}, Grade: {grade.grade}, Date: {grade.grade_date}, Student ID: {grade.student_id}, Subject ID: {grade.subject_id}")

def update_grade(grade_id, grade, grade_date, student_id, subject_id):
    grade_record = session.query(Grade).filter_by(id=grade_id).first()
    if grade_record:
        grade_record.grade = grade
        grade_record.grade_date = grade_date
        grade_record.student_id = student_id
        grade_record.subject_id = subject_id
        session.commit()
        print(f"Grade ID {grade_id} updated.")
    else:
        print("Grade not found.")

def remove_grade(grade_id):
    grade_record = session.query(Grade).filter_by(id=grade_id).first()
    if grade_record:
        session.delete(grade_record)
        session.commit()
        print(f"Grade ID {grade_id} removed.")
    else:
        print("Grade not found.")
