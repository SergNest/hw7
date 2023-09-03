from database.db import session
from database.models import Group


def create_groups():
    groups_list = ['First', 'Second', 'Third']
    for gp in groups_list:
        new_group = Group(
            name=gp
        )
        session.add(new_group)
    session.commit()


if __name__ == '__main__':
    create_groups()
