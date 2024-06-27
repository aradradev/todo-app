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
    print("7. View To-Do List by Category")
    print("8. Exit")

def view_todo_list():
    print("\nTo-Do List:")
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        for i, item in enumerate(items, 1):
            try:
                task, category = item.strip().split('|')
                print(f"{i}. [{category} ] {task}")
            except ValueError:
                print(f"Error in item: {item}")
    print()
    

def add_todo_item():
    item = input("Enter a new to-do item: ")
    category = input("Enter a category for this item: ")
    with open('todo_list.txt', 'a') as file:
        file.write(f"{item} | {category}\n")
    print("To-Do item added successfully.")

def edit_todo_item():
    view_todo_list()
    item_number = int(input("Enter the number of the item to edit: "))
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
    if 0 <item_number<= len(items):
        new_item = input("Enter the new item: ")
        new_category = inpute("Enter the new category: ")
        items[item_number - 1] = f"{new_item} | {new_category}\n"
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
                task, category = item.strip().split('|')
                print(f"{i}. [{category}], {item}")
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

def view_by_category():
    category = input("Enter the category to view: ")
    print(f"\nTo-Do List for Category: '{category}':")
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        category_items = [item.strip() for item in items if item.strip().endswith(f"|{category}")]
        if category_items:
            for i, item in enumerate(category_items, 1):
                task, category = item.split('|')
                print(f"{i}. [{category}] {task}")
        else:
            print(f"No items found for this category '{category}.")
    print()


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
            view_by_category()
        elif choice == '8':
            print('GoodBye.')
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    print("Starting To-Do List Application")
    main()
