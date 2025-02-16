from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session

def select_01():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result

def select_02():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result

def select_03():
    result = session.query(Group.id.label('group_id'), Group.name,
        func.round(func.avg(Grade.grade), 2).label('average_grade'),Subject.name).select_from(Group) \
        .join(Student, Student.group_id == Group.id).join(Grade, Grade.student_id == Student.id) \
        .join(Subject, Subject.id == Grade.subject_id).filter(Subject.name == 'Mathematics') \
        .group_by(Group.id, Group.name, Subject.name).order_by('group_id').all()
    return result

def select_04():
    result=session.query(func.round(func.avg(Grade.grade), 2)).select_from(Grade).all()
    return result

def select_05():
    result=session.query(Subject.name, Teacher.fullname).select_from(Subject).join(Teacher) \
        .filter(Teacher.fullname=='Кирило Ільєнко').all()
    return result

def select_06():
    result = session.query(Group.id.label("group_id"), Student.fullname).select_from(Group) \
             .join(Student).filter(Group.name=='implement B2B bandwidth').all()
    return result


def select_12():
    subquery = (select(func.max(Grade.grade_date)).join(Student).filter(and_(
        Grade.subject_id == 2, Student.group_id == 3
    ))).scalar_subquery()

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.grade_date) \
        .select_from(Grade) \
        .join(Student) \
        .filter(and_(Grade.subject_id == 2, Student.group_id == 3, Grade.grade_date == subquery)).all()

    return result

if __name__ == '__main__':
    # print(select_01())
    # print(select_02())
    # print(select_03())
    # print(select_04())
    # print(select_05())
    print(select_06())
    # print(select_12())