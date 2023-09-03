import random

from faker import Faker
from database.db import session
from database.models import Subject, Student, Grade

fake = Faker()


def create_grades():

    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for _ in range(1, 50):
        new_grade = Grade(
            value=random.randint(1, 5),
            date=fake.date_between(start_date='-1y'),
            student_id=random.choice(students).id,
            subject_id=random.choice(subjects).id
        )
        session.add(new_grade)
    session.commit()


if __name__ == '__main__':
    create_grades()
