from models.__init__ import CURSOR, CONN
from models.user import User
from models.category import Category

class Expense:

    all = {}

    def __init__(self, user_id, date, amount, category_id, description, id=None):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.amount = amount
        self.category_id = category_id
        self.description = description

    def __repr__(self):
        return (
            f"<Expense {self.id}: {self.date}, ${self.amount}, {self.description}; " +
            f"User ID: {self.user_id}; " +
            f"Category ID: {self.category_id}>"
        )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Expense instances """
        sql = """
            CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            date DATE,
            amount FLOAT,
            category_id INTEGER,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Expense instances """
        sql = """
            DROP TABLE IF EXISTS expenses;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the user id, date, amount, category id and description values of the current Expense object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO expenses (user_id, date, amount, category_id, description)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.user_id, self.date, self.amount, self.category_id, self.description))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        """Update the table row corresponding to the current Expense object."""
        sql = """
            UPDATE expenses
            SET user_id = ?, date = ?, amount = ?, category_id = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.user_id, self.date, self.amount, self.category_id, self.description, self.id))
        CONN.commit()

    @classmethod
    def create(cls, user_id, date, amount, category_id, description):
        """ Initialize a new Expense object and save the object to the database """
        expense = cls(user_id, date, amount, category_id, description)
        expense.save()
        return expense
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Expense object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        expense = cls.all.get(row[0])
        if expense:
            # ensure attributes match row values in case local instance was modified
            expense.user_id = row[1]
            expense.date = row[2]
            expense.amount = row[3]
            expense.category_id = row[4]
            expense.description = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            expense = cls(row[1], row[2], row[3], row[4], row[5])
            expense.id = row[0]
            cls.all[expense.id] = expense
        return expense

    @classmethod
    def get_all(cls):
        """Return a list containing one Expense object per table row"""
        sql = """
            SELECT *
            FROM expenses
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Expense object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM expenses
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None