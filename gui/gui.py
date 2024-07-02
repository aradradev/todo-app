import tkinter as tk

# Initialize the main window
window = tk.Tk()

window.title('To-Do App')

window.geometry('500x400')

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
add_task_button = tk.Button(frame, text="Add Task", width="15")
add_task_button.pack(pady=10)

window.mainloop()