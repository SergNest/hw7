import random

from database.db import session
from database.models import TeacherStudent, Teacher, Student


def create_rel():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for stud in students:
       teacher = random.choice(teachers)
       rel = TeacherStudent(teacher_id=teacher.id, student_id=stud.id)
       session.add(rel)

    session.commit()


if __name__ == '__main__':
    create_rel()
