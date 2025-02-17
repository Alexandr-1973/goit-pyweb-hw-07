from conf.db import session
from conf.models import Subject

def create_subject(name, teacher_id):
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    print(f"Subject '{name}' created with ID {subject.id}")

def list_subjects():
    subjects = session.query(Subject).all()
    for subject in subjects:
        print(f"ID: {subject.id}, Name: {subject.name}, Teacher ID: {subject.teacher_id}")

def update_subject(subject_id, name, teacher_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        subject.name = name
        subject.teacher_id = teacher_id
        session.commit()
        print(f"Subject ID {subject_id} updated to '{name}'")
    else:
        print("Subject not found.")

def remove_subject(subject_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        session.delete(subject)
        session.commit()
        print(f"Subject ID {subject_id} removed.")
    else:
        print("Subject not found.")
