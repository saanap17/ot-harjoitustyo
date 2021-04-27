import unittest
import pytest
import sqlite3
import os
from services.wordapp_service import WordAppService
from repositories.users import Users
from entities.user import User
from repositories.wordlist import Wordlist
from entities.word import Word


class TestWordAppService(unittest.TestCase):
    def setUp(self):
        self.user = 'User'
        self.pw = 'Pw'
        self.word = ['Admin', 'TestWord', 'Transl', 'Lang']

    @pytest.fixture(autouse=True)
    def create_data(self):
        self.service = WordAppService(
            (sqlite3.connect('test_users.db')), 'test_words.csv')
        self.wordlist = self.service.wordlist_repository
        self.users = self.service.users_repository
        self.users.create_db()
        yield
        self.users.con.close()
        os.remove('test_words.csv')
        os.remove('test_users.db')

    def test_adding_user(self):
        self.assertEqual(self.service.add_user(self.user, self.pw), True)

    def test_login(self):
        self.assertEqual(self.service.login(self.user, self.pw), False)
        self.service.add_user(self.user, self.pw)
        self.assertEqual(self.service.login(self.user, self.pw), True)

    def test_deleting_user(self):
        self.service.add_user(self.user, self.pw)
        self.assertEqual(self.service.login(self.user, self.pw), True)
        self.service.delete_user(self.user)
        self.assertEqual(self.service.login(self.user, self.pw), False)

    def test_reading_list_by_user_only(self):
        self.assertEqual(self.service.read_list('Admin', 'Lang'), False)
        self.service.add_word(
            self.word[0], self.word[1], self.word[2], self.word[3])
        self.service.add_word(
            self.word[0], 'Word2', self.word[2], self.word[3])
        self.service.add_word(
            'AnotherUser', self.word[1], self.word[2], self.word[3])
        self.assertEqual(len(self.service.read_list('Admin', 'Lang')), 2)

    def test_adding_word(self):
        self.service.add_word(
            self.word[0], self.word[1], self.word[2], self.word[3])
        self.assertEqual(self.service.read_list(
            'Admin', 'Lang')[0].word, 'TestWord')
        self.service.add_word(
            self.word[0], 'Word2', self.word[2], self.word[3])
        self.assertEqual(self.service.read_list(
            'Admin', 'Lang')[1].word, 'Word2')
        self.assertEqual(len(self.service.read_list('Admin', 'Lang')), 2)

    def test_deleting_word(self):
        self.service.add_word(
            self.word[0], self.word[1], self.word[2], self.word[3])
        self.assertEqual(len(self.service.read_list('Admin', 'Lang')), 1)
        self.service.delete_word(self.word[0], self.word[1], self.word[3])
        self.assertEqual(self.service.read_list('Admin', 'Lang'), False)

    def test_get_languages(self):
        self.assertEqual(self.service.get_languages('Admin'), False)
        self.service.add_word(
            self.word[0], self.word[1], self.word[2], self.word[3])
        self.assertEqual(self.service.get_languages('Admin'), True)

    def test_get_words(self):
        self.assertEqual(self.service.get_words('Admin', 'Lang'), False)
        self.service.add_word(
            self.word[0], self.word[1], self.word[2], self.word[3])
        self.assertEqual(self.service.get_words('Admin', 'Lang'), True)

    def test_edit_word(self):
        self.service.add_word(
            self.word[0], self.word[1], self.word[2], self.word[3])
        self.service.edit_word(
            self.word[0], self.word[1], self.word[3], 'NewWord', 'NewTransl', 'NewLang')
        self.assertEqual(self.service.read_list('Admin', 'Lang'), False)
        self.assertEqual(len(self.service.read_list('Admin', 'NewLang')), 1)
