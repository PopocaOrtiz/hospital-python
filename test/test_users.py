from unittest import TestCase

from app.users import chain_users
from app.schemas import User


class TestUsers(TestCase):

    def test_chain(self):
        users = [
            User(id=1, firstname='tom', lastname='hardy'),
            User(id=2, firstname='tom', lastname='holland')
        ]

        self.assertEqual(users, list(chain_users()))
