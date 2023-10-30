# lib/helpers.py
from models.user import User
from models.expense import Expense
from models.category import Category
import bcrypt
from getpass import getpass

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