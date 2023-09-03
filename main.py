from datetime import datetime

from sqlalchemy.orm import joinedload
from sqlalchemy import and_

from database.db import session
from database.models import Teacher, Student


def get_students():
    students = session.query(Student).options(joinedload(Student.teachers)).all()
    for s in students:
        print(s.first_name)
        print(f"{[f'id: {teacher.id} first_name: {teacher.first_name}' for teacher in s.teachers]}")


def get_teachers():
    teachers = session.query(Teacher).options(joinedload(Teacher.students)).all()
    for t in teachers:
        print(t.first_name)
        print(f"{[f'id: {student.id} first_name: {student.first_name}' for student in t.students]}")


def get_teachers_filter():
    teachers = session.query(Teacher).options(joinedload(Teacher.students)).filter(and_(
        Teacher.statr_work > datetime(year=2020, month=12, day=1),
        Teacher.statr_work < datetime(year=2022, month=6, day=1)
    )).all()

    for t in teachers:
        print(t.first_name)
        print(f"{[f'id: {student.id} first_name: {student.first_name}' for student in t.students]}")


if __name__ == '__main__':
     # get_students()
    # get_teachers()
    get_teachers_filter()
