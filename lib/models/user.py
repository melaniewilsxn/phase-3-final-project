from models.__init__ import CURSOR, CONN

class User:
    
    def __init__(self, first_name, last_name, email, username, password, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User: {self.id}: {self.first_name} {self.last_name}>"

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
        """ Drop the table that persists Department instances """
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

        CURSOR.execute(sql, (self.first_name, self.last_name, self.email, self.username, self.password))
        CONN.commit()

        self.id = CURSOR.lastrowid

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
        CURSOR.execute(sql, (self.first_name, self.last_name, self.email, self.username, self.password, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current User instance"""
        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
