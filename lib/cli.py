# lib/cli.py

from helpers import (
    exit_program,
    login,
    create_user,
    list_all_expenses,
    list_categories,
    list_expenses_by_category,
    list_expenses_by_date,
    find_expenses_by_description,
    create_expense,
    update_expense,
    delete_expense,
    find_category_by_name,
    find_category_by_id,
    create_category,
    update_category,
    delete_category
)

def main_menu(current_user):
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            expense_search_menu(current_user)
        elif choice == "2":
            expense_edit_menu(current_user)
        elif choice == "3":
            category_search_menu(current_user)
        elif choice == "4":
            category_edit_menu(current_user)
        elif choice == ("L" or "l"):
            current_user = None
            login_menu()
        else:
            print("Invalid choice")

def expense_search_menu(current_user):
    while True:
        print("------------------------------------")
        print("Type 'A' to show all expenses")
        print("Type 'C' to show expenses by category")
        print("Type 'D' to show expenses by date")
        print("Type 'S' to search expenses by the description")
        print("Type 'R' to return to the previous menu")
        print("------------------------------------")
        choice = input("Please enter your choice: ")

        if choice == ("A" or "a"):
            list_all_expenses(current_user)
        elif choice == ("C" or "c"):
            list_categories()
            category_id = input("Please enter the ID number corresponding to the category you would like to see expenses for: ")
            list_expenses_by_category(category_id)
        elif choice == ("D" or "d"):
            list_expenses_by_date(current_user)
        elif choice == ("S" or "s"):
            find_expenses_by_description(current_user)
        elif choice == ("R" or "r"):
            main_menu(current_user)
        else:
            print("Invalid choice")

def expense_edit_menu(current_user):
    while True:
        print("------------------------------------")
        print("Type 'C' to create a new expense")
        print("Type 'U' to update an expense")
        print("Type 'D' to delete an expense")
        print("Type 'R' to return to the previous menu")
        print("------------------------------------")
        choice = input("Please enter your choice: ")

        if choice == ("C" or "c"):
            create_expense(current_user)
        elif choice == ("U" or "u"):
            update_expense(current_user)
        elif choice == ("D" or "d"):
            delete_expense(current_user)
        elif choice == ("R" or "r"):
            main_menu(current_user)
        else:
            print("Invalid choice")

def category_search_menu(current_user):
    while True:
        print("------------------------------------")
        print("Type 'A' to show all categories")
        print("Type 'S' to search categories by name")
        print("Type 'I' to search categories by id")
        print("Type 'R' to return to the previous menu")
        print("------------------------------------")
        choice = input("Please enter your choice: ")

        if choice == ("A" or "a"):
            list_categories()
        elif choice == ("S" or "s"):
            find_category_by_name()
        elif choice == ("I" or "i"):
            find_category_by_id()
        elif choice == ("R" or "r"):
            main_menu(current_user)
        else:
            print("Invalid choice")

def category_edit_menu(current_user):
    while True:
        print("------------------------------------")
        print("Type 'C' to create a new category")
        print("Type 'U' to update a category")
        print("Type 'D' to delete a category")
        print("Type 'R' to return to the previous menu")
        print("------------------------------------")
        choice = input("Please enter your choice: ")

        if choice == ("C" or "c"):
            create_category()
        elif choice == ("U" or "u"):
            update_category()
        elif choice == ("D" or "d"):
            delete_category()
        elif choice == ("R" or "r"):
            main_menu(current_user)
        else:
            print("Invalid choice")

def login_menu():
    while True:
        print("------------------------------------")
        print("Welcome to the Expense Tracker App!")
        print("Type 'L' to log in")
        print("Type 'N' to create a new user")
        print("Type 'E' to exit the program")
        print("------------------------------------")
        choice = input("Please enter your choice: ")
        
        if choice == ("E" or "e"):
            exit_program()
        elif choice == ("L" or "l"):
            user = login()
            if user:
                print(f"Welcome back, {user.first_name}!")
                main_menu(user)
                break
        elif choice == ("N" or "n"):
            create_user()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("------------------------------------")
    print("Please select an option:")
    print("1. Show expenses")
    print("2. Edit Expenses")
    print("3. Show categories")
    print("4: Edit categories")
    print("Type 'L' to logout")
    print("------------------------------------")

if __name__ == "__main__":
    login_menu()
