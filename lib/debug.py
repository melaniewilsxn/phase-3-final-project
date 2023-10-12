#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User
from models.category import Category
from models.expense import Expense

import ipdb

def reset_database():
    User.drop_table()
    User.create_table()
    Category.drop_table()
    Category.create_table()
    Expense.drop_table()
    Expense.create_table()

    User.create("Melanie", "Wilson", "melaniemwilson1@gmail.com", "melaniewilsxn", "August29")
    User.create("Makayla", "Martorana", "makayla.martorana@gmail.com", "makaylamartorana", "December13")
    Category.create("Housing")
    Category.create("Transportation")
    Category.create("Food")
    Expense.create(1, "2023-09-01", 1200.00, 1, "Monthly rent")
    Expense.create(1, "2023-09-03", 65.45, 3, "Groceries for the week")
    Expense.create(1, "2023-09-04", 30.00, 2, "Gas refill")

reset_database()
ipdb.set_trace()