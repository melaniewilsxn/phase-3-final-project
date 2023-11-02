from models.__init__ import CURSOR, CONN

class Category:

    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Category name must be a non-empty string")
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Category instances """
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Category instances """
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the name values of the current Category instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO categories (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Category instance and save the object to the database """
        category = cls(name)
        category.save()
        return category

    def update(self):
        """Update the table row corresponding to the current Category instance."""
        sql = """
            UPDATE categories
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Category instance, delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM categories
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Category object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        category = cls.all.get(row[0])
        if category:
            # ensure attributes match row values in case local object was modified
            category.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            category = cls(row[1])
            category.id = row[0]
            cls.all[category.id] = category
        return category

    @classmethod
    def get_all(cls):
        """Return a list containing a Category object per row in the table"""
        sql = """
            SELECT *
            FROM categories
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Category object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM categories
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Category object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM categories
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def expenses(self):
        """Return list of expenses associated with current category"""
        from models.expense import Expense
        sql = """
            SELECT * FROM expenses
            WHERE category_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Expense.instance_from_db(row) for row in rows
        ]