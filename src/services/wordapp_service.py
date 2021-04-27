from entities.user import User
from entities.word import Word
from repositories.users import Users
from repositories.wordlist import Wordlist

class WordAppService:

    def __init__(self, users_address, words_address):
        self.users_repository = Users(users_address)
        self.users_repository.create_db()
        self.wordlist_repository = Wordlist(words_address)

    def add_user(self, username, password):
        user = User(username, password)
        return self.users_repository.add_user_sql(user)

    def login(self, username, password):
        return self.users_repository.check_login_sql(username, password)

    def delete_user(self, username):
        self.users_repository.delete_user(username)
        self.wordlist_repository.delete_words_user(username)

    def add_word(self, user, word, translation, language):
        word = Word(user, word, translation, language)
        self.wordlist_repository.add_word(word)

    def delete_word(self, user, word, language):
        self.wordlist_repository.delete_word(user, word, language)

    def read_list(self, user, lang):
        words = self.wordlist_repository.read_list(user, lang)
        if not words or lang == '':
            return False
        return words

    def get_languages(self, user):
        langs = self.wordlist_repository.get_languages(user)
        if not langs:
            return False
        print('     Your languages: ')
        for lang in langs:
            print(f'        - {lang.capitalize()}')
        return True

    def get_words(self, user, language):
        words = self.read_list(user, language)
        if not words:
            return False
        print(f'\n     Your words in {language.capitalize()}:')
        for word in words:
            print(f'        - {word.word}, {word.translation}')
        return True

    def edit_word(self, user, old_word, old_lang, new_word, transl, new_lang):
        self.delete_word(user, old_word, old_lang)
        self.add_word(user, new_word, transl, new_lang)
