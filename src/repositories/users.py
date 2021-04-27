import sqlite3


class Users:
    def __init__(self, conn):
        self.con = conn
        self.cur = self.con.cursor()

    def create_db(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Users
                        (username text, password text, UNIQUE(username))''')
        self.con.commit()

    def add_user_sql(self, user):
        try:
            self.cur.execute(
                '''INSERT INTO Users VALUES(?,?)''', (user.username, user.password))
            self.con.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def check_login_sql(self, username, password):
        psw = self.cur.execute(
            '''SELECT * FROM Users WHERE username=(?) AND password=(?)''', (username, password))
        if psw.fetchone() is None:
            return False
        return True

    def delete_user(self, username):
        self.cur.execute(
            '''DELETE FROM Users WHERE username=(?)''', (username, ))
        self.con.commit()
