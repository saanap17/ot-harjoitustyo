from entities.user import User
from entities.word import Word
from entities.level import Level
from repositories.users import Users
from repositories.wordlist import Wordlist


class WordAppService:
    """Class responsible for communication between the interface and data repositories."""

    def __init__(self, users_address, words_address):
        """Constructor, creates a new service object.
        Args:
            users_address: address for the SQLite file.
            words_address: address for the CSV file."""

        self.users_repository = Users(users_address)
        self.users_repository.create_db()
        self.wordlist_repository = Wordlist(words_address)

    def add_user(self, username, password):
        """Adds one user to the database.
        Args:
            username: name of the user.
            password: password of the user."""

        user = User(username, password)
        return self.users_repository.add_user_sql(user)

    def login(self, username, password):
        """Verifies a login attempt.
        Args:
            username: name of the user.
            password: password of the user.
        Returns:
            True, if login attempt is valid."""

        return self.users_repository.check_login_sql(username, password)

    def delete_user(self, username):
        """Deletes one uesr from the database.
        Args:
            username: name of the user."""

        self.users_repository.delete_user(username)
        self.wordlist_repository.delete_words_user(username)

    def add_word(self, user, word, translation, language):
        """Creates a Word object and adds it to the CSV file.
        Args:
            user: name of the user adding the word.
            word: word string.
            translation: translation for the word.
            language: language of the translation."""

        word = Word(user, word, translation, language)
        self.wordlist_repository.add_word(word)

    def delete_word(self, user, word, language):
        """Deletes one word from the CSV file.
        Args:
            user: name of the user.
            word: word string.
            language: language string."""

        self.wordlist_repository.delete_word(user, word, language)

    def read_list(self, user, lang):
        """Returns a list of words from a user in a specific language.
        Args:
            user: name of the user.
            language: language of the words.
        Returns:
            words: list of Word objects, False if list is empty."""

        words = self.wordlist_repository.read_list(user, lang)
        if not words or lang == '':
            return False
        return words

    def get_languages(self, user):
        """Returns a dictionary with all languages available to a user.
        Args:
            user: name of the user.
        Returns:
            lang_list: list of number-language pairs, False if list is empty."""

        langs = self.wordlist_repository.get_languages(user)
        if not langs:
            return False
        order = 1
        lang_list = [[0]]*(len(langs)+1)
        lang_list = {}

        for i in range(len(langs)):
            lang_list[order] = langs[i]
            order += 1
        return lang_list

    def edit_word(self, user, old_word, old_lang, new_word, transl, new_lang):
        """Edits one word.
        Args:
            user: name of the user.
            old_word: word that is edited.
            old_lang: language of the old word.
            new_word: new word string.
            transl: new translation string.
            new_lang: new language string.
        Returns:
            False, if given strings are unvalid, otherwise True."""

        if not old_word or not new_word or not transl or not new_lang:
            return False
        self.delete_word(user, old_word, old_lang)
        self.add_word(user, new_word, transl, new_lang)
        return True

    def get_experience(self, user):
        """Returns the experience points of a specific user.
        Args:
            user: name of the user"""
        return self.users_repository.get_user(user)[2]

    def get_level(self, user):
        """Returns the level of a specific user.
        Args:
            user: name of the user"""
        experience = self.get_experience(user)
        level = Level()
        return level.check_level(int(experience))

    def update_exp(self, user, exp):
        """Updates a user's experience points.
        Args:
            user: name of the user.
            exp: new experience value."""
        new_exp = int(self.get_experience(user))
        new_exp += int(exp)
        self.users_repository.update_exp(user, new_exp)
