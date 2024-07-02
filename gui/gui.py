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

window.mainloop()