from sqlalchemy import func, desc, select, and_
from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session

def select_01():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return f"\nselect_01\n{result}"

def select_02():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return f"\nselect_02\n{result}"

def select_03(query_discipline):
    result = session.query(Group.id.label('group_id'), Group.name,
        func.round(func.avg(Grade.grade), 2).label('average_grade'),Subject.name).select_from(Group) \
        .join(Student, Student.group_id == Group.id).join(Grade, Grade.student_id == Student.id) \
        .join(Subject, Subject.id == Grade.subject_id).filter(Subject.name == query_discipline) \
        .group_by(Group.id, Group.name, Subject.name).order_by('group_id').all()
    return f"\nselect_03\n{result}"

def select_04():
    result=session.query(func.round(func.avg(Grade.grade), 2)).select_from(Grade).all()
    return f"\nselect_04\n{result}"

def select_05(query_teacher_fullname):
    result=session.query(Subject.name, Teacher.fullname).select_from(Subject).join(Teacher) \
        .filter(Teacher.fullname==query_teacher_fullname).all()
    return f"\nselect_05\n{result}"

def select_06(query_group_name):
    result = session.query(Group.id.label("group_id"), Student.fullname).select_from(Group) \
             .join(Student).filter(Group.name==query_group_name).all()
    return f"\nselect_06\n{result}"

def select_07(query_discipline, query_group_name):
    result=session.query(Grade.grade, Student.fullname, Group.name, Subject.name) \
           .select_from(Grade).join(Student).join(Group).join(Subject) \
           .where(and_(Subject.name==query_discipline, Group.name==query_group_name)).all()
    return f"\nselect_07\n{result}"

def select_08(query_teacher_fullname):
    result=session.query(Teacher.fullname, Subject.name, func.round(func.avg(Grade.grade), 2)
           .label('average_grade')).select_from(Teacher).join(Subject).join(Grade) \
           .filter(Teacher.fullname==query_teacher_fullname).group_by(Teacher.fullname, Subject.name).all()
    return f"\nselect_08\n{result}"

def select_09(query_student_fullname):
    result=session.query(Student.fullname, Subject.name).select_from(Student).join(Grade) \
           .join(Subject).where(Student.fullname==query_student_fullname).distinct().all()
    return f"\nselect_09\n{result}"

def select_10(query_teacher_fullname, query_student_fullname):
    result=session.query(Student.fullname, Teacher.fullname, Subject.name).select_from(Student) \
           .join(Grade).join(Subject).join(Teacher) \
        .where(and_(Teacher.fullname==query_teacher_fullname, Student.fullname==query_student_fullname)) \
        .distinct().all()
    return f"\nselect_10\n{result}"

def select_11(query_teacher_fullname, query_student_fullname):
    result=session.query(func.round(func.avg(Grade.grade), 2).label('average_grade'), Teacher.fullname,
           Student.fullname).select_from(Grade).join(Subject).join(Teacher).join(Student) \
           .filter(and_(Teacher.fullname==query_teacher_fullname, Student.fullname==query_student_fullname)) \
           .group_by(Teacher.fullname, Student.fullname).all()
    return f"\nselect_11\n{result}"

def select_12(query_subject_id, query_group_id):
    subquery = (select(func.max(Grade.grade_date)).join(Student).filter(and_(
        Grade.subject_id == query_subject_id, Student.group_id == query_group_id
    ))).scalar_subquery()

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.grade_date) \
        .select_from(Grade) \
        .join(Student) \
        .filter(and_(Grade.subject_id == query_subject_id, Student.group_id == query_group_id, Grade.grade_date == subquery)).all()

    return f"\nselect_12\n{result}"

if __name__ == '__main__':
    print(select_01())
    print(select_02())
    print(select_03('Mathematics'))
    print(select_04())
    print(select_05('Кирило Ільєнко'))
    print(select_06('implement B2B bandwidth'))
    print(select_07('Mathematics', 'monetize open-source functionalities'))
    print(select_08('Кирило Мамчур'))
    print(select_09('Панас Зубко'))
    print(select_10('Антон Швайка', 'Ірена Парасюк'))
    print(select_11('Борислав Данькевич', 'Нестор Тягнибок'))
    print(select_12(2, 3))