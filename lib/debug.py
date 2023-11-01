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
    Category.create("Utilities")
    Category.create("Savings")
    Category.create("Medical")
    Category.create("Insurance")
    Category.create("Personal")
    Category.create("Entertainment")
    Category.create("Miscellaneous")
    Expense.create(1, "2023-09-01", 1200.00, 1, "Monthly rent")
    Expense.create(1, "2023-09-01", 60.00, 4, "Internet")
    Expense.create(1, "2023-09-01", 97.22, 4, "Electric bill")
    Expense.create(1, "2023-09-03", 65.45, 3, "Groceries for the week")
    Expense.create(1, "2023-09-04", 30.00, 2, "Gas refill")
    Expense.create(1, "2023-09-10", 200.00, 4, "Electricity bill")
    Expense.create(1, "2023-09-15", 50.00, 5, "Savings for vacation")
    Expense.create(1, "2023-09-20", 100.00, 6, "Doctor visit")
    Expense.create(1, "2023-09-25", 150.00, 7, "Car insurance")
    Expense.create(1, "2023-09-30", 75.00, 8, "New shoes")
    Expense.create(1, "2023-10-01", 1200.00, 1, "Monthly rent")
    Expense.create(1, "2023-10-03", 70.00, 3, "Groceries for the week")
    Expense.create(1, "2023-10-10", 50.00, 4, "Water bill")
    Expense.create(1, "2023-10-15", 30.00, 2, "Gas refill")
    Expense.create(1, "2023-10-20", 200.00, 6, "Dental checkup")
    Expense.create(1, "2023-10-25", 100.00, 7, "Car maintenance")
    Expense.create(1, "2023-10-30", 80.00, 8, "New clothes")
    Expense.create(2, "2023-09-05", 800.00, 1, "Rent")
    Expense.create(2, "2023-09-10", 70.00, 3, "Weekend dining out")
    Expense.create(2, "2023-09-15", 40.00, 2, "Public transit pass")
    Expense.create(2, "2023-09-20", 25.00, 9, "Movie night")
    Expense.create(2, "2023-09-25", 100.00, 10, "Birthday gift for friend")
    Expense.create(2, "2023-10-05", 800.00, 1, "Rent")
    Expense.create(2, "2023-10-10", 60.00, 3, "Groceries")
    Expense.create(2, "2023-10-15", 40.00, 2, "Bus pass")
    Expense.create(2, "2023-10-20", 20.00, 9, "Cinema")
    Expense.create(2, "2023-10-25", 90.00, 10, "Gift for mom")
    Expense.create(2, "2023-10-30", 100.00, 5, "Savings for new phone")

reset_database()
ipdb.set_trace()