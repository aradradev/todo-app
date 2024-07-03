import json
import tkinter as tk
from tkinter import messagebox

# Add function to proceed the input
def add_task():
    # Get the input from the user
    task = task_entry.get()
    category = category_filter.get()
    deadline = deadline_entry.get()
    priority = priority_entry.get()

    if task and category and deadline and priority:
        # Add the task to the list
        task_listbox.insert(tk.END, f"Task: {task}, Category: {category}, Deadline: {deadline}, Priority: {priority}, Complete: False")
        all_tasks.append({"task": task, "category": category, "deadline": deadline, 'priority': priority, "complete": False})
        messagebox.showinfo("Task Added", "Your task has been added successfully!")

        # Clear the entries
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Incomplete Data", "Please fill out all fields.")

# Remove task function
def remove_task():
    # Get the selected task from the listbox
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        all_tasks.pop(selected_task_index)
        messagebox.showinfo("Task Removed", "Your task has been removed successfully!")
    except IndexError:
        messagebox.showerror("No Selection", "Please select a task to remove.")

# Edit task function
def edit_task():
    # Get the selected task from the listbox
    try:
        selected_task_index = task_listbox.curselection()[0]
        selected_task = task_listbox.get(selected_task_index)

        task_details = selected_task.split(", ")
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)

        task_entry.insert(0, task_details[0].split(": ")[1])
        category_filter.set(task_details[1].split(": ")[1])
        deadline_entry.insert(0, task_details[2].split(": ")[1])
        priority_entry.insert(0, task_details[3].split(": ")[1])

        task_listbox.delete(selected_task_index)
        all_tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showerror("No Selection", "Please select a task to edit.")

# Filter task function
def filter_task():
    # Get the selected task from the listbox
    try:
        select_category = category_filter.get()
        if select_category == 'All':
            display_all_tasks()
        else:
            task_listbox.delete(0, tk.END)
            for task in all_tasks:
                if f"Category: {select_category}" in task:
                    task_str = f"Task: {task['task']}, Category: {task['category']}, Deadline: {task['deadline']}, Priority: {task['priority']}, Complete: True"
                    task_listbox.insert(tk.END, task_str)
    except IndexError:
        messagebox.showerror("No Selection", "Please select a category.")

def display_all_tasks():
    task_listbox.delete(0, tk.END)
    for task in all_tasks:
        task_str = f"Task: {task['task']}, Category: {task['category']}, Deadline: {task['deadline']}, Priority: {task['priority']}, Complete: True"
        task_listbox.insert(tk.END, task_str)


# Mark complete function
def mark_complete():
    # Get the selected task from the listbox
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, {'bg':'lightgreen'})
        task = all_tasks[selected_task_index]
        task['complete'] = True
        updated_tasks = f"Task: {task['task']}, Category: {task['category']}, Deadline: {task['deadline']}, Priority: {task['priority']}, Complete: True"
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, updated_tasks)
        messagebox.showinfo("Task Complete", "Your task has been completed successfully!")
    except IndexError:
        messagebox.showerror("No Selection", "Please select a task to mark as complete.")

# View Completed tasks function
def view_completed_tasks():
    task_listbox.delete(0, tk.END)
    for task in all_tasks:
        if task['complete'] == True:
            task_str = f"Task: {task['task']}, Category: {task['category']}, Deadline: {task['deadline']}, Priority: {task['priority']}, Complete: True"
            task_listbox.insert(tk.END, task_str)

# Save tasks function
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(all_tasks, file)
    messagebox.showinfo("Save Tasks", "Tasks saved successfully!")

# Initialize the main window
window = tk.Tk()

window.title('To-Do App')

window.geometry('600x500')

# Create a frame to hold the widget
frame = tk.Frame(window)
frame.pack(pady=20)

# Create a label to display the title
title_label = tk.Label(frame, text="To-Do List", font=("Helvetica", 18))
title_label.pack()

# Entry for task input
task_entry = tk.Entry(frame, width=30)
task_entry.insert(0, "Enter your task")
task_entry.pack(pady=5)

# Entry for deadline input
deadline_entry = tk.Entry(frame, width=30)
deadline_entry.insert(0, "Enter deadline")
deadline_entry.pack(pady=5)

# Enter for priority input
priority_entry = tk.Entry(frame, width=30)
priority_entry.insert(0, "Enter priority")
priority_entry.pack(pady=5)

# Category dropdown
category_list = ["All", "Personal", "Work", "Shopping", "Others"]
category_filter = tk.StringVar(value="All")
category_menu = tk.OptionMenu(frame, category_filter, *category_list)
category_menu.pack(pady=5)

# Button to add task
add_task_button = tk.Button(frame, text="Add Task", width=15, command=add_task)
add_task_button.pack(pady=5)

# Button to edit task
edit_task_button = tk.Button(frame, text="Edit Task", width=15, command=edit_task)
edit_task_button.pack(pady=5)

# Button to apply the filter
filter_button = tk.Button(frame, text="Filter Task", width=15, command=filter_task)
filter_button.pack(pady=5)

# Button to mark complete
mark_complete_button = tk.Button(frame, text="Mark Complete", width=15, command=mark_complete)
mark_complete_button.pack(pady=5)

# Button to view completed task
view_complete_button = tk.Button(frame, text="View Complete", width=15, command=view_completed_tasks)
view_completed_button.pack(pady=5)

# Button to save tasks
save_task_button = tk.Button(frame, text="Save Task", width=15, command=save_tasks)

# Button to remove task
remove_task_button = tk.Button(frame, text="Remove Task", width=15, command=remove_task)
remove_task_button.pack(pady=5)

# List box to display tasks
task_listbox = tk.Listbox(frame, width=80, height=10)
task_listbox.pack(pady=10)

all_tasks = []

window.mainloop()