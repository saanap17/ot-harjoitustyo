import sqlite3


class Users:
    """Class that manages the SQLite database containing user information."""

    def __init__(self, conn):
        """Constructor, creates a new user repository.
        Args:
            conn: address for the database file."""

        self.con = conn
        self.cur = self.con.cursor()

    def create_db(self):
        """Creates a new database if it doesn't exist."""

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Users
                        (username text, password text, experience integer, UNIQUE(username))''')
        self.con.commit()

    def add_user_sql(self, user):
        """Adds one user to the database.
        Args:
            user: User object containing the user's name and password."""

        try:
            self.cur.execute(
                '''INSERT INTO Users VALUES(?,?,?)''', (user.username, user.password, 0))
            self.con.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def check_login_sql(self, username, password):
        """Checks whether a login attempt is valid.
        Args:
            username: name of the user.
            password= password of the user.
        Returns:
            True, if the password matches the user and logging in is allowed, otherwise False."""

        psw = self.cur.execute(
            '''SELECT * FROM Users WHERE username=(?) AND password=(?)''', (username, password))
        if psw.fetchone() is None:
            return False
        return True

    def delete_user(self, username):
        """Deletes one user from the database.
        Args:
            username: name of the user."""

        self.cur.execute(
            '''DELETE FROM Users WHERE username=(?)''', (username, ))
        self.con.commit()

    def get_user(self, username):
        """Finds a specific user from the database.
        Args:
            username: name of the user.
        Returns:
            user: User object"""

        user = self.cur.execute(
            '''SELECT * FROM Users WHERE username=(?)''', (username, )).fetchone()
        return user

    def update_exp(self, username, exp):
        """Updates the experience points of a specific user.
        Args:
            username: name of the user.
            exp: new experience value."""
        self.cur.execute(
            '''UPDATE Users SET experience=(?) WHERE username=(?)''', (exp, username, ))
        self.con.commit()
