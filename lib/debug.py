#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User

import ipdb

def reset_database():
    User.drop_table()
    User.create_table()

    User.create("Melanie", "Wilson", "melaniemwilson1@gmail.com", "melaniewilsxn", "August29")
    User.create("Makayla", "Martorana", "makayla.martorana@gmail.com", "makaylamartorana", "December13")

reset_database()
ipdb.set_trace()