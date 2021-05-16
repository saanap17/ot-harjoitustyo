from ui.interface import Interface
from ui.commands import Commands
from services.wordapp_service import WordAppService
import sqlite3

if __name__ == "__main__":
    wordapp_service = WordAppService(
        (sqlite3.connect('data/users.db')), 'data/wordlist.csv')
    interface = Interface(wordapp_service,Commands(wordapp_service))
    interface.start()
