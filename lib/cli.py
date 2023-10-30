# lib/cli.py

from helpers import (
    exit_program,
    login,
    create_user,
    list_all_expenses,
    list_categories,
    list_expenses_by_category
)

def main_menu(current_user):
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_all_expenses(current_user)
        elif choice == "2":
            list_categories()
            category_id = input("Please enter the number corresponding to the category you would like to see expenses for: ")
            list_expenses_by_category(category_id)
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        elif choice == "10":
            pass
        elif choice == "11":
            pass
        elif choice == "12":
            pass
        elif choice == "13":
            pass
        elif choice == "14":
            pass
        elif choice == "0":
            current_user = None
            login_menu()
        else:
            print("Invalid choice")


def login_menu():
    while True:
        print("\nWelcome to the Expense Tracker App!")
        print("1. Log in")
        print("2. Create a new user")
        print("0. Exit")
        choice = input("Please enter the number corresponding to your choice: ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            user = login()
            if user:
                print(f"Welcome back, {user.first_name}!")
                main_menu(user)
                break
        elif choice == "2":
            create_user()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("Please select an option:")
    print("1. List all expenses")
    print("2. List all expenses by category")
    print("3. List all expenses by date")
    print("4: Search expense by name")
    print("5: Search expense by date")
    print("6: Create expense")
    print("7: Update expense")
    print("8: Delete expense")
    print("9. List all categories")
    print("10. Find category by name")
    print("11. Find category by id")
    print("12: Create category")
    print("13: Update category")
    print("14: Delete category")
    print("0: Logout")

if __name__ == "__main__":
    login_menu()
