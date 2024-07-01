from app.user import register, login
from app.todo import (view_todo_list, add_todo_item, 
                      edit_todo_item, mark_complete, view_completed_items,
                      view_by_category, remove_todo_item, set_reminder,
                      load_json, save_to_json, sort_todo_list, search_todo_items)
from app.utils import display_menu

def main():
    while True:
        print("*************")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("*************")
        choice = input("Enter you choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    display_menu()
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        view_todo_list(username)
                    elif choice == '2':
                        add_todo_item(username)
                    elif choice == '3':
                        edit_todo_item(username)
                    elif choice == '4':
                        mark_complete(username)
                    elif choice == '5':
                        view_completed_items(username)
                    elif choice == '6':
                        remove_todo_item(username)
                    elif choice == '7':
                        view_by_category(username)
                    elif choice == '8':
                        search_todo_items(username)
                    elif choice == '9':
                        sort_todo_list(username)
                    elif choice == '10':
                        set_reminder(username)
                    elif choice == '11':
                        save_to_json(username)
                    elif choice == '12':
                        load_json(username)
                    elif choice == '13':
                        print('GoodBye.')
                        break
                    else:
                        print("Invalid choice. Please try again.\n")
        elif choice == '3':
            print("GoodBye.")
            break
        else:
            print("Invalid choice. Please try again.\n")