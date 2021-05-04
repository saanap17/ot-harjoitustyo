import unittest
import pytest
import os
import sqlite3
from repositories.users import Users
from entities.user import User


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_user = User('Username', 'Password')

    @pytest.fixture(autouse=True)
    def before(self):
        self.users = Users(sqlite3.connect('test_users.db'))
        self.users.create_db()
        yield
        self.users.con.close()
        os.remove('test_users.db')

    def test_adding_users(self):
        self.assertEqual(self.users.add_user_sql(self.test_user), True)

    def test_no_duplicates(self):
        self.users.add_user_sql(self.test_user)
        self.assertEqual(self.users.add_user_sql(self.test_user), False)

    def test_allow_login(self):
        self.users.add_user_sql(self.test_user)
        self.assertEqual(self.users.check_login_sql(
            self.test_user.username, self.test_user.password), True)
        self.assertEqual(self.users.check_login_sql(
            'Username1', 'Username2'), False)

    def test_deleting_users(self):
        self.users.add_user_sql(self.test_user)
        self.users.delete_user(self.test_user.username)
        self.assertEqual(self.users.check_login_sql(
            'Username1', 'Username2'), False)

    def test_updating_exp(self):
        self.users.add_user_sql(self.test_user)
        user = self.users.get_user(self.test_user.username)
        self.assertEqual(user[2], 0)
        self.users.update_exp(self.test_user.username, 10)
        user = self.users.get_user(self.test_user.username)
        self.assertEqual(user[2], 10)
