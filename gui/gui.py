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

# Entry for category
category_entry = tk.Entry(frame, width=30)
category_entry.insert(0, "Enter your category")
category_entry.pack(pady=5)

window.mainloop()