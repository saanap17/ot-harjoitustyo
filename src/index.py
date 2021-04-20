from interface import Interface
from repositories.users import Users
from repositories.wordlist import Wordlist
import sqlite3

if __name__ == "__main__":
    users = Users(sqlite3.connect('data/users.db'))
    users.create_db()
    wordlist = Wordlist('data/wordlist.csv')
    interface = Interface(users, wordlist)
    interface.start()
