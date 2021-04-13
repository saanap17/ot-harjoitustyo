import getpass
import sys, os
from users import Users

class Interface:
    
    def __init__(self):
        self.users = Users('users.txt')
        
    def commands(self):
        print('     L = Login With an Existing User')
        print('     C = Create a User')
        print('     Q = Quit\n')
        #print('---------------------\n')
    
    def start(self):
        print('\n~ Welcome to LanguageLearningProgram! ~ \n\nCOMMANDS:')
        self.commands()
        
        while True:
            print('Type "help" to see all commands.')
            cmd = input('What would you like to do? ').lower()
            print('')
    
            if cmd == 'help':
                self.commands()
            elif cmd == 'l':
                self.login()
            elif cmd == 'c':
                self.create_user()
            elif cmd == 'q':
                print('Happy language learning!')
                sys.exit()
            else:
                print("I couldn't understand your command, please try again.")
    
    def login(self):
        print('---------------------\n')
        print('All inputs are case sensitive!')
        print('Type "back" to go back to the login screen.\n')
        
        while True:
            username = input('Username: ')
            
            if username.lower() == 'back':
                print('---------------------\n')
                break
            password = getpass.getpass(prompt='Password: ', stream=None)
            
            if self.users.check_login(username,password):
                print('\n---------------------\n')
                self.logged_in(username)
                break
            else:
                print('Username or password incorrect! \n')

    
    def create_user(self):
        print('Type "back" to go back to the login screen.\n')
        while True:
            username = input('Please enter a username: ')
            if username.lower() == 'back':
                print('---------------------\n')
                break
            password = getpass.getpass(prompt='Please enter a password: ', stream=None)
        
            if self.users.add_user(username,password):
                self.users.add_user(username,password)
                print('\nUser successfully added!\n--------------------- \n')
                break
            else:
                print('Username already in use! \n')
    
    def logged_in(self,user):
        print(f'Welcome, {user}!')
        print('L = Logout')
        cmd = input('What would you like to do? ').lower()
        print('')
        
        if cmd == 'l':
            print('---------------------\n')
            self.start()