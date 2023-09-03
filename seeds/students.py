import random

from faker import Faker

from database.db import session
from database.models import Student, Group

fake = Faker('uk_UA')


def create_students():
    for _ in range(1, 15):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        session.add(student)
    session.commit()


def fill_students():
    students = session.query(Student).all()
    groups = session.query(Group).all()
    for sd in students:
        random_group = random.choice(groups)
        sd.group = random_group
    session.commit()


if __name__ == '__main__':
    fill_students()
