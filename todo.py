from datetime import datetime, timedelta
import json

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
    print("9. Sort To-Do List")
    print("10. Set Reminders for Tasks")
    print("11. Save To-Do List")
    print("12. Load To-Do List")
    print("13. Exit")

def view_todo_list():
    print("\nTo-Do List:")
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        if not items:
            print("No items found.")
        else:
            for i, item in enumerate(items, 1):
                try:
                    task, category, deadline, priority = item.strip().split('|')
                    print(f"{i}. [{category} ] {task} - Priority: {priority} - Due by {deadline}")
                except ValueError:
                    print(f"Error in item: {item}")
    print()
    

def add_todo_item():
    item = input("Enter a new to-do item: ").strip().lower()
    category = input("Enter a category for this item: ").strip().lower()
    deadline = input("Enter a deadline for this item (YYYY-MM-DD): ")
    priority = input("Enter the priority for this item (High, Medium, Low): ").strip().lower()
    with open('todo_list.txt', 'a') as file:
        file.write(f"{item} | {category} | {deadline} | {priority}\n")
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
        new_priority = input("Enter the new priority (High, Medium, Low): ")
        items[item_number - 1] = f"{new_item} | {new_category} | {new_priority} | {new_deadline}\n"
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
                    task, category, deadline, priority = item.strip().split('|')
                    print(f"{i}. [{category}], {task} - Priority: {priority} - Due by {deadline}")
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
                task, cat, deadline, priority = item.strip().split('|')
                if cat.strip() == category.strip():
                    category_items.append(item.strip())
            except ValueError:
                print(f"Error in item: {item}")
        if not category_items:
            print(f"No items found for this category '{category}'.")
        else:
            for i, item in enumerate(category_items, 1):
                task, cat, deadline = item.strip().split('|')
                print(f"{i}. {task} - Priority: {priority} - Due by {deadline}")
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
                task, category, deadline, priority = item.strip().split('|')
                print(f"{i}. [{category}] {task} - Priority: {priority} - Due by {deadline}")
    print()

def sort_todo_list():
    print("\nSort To-Do List")
    print("1. By Priority")
    print("2. By Deadline")
    print("3. By Category")
    choice = input("Enter your choice: ")

    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
    if  not items:
        print("No items found.")
        return
    if choice == '1':
        sorted_items = sorted(items, key=lambda x: x.strip().split('|')[3].lower())
    elif choice == '2':
        sorted_items = sorted(items, key=lambda x: x.strip().split('|')[2].lower())
    elif choice == '3':
        sorted_items = sorted(items, key=lambda x: x.strip().split('|')[1].lower())
    else:
        print("Invalid choice. Returning to main menu.")
        return
    
    print("\n Sorted To-Do List:")
    for i, item in enumerate(sorted_items, 1):
        try:
            task, category, deadline, priority = item.strip().split('|')
            print(f"{i}. [{category}] {task} - Priority: {priority} - Due by {deadline}\n")
        except ValueError:
            print(f"Error in item: {item}")
    print()

def set_reminder():
    print("\nSetting Reminders for Upcoming Tasks")
    reminder_days = int(input("Enter the number of days before the deadline to set a reminder: "))
    current_date = datetime.now()
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        if not items:
            print("No items found.")
            return
        
        upcoming_tasks = []
        for item in items:
            try:
                task, category, deadline, priority = item.strip().split('|')
                deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
                if deadline_date - current_date <= timedelta(days=reminder_days):
                    upcoming_tasks.append(item.strip())
            except ValueError:
                print(f"Error in item: {item}")
                
                if not upcoming_tasks:
                    print(f"No tasks found with deadlines within {reminder_days} days.")
                else:
                    print(f"\nUpcoming Tasks with deadlines within {reminder_days} days:")
                    for i, item in enumerate(upcoming_tasks, 1):
                        task, category, deadline, priority = item.strip().split('|')
                        print(f"{i}. [{category}] {task} - Priority: {priority} - Due by {deadline}")
    print()

def save_to_json():
    with open('todo_list.txt', 'r') as file:
        items = file.readlines()
        todo_list = []
        for item in items:
            try:
                task, category, deadline, priority = item.strip().split('|')
                todo_list.append({
                    'task': task,
                    'category': category,
                    'deadline': deadline,
                    'priority': priority
                })
            except ValueError:
                print(f"Error in item: {item.strip()}")
    with open('todo_list.json', 'w') as json_file:
        json.dump(todo_list, json_file, indent=4)
    print("To-Do List saved to todo_list.json")

def load_json():
    try:
        with open('todo_list.json', 'r') as json_load:
            todo_list = json.load(json_load)
        with open('todo_list.txt', 'w') as file:
            for item in todo_list:
                file.write(f"{item['task']} | {item['category']} | {item['deadline']} | {item['priority']}\n")
        print("To-Do List loaded from todo_list.json")
    except FileNotFoundError:
        print("No To-Do List found. Please add items to the list first.")

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
            sort_todo_list()
        elif choice == '10':
            set_reminder()
        elif choice == '11':
            save_to_json()
        elif choice == '12':
            load_json()
        elif choice == '13':
            print('GoodBye.')
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
