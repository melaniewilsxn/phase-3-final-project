#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User

import ipdb

User.drop_table()
User.create_table()

ipdb.set_trace()