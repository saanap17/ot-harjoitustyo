import unittest
import pytest
import os
import sqlite3
from repositories.users import Users
from entities.user import User
from repositories.wordlist import Wordlist
from entities.word import Word


class TestWordlist(unittest.TestCase):
    def setUp(self):
        self.new_word = Word('TestUser', 'TestWord', 'TestTranslation')
        self.address = 'test_words.csv'

    @pytest.fixture(autouse=True)
    def before(self):
        self.wordlist = Wordlist('test_words.csv')
        self.wordlist.create_list()
        yield
        os.remove('test_words.csv')

    def test_creates_list_if_not_exist(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.create_list()
        self.wordlist.create_list()
        self.assertEqual(len(self.wordlist.read_list()), 2)

    def test_reading_list(self):
        result = len(self.wordlist.read_list())
        self.assertEqual(result, 1)

    def test_reading_list_by_user(self):
        self.wordlist.add_word(self.new_word)
        second_word = Word('User2', 'Word2', 'Transl2')
        self.wordlist.add_word(second_word)
        self.assertEqual(len(self.wordlist.read_list_user('TestUser')), 1)

    def test_adding_words(self):
        result = False
        self.wordlist.add_word(self.new_word)
        words = self.wordlist.read_list()
        for w in words:
            if w.word == self.new_word.word and w.user == self.new_word.user:
                result = True
        self.assertEqual(result, True)

    def test_read_list_returns_words(self):
        self.wordlist.add_word(self.new_word)
        result = self.wordlist.read_list()[1].user
        self.assertEqual(result, 'TestUser')

    def test_deleting_words(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.delete_word(self.new_word.user, self.new_word.word)
        self.assertEqual(len(self.wordlist.read_list()), 1)
