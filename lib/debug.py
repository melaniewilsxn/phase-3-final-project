#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User
from models.category import Category

import ipdb

def reset_database():
    User.drop_table()
    User.create_table()
    Category.drop_table()
    Category.create_table()

    User.create("Melanie", "Wilson", "melaniemwilson1@gmail.com", "melaniewilsxn", "August29")
    User.create("Makayla", "Martorana", "makayla.martorana@gmail.com", "makaylamartorana", "December13")
    Category.create("Housing")
    Category.create("Transportation")
    Category.create("Food")

reset_database()
ipdb.set_trace()