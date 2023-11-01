# lib/helpers.py
from models.user import User
from models.expense import Expense
from models.category import Category
import bcrypt
from getpass import getpass
from datetime import datetime

def exit_program():
    print("Goodbye!")
    exit()

def login():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    user = User.find_by_username(username)
    
    if user is None:
        print("Invalid username. Please try again.")
    else:
        if bcrypt.checkpw(password.encode('utf-8'), user.password):
                print("Login successful!")
                return user
        else:
            print("Invalid password. Please try again.")
            return None

def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    try:
        user = User.create(first_name, last_name, email, username, password)
        print(f'Success: {user}')
    except Exception as exc:
        print("Error creating new user: ", exc)

def list_all_expenses(user):
    expenses = user.expenses()
    for expense in expenses:
        print(expense)

def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(category)

def list_expenses_by_category(category_id):
    category = Category.find_by_id(category_id)
    expenses = category.expenses()
    for expense in expenses:
        print(expense)

def list_expenses_by_date(user):
    DATE_FORMAT = "%Y-%m-%d"

    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD) or press enter to view expenses for a single date: ")

    try:
        start_date = datetime.strptime(start_date_str, DATE_FORMAT)
        print(start_date)

        if not end_date_str:
            expenses = Expense.find_by_date(user.id, start_date)
        else:
            end_date = datetime.strptime(end_date_str, DATE_FORMAT)
            expenses = Expense.find_by_date(user.id, start_date, end_date)
        for expense in expenses:
            print(expense)
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")