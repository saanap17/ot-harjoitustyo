import getpass
import sys
import sqlite3
from repositories.users import Users
from repositories.wordlist import Wordlist
from entities.user import User
from entities.word import Word


class Interface:
    def __init__(self, users, wordlist):
        self.users = users
        self.wordlist = wordlist
        self.line = '-'*40 + '\n'
        self.help_msg = 'Type "help" to see all commands.'
        self.to_do = 'What would you like to do? '

    def commands(self, code):
        if code == 1:
            return 'COMMANDS:\n     L = Login With an Existing User\n     C = Create a User\n     Q = Quit\n'
        elif code == 2:
            return '     L = Logout\n     M = Manage Word Lists\n     P = Play\n'
        elif code == 3:
            return '     A = Add Words\n     D = Delete Words\n'

    def start(self):
        print(
            f'\n~ Welcome to LanguageLearningProgram! ~ \n\n{self.commands(1)}')
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
        print('Type "back" to go back to the login screen.\n')

        while True:
            username = input('     Username: ')

            if username.lower() == 'back':
                print(self.line)
                break
            password = getpass.getpass(prompt='     Password: ', stream=None)

            if self.users.check_login_sql(username, password):
                print(f'\n{self.line}')
                self.logged_in(username)
                break
            print('     Username or password incorrect! \n')

    def create_user(self):
        print(self.line)
        print('     CREATE USER\n\nType "back" to go back to the login screen.\n')
        while True:
            username = input('     Please enter a username: ')
            if username.lower() == 'back':
                print(self.line)
                break
            password = getpass.getpass(
                prompt='     Please enter a password: ', stream=None)

            if self.users.add_user_sql(User(username, password)):
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
                print('Playing has not been implemented yet.\n')
            else:
                print(
                    f"I couldn't understand your command, please try again.\n({self.help_msg})\n")

    def manage(self, user):
        print(self.line)
        print(
            f'     MANAGE WORD LISTS\n\nType "back" to go back to the login screen.\n\n{self.commands(3)}')

        while True:
            cmd = input(f'{self.to_do}').lower()
            print('')

            if cmd == 'back':
                print(self.line)
                break
            elif cmd == 'help':
                print(self.commands(3))
            elif cmd == 'a':
                word = input('\n     Word: ').lower()
                translation = input('     Translation: ').lower()
                self.wordlist.add_word(Word(user, word, translation))
                print('')
            elif cmd == 'd':
                word = input(
                    '     Which word would you like to delete? ').lower()
                self.wordlist.delete_word(user, word)
                print('')
            else:
                print(
                    f"I couldn't understand your command, please try again.\n({self.help_msg})\n")

    def play(self, user):
        return
