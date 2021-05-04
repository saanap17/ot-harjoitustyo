class Commands:
    """Class that manages the execution of input commands."""

    def __init__(self, wordappservice):
        self.wordapp_service = wordappservice

    def print_words(self, words, lang):
        print(f'\n     Your words in {lang.capitalize()}:')
        for word in words:
            print(f'        - {word.word}, {word.translation}')

    def language_access(self, langs):
        if not langs:
            print('You are yet to add any words!')
            return False

        print('     Your languages:')
        for i in range(1, len(langs)+1):
            print(f'     ({i}) {langs[i].capitalize()}')
        print('')
        print('Type "back" to return.')

        while True:
            lang = input(
                'Which language list would you like to access (no.)? ').lower()
            if lang == 'back':
                return False
            try:
                if int(lang) > len(langs):
                    print('Please type a number from the list.')
                    continue
            except ValueError:
                print('Please type a number.')
                continue
            return langs[int(lang)]

    def add_word(self, user, langs):
        language = input('     Choose language: ').lower()
        language = self.language_access(langs)
        word = input('     Word: ').lower()
        translation = input('     Translation: ').lower()
        self.wordapp_service.add_word(user, word, translation, language)

    def delete_word(self, user, langs):
        language = self.language_access(langs)
        self.print_words(self.wordapp_service.read_list(
            user, language), language)
        word = input('\nWhich word would you like to delete? ').lower()
        self.wordapp_service.delete_word(user, word, language)

    def edit_word(self, user, langs):
        old_lang = self.language_access(langs)
        self.print_words(self.wordapp_service.read_list(
            user, old_lang), old_lang)

        old_word = input('\nWhich word would you like to edit? ').lower()
        new_word = input('\n     New word: ').lower()
        new_transl = input('     New translation: ').lower()
        new_lang = input('     New language: ').lower()

        if not self.wordapp_service.edit_word(user, old_word, old_lang, new_word, new_transl, new_lang):
            return False
        else:
            return True

    def delete_user(self, user):
        conf = input(
            'Are you sure you want to delete this user ("YES" to confirm)? ').lower()
        if conf == 'yes':
            self.wordapp_service.delete_user(user)
            return True
        return False
