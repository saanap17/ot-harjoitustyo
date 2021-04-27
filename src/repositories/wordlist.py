import csv
import os.path
from entities.word import Word


class Wordlist:
    def __init__(self, address):
        self.address = address
        self.create_list()

    def create_list(self):
        if os.path.exists(self.address):
            return
        with open(self.address, 'w', newline='') as new_file:
            writer = csv.writer(new_file, delimiter=',')
            writer.writerow(['User', 'Word', 'Translation', 'Language'])

    def get_languages(self, user):
        words = self.read_list(user)
        added = []
        for word in reversed(words):
            if word.language in added:
                words.remove(word)
            else:
                added.append(word.language)
        return added

    def read_list(self, username=False, language=False):
        words = []
        with open(self.address) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(',')
                user = parts[0]
                word = parts[1]
                transl = parts[2]
                lang = parts[3]
                if (not username) and (not language):
                    words.append(Word(user, word, transl, lang))
                elif username and (not language):
                    if user == username:
                        words.append(Word(user, word, transl, lang))
                elif username and language:
                    if user == username and lang == language:
                        words.append(Word(user, word, transl, lang))
        return words

    def add_word(self, word):
        words = self.read_list()
        for entry in words:
            if (
                    entry.user == word.user) and (
                    entry.word == word.word) and (
                    entry.language == word.language):
                return

        with open(self.address, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [word.user, word.word, word.translation, word.language])

    def delete_word(self, delete_user, delete_word, delete_language):
        words = self.read_list()
        with open(self.address, 'w') as file:
            for word in words:
                if (
                        word.user == delete_user) and (
                        word.word == delete_word) and (
                        word.language == delete_language):
                    continue
                file.write(
                    f'{word.user},{word.word},{word.translation},{word.language}\n')

    def delete_words_user(self, user):
        words = self.read_list()
        with open(self.address, 'w') as file:
            for word in words:
                if word.user == user:
                    continue
                file.write(
                    f'{word.user},{word.word},{word.translation},{word.language}\n')
