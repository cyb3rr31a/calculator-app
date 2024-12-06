import tkinter as tk
from tkinter import ttk

# Function to update the input field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())  # Unsafe in production; validate inputs in real apps
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#f3f4f6")

# Create a styled input field
entry = ttk.Entry(root, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Define common button style
button_style = {
    "font": ("Arial", 18),
    "width": 5,
    "height": 2,
    "relief": "solid"
}

# Create buttons and arrange them in a grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(
            root, text=text, command=calculate, bg="#4caf50", fg="#ffffff",
            activebackground="#388e3c", activeforeground="#ffffff", **button_style
        ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == 'C':
        tk.Button(
            root, text=text, command=clear, bg="#f44336", fg="#ffffff",
            activebackground="#d32f2f", activeforeground="#ffffff", **button_style
        ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(
            root, text=text, command=lambda t=text: button_click(t),
            bg="#ffffff", fg="#333333", activebackground="#e0e0e0",
            activeforeground="#333333", **button_style
        ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Adjust grid spacing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
