import sys

def display_menu():
    print("To-Do List Application")
    print("======================")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Remove To-Do Item")
    print("4. Exit")

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

def remove_todo_item():
    view_todo_list()
    item_number = int(input("Enter te=he number of the item to remove: "))
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
            remove_todo_item()
        elif choice == '4':
            print('GoodBye.')
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    print("Starting To-Do List Application")
    main()
