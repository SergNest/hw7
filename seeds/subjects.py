import random

from database.db import session
from database.models import Subject, Teacher


def create_subjects():
    subjects_list = ['Прикладна математика', 'Інженерія програмного забезпечення',
                     'Комп’ютерні науки та інформаційні технології' 'Комп’ютерна інженерія',
                     'Кібербезпека', 'Інформаційні системи та технології', 'Іноземна мова', 'Історія України']
    teachers = session.query(Teacher).all()

    for subject in subjects_list:
        random_teacher = random.choice(teachers)
        new_subject = Subject(
            name=subject,
            teacher_id=random_teacher.id
        )
        session.add(new_subject)
    session.commit()


if __name__ == '__main__':
    create_subjects()
