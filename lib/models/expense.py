from models.__init__ import CURSOR, CONN
from models.user import User
from models.category import Category
from datetime import datetime

class Expense:

    all = {}
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, user_id, date, amount, category_id, description, id=None):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.amount = amount
        self.category_id = category_id
        self.description = description

    def __repr__(self):
        category_name = self.get_category_name()
        date_str = self.date.strftime(self.DATE_FORMAT)
        return (
            f"<Expense Date: {date_str}" +
            f"\nCategory: {category_name}, Amount: ${self.amount}, Description: {self.description}>"
        )
    
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if type(user_id) is int and User.find_by_id(user_id):
            self._user_id = user_id
        else:
            raise ValueError(
                "user_id must reference a user in the database")
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, datetime):
            self._date = date
        else:
            try:
                date_obj = datetime.strptime(date, self.DATE_FORMAT)
                self._date = date_obj
            except ValueError:
                try:
                    date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                    self._date = date_obj
                except ValueError:
                    raise ValueError(f"Date does not match format {self.DATE_FORMAT} or YYYY-MM-DD HH:MM:SS.")
    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, float) and (amount > 0):
            self._amount = amount
        else:
            raise ValueError("Amount must be a positive integer")
        
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError(
                "category_id must reference a category in the database")
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError("Description must be a non-empty integer")

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

    def get_category_name(self):
        category = Category.find_by_id(self.category_id)
        return category.name if category else 'Unknown Category'