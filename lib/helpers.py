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

        if not end_date_str:
            expenses = Expense.find_by_date(user.id, start_date)
        else:
            end_date = datetime.strptime(end_date_str, DATE_FORMAT)
            expenses = Expense.find_by_date(user.id, start_date, end_date)
        for expense in expenses:
            print(expense)
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
    
def find_expenses_by_description(user):
    description = input("Enter the description you would like to search: ")

    expenses = Expense.find_by_description(user.id, description)
    for expense in expenses:
        print(expense)

def create_expense(user):
    date = input("Enter date in the format YYYY-MM-DD: ")
    raw_amount = input("Enter amount with two decimal places: $")
    description = input("Enter the description: ")
    list_categories()
    raw_category_id = input("Enter the id number of the category: ")

    try:
        amount = float(raw_amount)
        category_id = int(raw_category_id)
        expense = Expense.create(user.id, date, amount, category_id, description)
        print(f"Success: {expense}")
    except Exception as exc:
        print("Error creating expense: ", exc)

def update_expense(user):
    id_ = input("Enter the expense's id: ")
    if expense := user.expense_by_id(id_):
        try:
            date = input("Enter date in the format YYYY-MM-DD: ")
            expense.date = date
            raw_amount = input("Enter amount with two decimal places: $")
            expense.amount = float(raw_amount)
            description = input("Enter the description: ")
            expense.description = description
            list_categories()
            raw_category_id = input("Enter the id number of the category: ")
            expense.category_id = int(raw_category_id)

            expense.update()
            print(f"Success: {expense}")
        except Exception as exc:
            print("Error updating expense: ", exc)
    else:
        print(f'Expense {id_} not found')

def delete_expense(user):
    id_ = input("Enter the expense's id: ")
    if expense := user.expense_by_id(id_):
        expense.delete()
        print(f"Expense {id_} deleted")
    else:
        print(f'Expense {id_} not found')

def find_category_by_name():
    name = input("Enter the category's name: ")
    category = Category.find_by_name(name)
    print(category) if category else print(f"Category {name} not found")

def find_category_by_id():
    id_ = input("Enter the category's id: ")
    category = Category.find_by_id(id_)
    print(category) if category else print(f"Category {id_} not found")

def create_category():
    name = input("Enter the category's name: ")
    try:
        category = Category.create(name)
        print(f"Success: {category}")
    except Exception as exc:
        print("Error creating category: ", exc)

def update_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        try:
            name = input("Enter the category's name: ")
            category.name = name

            category.update()
            print(f"Success: {category}")
        except Exception as exc:
            print("Error updating category: ", exc)
    else:
        print(f'Category {id_} not found')

def delete_category():
    id_ = input("Enter the expense's id: ")
    if category := Category.find_by_id(id_):
        category.delete()
        print(f"Category {id_} deleted")
    else:
        print(f'Category {id_} not found')
