import tkinter as tk
from math import sqrt

# Function to update the expression in the entry box
def press(num):
    entry_text.set(entry_text.get() + str(num))

# Function to evaluate the final expression
def equal_press():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except ZeroDivisionError:
        entry_text.set("Error: Division by Zero")
    except:
        entry_text.set("Error")

# Function to clear the entry box
def clear():
    entry_text.set("")

# Function to calculate square root
def square_root():
    try:
        result = str(sqrt(float(entry_text.get())))
        entry_text.set(result)
    except:
        entry_text.set("Error")

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
entry_text = tk.StringVar()

# Entry widget
entry = tk.Entry(root, textvariable=entry_text, font=('Arial', 18), bd=5, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('√', 5, 0), ('Clear', 5, 1), ('=', 5, 2)
]

for (text, row, col) in buttons:
    if text == 'Clear':
        action = clear
    elif text == '=':
        action = equal_press
    elif text == '√':
        action = square_root
    else:
        action = lambda x=text: press(x)
    tk.Button(root, text=text, width=8, height=2, command=action).grid(row=row, column=col)

root.mainloop()
