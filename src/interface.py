import getpass
import sys
import sqlite3
from services.wordapp_service import WordAppService


class Interface:
    def __init__(self, wordapp_service):
        self.wordapp_service = wordapp_service
        self.line = '-'*40 + '\n'
        self.help_msg = 'Type "help" to see all commands.'
        self.to_do = 'What would you like to do? '

    def commands(self, code):
        str = ''
        if code == 1:
            return 'COMMANDS:\n     L = Login With an Existing User\n     C = Create a User\n     Q = Quit\n'
        elif code == 2:
            return '     L = Logout\n     M = Manage Word Lists\n     P = Play\n     D = Delete User\n'
        elif code == 3:
            str = '     A = Add Words\n     D = Delete Words\n     E = Edit Words\n'
        return str + '     B = Return to the Previous Page\n'

    def start(self):
        print(
            f'~ Welcome to LanguageLearningProgram! ~ \n\n{self.commands(1)}')
        while True:
            cmd = input(f'{self.to_do}').lower()
            print('')
            if cmd == 'help':
                print(self.commands(1))
            elif cmd == 'l':
                self.login()
            elif cmd == 'c':
                self.create_user()
            elif cmd == 'q':
                print('Happy language learning!')
                sys.exit()
            else:
                print(
                    f"I couldn't understand your command, please try again.\n({self.help_msg})\n")

    def login(self):
        print(self.line)
        print('     LOGIN SCREEN\n\nAll inputs are case sensitive!')
        print('Type "B" to go back to the login screen.\n')
        while True:
            username = input('     Username: ')
            if username.lower() == 'b':
                print(self.line)
                break
            password = getpass.getpass(prompt='     Password: ', stream=None)
            if self.wordapp_service.login(username, password):
                print(f'\n{self.line}')
                self.logged_in(username)
                break
            print('     Username or password incorrect! \n')

    def create_user(self):
        print(self.line)
        print('     CREATE USER\n\nType "B" to go back to the login screen.\n')
        while True:
            username = input('     Please enter a username: ')
            if username.lower() == 'b':
                print(self.line)
                break
            password = getpass.getpass(
                prompt='     Please enter a password: ', stream=None)
            if self.wordapp_service.add_user(username, password):
                print(f'\nUser successfully added!\n{self.line} \n')
                break
            print('     Username already in use! \n')

    def logged_in(self, user):
        print(f'Welcome, {user}!\n\n{self.commands(2)}')
        while True:
            cmd = input(f'{self.to_do} ').lower()
            print('')

            if cmd == 'help':
                print(self.commands(2))
            elif cmd == 'l':
                print(self.line)
                self.start()
            elif cmd == 'm':
                self.manage(user)
            elif cmd == 'p':
                self.play_setup(user)
            elif cmd == 'd':
                conf = input(
                    'Are you sure you want to delete this user (Y/N)? ').lower()
                if conf == 'y':
                    self.wordapp_service.delete_user(user)
                    print(f'User has been deleted!\n{self.line}')
                    return
                else:
                    print('User was not deleted.\n')
            else:
                print(
                    f"I couldn't understand your command, please try again.\n({self.help_msg})\n")
                continue

    def manage(self, user):
        print(self.line)
        print(f'     MANAGE WORD LISTS\n\n{self.commands(3)}')

        while True:
            cmd = input(f'{self.to_do}').lower()
            print('')

            if cmd == 'b':
                print(self.line)
                break
            elif cmd == 'help':
                print(self.commands(3))
            elif cmd == 'a':
                language = input('     Choose language: ').lower()
                word = input('     Word: ').lower()
                translation = input('     Translation: ').lower()
                self.wordapp_service.add_word(
                    user, word, translation, language)
                print(self.line)
            elif cmd == 'd':
                self.wordapp_service.get_languages(user)
                language = input(
                    '\nWhich language list would you like to access? ').lower()
                self.wordapp_service.get_words(user, language)
                word = input('\nWhich word would you like to delete? ').lower()
                self.wordapp_service.delete_word(user, word, language)
                print('     Word deleted!\n')
            elif cmd == 'e':
                self.wordapp_service.get_languages(user)
                old_lang = input(
                    '\nWhich language list would you like to access? ').lower()
                if not self.wordapp_service.get_words(user, old_lang):
                    print("You do not have any words in that language. :(\n")
                    continue
                old_word = input(
                    '\nWhich word would you like to edit? ').lower()
                new_word = input('\n     New word: ').lower()
                new_transl = input('     New translation: ').lower()
                new_lang = input('     New language: ').lower()
                if not self.wordapp_service.edit_word(user, old_word, old_lang, new_word, new_transl, new_lang):
                    print('\nWord could not be edited, please try again.\n')
                else:
                    print('\nWord successfully edited!\n')
            else:
                print(
                    f"I couldn't understand your command, please try again.\n({self.help_msg})\n")

    def play_setup(self, user):
        print(f'{self.line}\n     WORD GAME\n')

        if not self.wordapp_service.get_languages(user):
            print(f'You are yet to add any words!\n\n{self.line}')
            return
        print('')
        while True:
            lang = input(
                'Please choose language you wish to practice: ').lower()
            if lang == 'back':
                print(self.line)
                return
            words = self.wordapp_service.read_list(user, lang)
            if not words:
                print("You do not have any words in that language. :(\n")
                continue
            break
        result = self.playing_game(words, lang)
        if result == 0:
            print(
                f'You got 0 words right... Better luck next time!\n{self.line}')
        else:
            print(
                f'Congratulations! You got {result} out of {len(words)} words right!\n{self.line}')

    def playing_game(self, words, lang):
        print(f'\n{self.line}\n~ Now playing in {lang.capitalize()}! ~\n(type "stop" if you wish to stop playing)\n')
        correct = 0
        for w in words:
            counter = 0
            while True:
                answer = input(f'What is the translation for "{w.word}"? ')
                if answer == w.translation:
                    print('     Correct!\n')
                    correct += 1
                    break
                elif answer == 'stop':
                    print(self.line)
                    return
                elif counter == 3:
                    print(f'The word was "{w.translation}".\n')
                    break
                else:
                    counter += 1
                    print('     Wrong!\n')
                if counter >= 2:
                    hint = ' _'*(len(w.translation)-1)
                    print(f'     Hint: {w.translation[0]}{hint}\n')
        return correct
