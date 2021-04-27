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
        self.new_word = Word('TestUser', 'TestWord',
                             'TestTranslation', 'TestLanguage')
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
        words = self.wordlist.read_list()
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0].language, 'Language')

    def test_reading_list_by_user(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.add_word(
            Word('TestUser', 'TestWord2', 'TestTranslation2', 'TestLanguage'))
        self.wordlist.add_word(
            Word('TestUser', 'TestWord3', 'TestTranslation3', 'TestLanguage2'))
        self.wordlist.add_word(Word('User2', 'Word2', 'Transl2', 'Lang2'))
        self.assertEqual(len(self.wordlist.read_list('TestUser')), 3)

    def test_reading_list_by_language(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.add_word(
            Word('TestUser', 'TestWord2', 'TestTranslation2', 'TestLanguage'))
        self.wordlist.add_word(
            Word('TestUser', 'TestWord3', 'TestTranslation3', 'TestLanguage2'))
        result = self.wordlist.read_list('TestUser', 'TestLanguage')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].language, 'TestLanguage')
        self.assertEqual(result[1].language, 'TestLanguage')

    def test_adding_words(self):
        result = False
        self.wordlist.add_word(self.new_word)
        words = self.wordlist.read_list()
        for w in words:
            if (w.word == self.new_word.word) and (
                    w.user == self.new_word.user) and (
                    w.language == self.new_word.language):
                result = True
        self.assertEqual(result, True)

    def test_dont_add_duplicates(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.add_word(self.new_word)
        self.wordlist.add_word(self.new_word)
        self.assertEqual(len(self.wordlist.read_list()), 2)

    def test_read_list_returns_words(self):
        self.wordlist.add_word(self.new_word)
        result = self.wordlist.read_list()[1].user
        self.assertEqual(result, 'TestUser')

    def test_deleting_words(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.delete_word(
            self.new_word.user, self.new_word.word, self.new_word.language)
        self.assertEqual(len(self.wordlist.read_list()), 1)
        self.assertEqual(self.wordlist.read_list()[0].user, 'User')

    def test_deleting_words_by_user(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.add_word(Word('1', '2,', '3,', '4'))
        self.wordlist.delete_words_user('TestUser')
        words = self.wordlist.read_list()
        self.assertEqual(len(words), 2)
        self.assertEqual(words[1].user, '1')

    def test_language_list_no_duplicates(self):
        self.wordlist.add_word(self.new_word)
        self.wordlist.add_word(
            Word('TestUser', 'TestWord2', 'TestTranslation2', 'TestLanguage'))
        self.wordlist.add_word(
            Word('TestUser', 'TestWord3', 'TestTranslation3', 'TestLanguage2'))
        languages = self.wordlist.get_languages('TestUser')
        self.assertEqual(len(languages), 2)
        self.assertEqual(languages, ['TestLanguage2', 'TestLanguage'])
