from itertools import chain

from app.schemas import User


def chain_users():
    one_group = [User(id=1, firstname='tom', lastname='hardy')]
    other_group = [User(id=2, firstname='tom', lastname='holland')]

    return chain(one_group, other_group)
