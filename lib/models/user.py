from models.__init__ import CURSOR, CONN

class User:

    all = {}
    
    def __init__(self, first_name, last_name, email, username, password, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.id}: {self.first_name} {self.last_name}>"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of User instances """
        sql = """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            username TEXT,
            password TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists User instances """
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the first name, last name, email, username and password values of the current User instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO users (first_name, last_name, email, username, password)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.email, self.username, self.password,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name, email, username, password):
        """ Initialize a new User instance and save the object to the database """
        user = cls(first_name, last_name, email, username, password)
        user.save()
        return user

    def update(self):
        """Update the table row corresponding to the current User instance."""
        sql = """
            UPDATE users
            SET first_name = ?, last_name = ?, email = ?, username = ?, password = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.email, self.username, self.password, self.id,))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current User instance, delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        """Return a User object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        user = cls.all.get(row[0])
        if user:
            # ensure attributes match row values in case local object was modified
            user.first_name = row[1]
            user.last_name = row[2]
            user.email = row[3]
            user.username = row[4]
            user.password = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            user = cls(row[1], row[2], row[3], row[4], row[5])
            user.id = cls(row[0])
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        """Return a list containing a User object per row in the table"""
        sql = """
            SELECT *
            FROM users
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, first_name, last_name):
        """Return a User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM users
            WHERE first_name = ? AND last_name = ?
        """
        row = CURSOR.execute(sql, (first_name, last_name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_email(cls, email):
        """Return a User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM users
            WHERE email = ?
        """
        row = CURSOR.execute(sql, (email,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_username(cls, username):
        """Return a User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM users
            WHERE username = ?
        """
        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def expenses(self):
        """Return list of expenses associated with current user"""
        from models.expense import Expense
        sql = """
            SELECT * FROM expenses
            WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Expense.instance_from_db(row) for row in rows
        ]