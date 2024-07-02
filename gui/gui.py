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
        task_listbox.insert(tk.END, f"Task: {task}, Category: {category}, Deadline: {deadline}, Priority: {priority}")
        all_tasks.append(f"Task: {task}, Category: {category}, Deadline: {deadline}, Priority: {priority}")
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
                    task_listbox.insert(tk.END, task)
    except IndexError:
        messagebox.showerror("No Selection", "Please select a category.")

def display_all_tasks():
    task_listbox.delete(0, tk.END)
    for task in all_tasks:
        task_listbox.insert(tk.END, task)

# Initialize the main window
window = tk.Tk()

window.title('To-Do App')

window.geometry('600x400')

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
add_task_button = tk.Button(frame, text="Add Task", width="15", command=add_task)
add_task_button.pack(pady=10)

# Button to edit task
edit_task_button = tk.Button(frame, text="Edit Task", width="15", command=edit_task)
edit_task_button.pack(pady=10)

# Button to apply the filter
filter_button = tk.Button(frame, text="Filter Task", width="15", command=filter_task)

# Button to remove task
remove_task_button = tk.Button(frame, text="Remove Task", width="15", command=remove_task)
remove_task_button.pack(pady=10)

# List box to display tasks
task_listbox = tk.Listbox(frame, width=80, height=10)
task_listbox.pack(pady=10)

all_tasks = []

window.mainloop()