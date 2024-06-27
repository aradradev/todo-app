import sys

def display_menu():
    print("To-Do List Application")
    print("======================")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Edit To-Do Item")
    print("4. Mark To-Do Item as Complete")
    print("5. View Completed Item")
    print("6. Remove To-Do Item")
    print("7. Exit")

def view_todo_list():
    print("\nTo-Do List:")
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        for i, item in enumerate(items, 1):
            print(f"{i}. {item.strip()}")
    print()
    

def add_todo_item():
    item = input("Enter a new to-do item: ")
    with open('todo_list.txt', 'a') as file:
        file.write(f"{item}\n")
    print("To-Do item added successfully.")

def edit_todo_item():
    view_todo_list()
    item_number = int(input("Enter the number of the item to edit: "))
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
    if 0 <item_number<= len(items):
        new_item = input("Enter the new item: ")
        items[item_number - 1] = f"{new_item}\n"
        with open('todo_list.txt', 'w') as file:
            file.writelines(items)
        print("Item edited successfully.")
    else:
        print("Invalid item number.")

def mark_complete():
    view_todo_list()
    item_number = int(input("Enter the number of the item to mark as complete: "))
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
    if 0 < item_number <= len(items):
        completed_item = items.pop(item_number -1)
        with open('todo_list.txt', 'w') as file:
            file.writelines(items)
        with open('completed_list.txt', 'a') as file:
            file.write(f"{completed_item}")
        print("Item marked as complete.")
    else:
        print("Invalid Item number.")

def view_completed_items():
    print("\nCompleted Items:")
    with open('completed_list.txt', 'r') as file:
        completed_items = file.readlines()
        if not completed_items:
            print("No completed Items.")
        else:
            for i, item in enumerate(completed_items, 1):
                print(f"{i}. {item.strip()}")
    print()

def remove_todo_item():
    view_todo_list()
    item_number = int(input("Enter the number of the item to remove: "))
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
    if 0 < item_number <= len(items):
        del items[item_number - 1]
        with open('todo_list.txt', 'w') as file:
            file.writelines(items)
        print("Item removed successfully.")
    else:
        print("Invalid item number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_todo_item()
        elif choice == '3':
            edit_todo_item()
        elif choice == '4':
            mark_complete()
        elif choice == '5':
            view_completed_items()
        elif choice == '6':
            remove_todo_item()
        elif choice == '7':
            print('GoodBye.')
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    print("Starting To-Do List Application")
    main()
