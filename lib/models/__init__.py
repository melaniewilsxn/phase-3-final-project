import sqlite3

CONN = sqlite3.connect('expense_tracker.db')
CURSOR = CONN.cursor()
