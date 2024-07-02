import tkinter as tk
from tkinter import messagebox

# Add function to proceed the input
def add_task():
    # Get the input from the user
    task = task_entry.get()
    category = category_entry.get()
    deadline = deadline_entry.get()
    priority = priority_entry.get()

    if task and category and deadline and priority:
        # Add the task to the list
        task_listbox.insert(tk.END, f"Task: {task}, Category: {category}, Deadline: {deadline}, Priority: {priority}")
        messagebox.showinfo("Task Added", "Your task has been added successfully!")

        # Clear the entries
        task_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Incomplete Data", "Please fill out all fields.")

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

# Entry for category input
category_entry = tk.Entry(frame, width=30)
category_entry.insert(0, "Enter category")
category_entry.pack(pady=5)

# Entry for deadline input
deadline_entry = tk.Entry(frame, width=30)
deadline_entry.insert(0, "Enter deadline")
deadline_entry.pack(pady=5)

# Enter for priority input
priority_entry = tk.Entry(frame, width=30)
priority_entry.insert(0, "Enter priority")
priority_entry.pack(pady=5)

# Button to add task
add_task_button = tk.Button(frame, text="Add Task", width="15", command=add_task)
add_task_button.pack(pady=10)

# List box to display tasks
task_listbox = tk.Listbox(frame, width=80, height=10)
task_listbox.pack(pady=10)

window.mainloop()