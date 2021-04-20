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
            writer.writerow(['User', 'Word', 'Translation'])

    def read_list_user(self, user):
        words = self.read_list()
        for i in range(len(words)-1):
            if words[i].user != user:
                words.pop(i)
        return words

    def read_list(self):
        words = []
        with open(self.address) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(',')
                user = parts[0]
                word = parts[1]
                transl = parts[2]
                words.append(Word(user, word, transl))
        return words

    def add_word(self, word):
        with open(self.address, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([word.user, word.word, word.translation])

    def delete_word(self, delete_user, delete_word):
        words = self.read_list()
        with open(self.address, 'w') as file:
            for word in words:
                if word.user == delete_user:
                    if word.word == delete_word:
                        continue
                file.write(f'{word.user},{word.word},{word.translation}\n')
