#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User

import ipdb

User.drop_table()
User.create_table()

melanie = User.create("Melanie", "Wilson", "melaniemwilson1@gmail.com", "melaniewilsxn", "August29")
print(melanie)

makayla = User.create("Makayla", "Martorana", "makayla.martorana@gmail.com", "makaylamartorana", "December13")
print(makayla)

ipdb.set_trace()