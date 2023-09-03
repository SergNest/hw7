from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from database.db import session
from database.models import Student, Grade, Subject, Teacher, Group


def select_1():

    top_students = (
        session.query(Student)
        .join(Grade)
        .group_by(Student)
        .order_by(func.avg(Grade.value).desc())
        .limit(5)
        .all()
    )
    return top_students


def select_2(subject_name):

    top_student = (
        session.query(Student)
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Student)
        .order_by(func.avg(Grade.value).desc())
        .first()
    )
    return top_student


def select_3(subject_name):

    avg_grades_by_group = (
        session.query(Group.name, func.avg(Grade.value).label('average_grade'))
        .join(Student)
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Group)
        .all()
    )
    return avg_grades_by_group


def select_4(group_name):

    average_grade_overall = (
        session.query(func.avg(Grade.value).label('average_grade'))
        .scalar()
    )
    return average_grade_overall


def select_5(teacher_name):

    teacher_courses = (
        session.query(Subject.name)
        .join(Teacher)
        .filter(Teacher.first_name == teacher_name)
        .all()
    )
    return [course[0] for course in teacher_courses]


def select_6(group_name):

    students_in_group = (
        session.query(Student)
        .join(Group)
        .filter(Group.name == group_name)
        .all()
    )
    return students_in_group


def select_7(group_name, subject_name):

    grades_in_group_subject = (
        session.query(Student, Grade)
        .join(Group)
        .join(Grade)
        .join(Subject)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )
    return grades_in_group_subject


def select_8(teacher_name):

    average_teacher_grades = (
        session.query(func.avg(Grade.value).label('average_grade'))
        .join(Subject)
        .join(Teacher)
        .filter(Teacher.first_name == teacher_name)
        .scalar()
    )
    return average_teacher_grades


def select_9(student_name):

    student_courses = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .filter(Student.first_name == student_name)
        .distinct()
        .all()
    )
    return [course[0] for course in student_courses]


def select_10(student_name, teacher_name):

    student_teacher_courses = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .join(Subject.teacher)
        .filter(Student.first_name == student_name, Subject.teacher.has(Teacher.first_name == teacher_name))
        .distinct()
        .all()
    )
    return [course[0] for course in student_teacher_courses]


if __name__ == '__main__':

    # result = select_1()
    # print(result)
    for student in select_1():
        print(f"Student ID: {student.id}")
        print(f"Student First Name: {student.first_name}")
        print(f"Student Last Name: {student.last_name}")
        print(f"Student Email: {student.email}")
        print("\n")
