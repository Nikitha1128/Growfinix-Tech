import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for task in file:
                task = task.strip()
                if task:
                    listbox.insert(tk.END, task)

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        tasks = listbox.get(0, listbox.size())
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")

def clear_tasks():
    listbox.delete(0, tk.END)
    save_tasks()

# Tkinter GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", width=15, command=clear_tasks)
clear_button.pack(pady=5)

# Load tasks on startup
load_tasks()

root.mainloop()
