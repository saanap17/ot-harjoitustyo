import unittest
import os
from users import Users
from interface import Interface

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.users = Users('test_users.txt')
        self.username = 'Username'
        self.password = 'Password'

    def test_adding_users(self):
        self.assertEqual(self.users.add_user(self.username,self.password),True)
        os.remove('test_users.txt')

    def test_no_duplicates(self):
        self.users.add_user(self.username,self.password)
        self.assertEqual(self.users.add_user(self.username,self.password),False)
        os.remove('test_users.txt')

    def test_checking_users(self):
        self.users.add_user(self.username,self.password)
        self.assertEqual(self.users.check_user(self.username),True)
        os.remove('test_users.txt')

    def test_allow_login(self):
        self.users.add_user(self.username,self.password)
        self.users.check_login(self.username,self.password)
        self.assertEqual(self.users.check_user(self.username),True)
        os.remove('test_users.txt')

    def test_dont_allow_login(self):
        self.assertEqual(self.users.check_user(self.username),False)
    
