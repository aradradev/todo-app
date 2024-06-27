def display_menu():
    print("======================")
    print("To-Do List Application")
    print("======================")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Edit To-Do Item")
    print("4. Mark To-Do Item as Complete")
    print("5. View Completed Item")
    print("6. Remove To-Do Item")
    print("7. View To-Do List by Category")
    print("8. Search To-Do Items by keyword")
    print("9. Exit")

def view_todo_list():
    print("\nTo-Do List:")
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        if not items:
            print("No items found.")
        else:
            for i, item in enumerate(items, 1):
                try:
                    task, category, deadline = item.strip().split('|')
                    print(f"{i}. [{category} ] {task} - Due by {deadline}")
                except ValueError:
                    print(f"Error in item: {item}")
    print()
    

def add_todo_item():
    item = input("Enter a new to-do item: ").strip().lower()
    category = input("Enter a category for this item: ").strip().lower()
    deadline = input("Enter a deadline for this item (YYYY-MM-DD): ")
    with open('todo_list.txt', 'a') as file:
        file.write(f"{item} | {category} | {deadline}\n")
    print("To-Do item added successfully.")

def edit_todo_item():
    view_todo_list()
    item_number = int(input("Enter the number of the item to edit: "))
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
    if 0 <item_number<= len(items):
        new_item = input("Enter the new item: ")
        new_category = input("Enter the new category: ")
        new_deadline = input("Enter the new deadline: ")
        items[item_number - 1] = f"{new_item} | {new_category} | {new_deadline}\n"
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
                try:
                    task, category, deadline = item.strip().split('|')
                    print(f"{i}. [{category}], {task} - Due by {deadline}")
                except ValueError:
                    print(f"Error in item: {item}")
                    
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
    category = input("Enter the category to view: ").strip().lower()
    print(f"\nTo-Do List for Category: '{category}':")
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        category_items = []
        for item in items:
            try:
                task, cat, deadline = item.strip().split('|')
                if cat.strip() == category.strip():
                    category_items.append(item.strip())
            except ValueError:
                print(f"Error in item: {item}")
        if not category_items:
            print(f"No items found for this category '{category}'.")
        else:
            for i, item in enumerate(category_items, 1):
                task, cat, deadline = item.strip().split('|')
                print(f"{i}. {task} - Due by {deadline}")
    print()

def search_todo_items():
    keyword = input("Enter the keyword to search for: ").strip().lower()
    print(f"\nSearching for items containing '{keyword}':")
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        matching_items = []
        for item in items:
            if keyword in item.strip().lower():
                matching_items.append(item.strip())
        if not matching_items:
            print(f"No items found containing '{keyword}'.")
        else:
            for i, item in enumerate(matching_items, 1):
                task, category, deadline = item.strip().split('|')
                print(f"{i}. [{category}] {task} - Due by {deadline}")
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
            search_todo_items()
        elif choice == '9':
            print('GoodBye.')
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
