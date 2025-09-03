import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts()
    update_listbox()
    clear_entries()
    messagebox.showinfo("Success", f"Contact {name} added successfully!")

def delete_contact():
    try:
        selected = listbox.curselection()[0]
        name = listbox.get(selected)
        if name in contacts:
            del contacts[name]
            save_contacts()
            update_listbox()
            messagebox.showinfo("Deleted", f"Contact {name} deleted successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a contact to delete")

def search_contact():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)
    for name in contacts:
        if query in name.lower():
            listbox.insert(tk.END, name)

def update_listbox():
    listbox.delete(0, tk.END)
    for name in contacts:
        listbox.insert(tk.END, name)

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def show_contact_details(event):
    try:
        selected = listbox.curselection()[0]
        name = listbox.get(selected)
        details = contacts.get(name, {})
        messagebox.showinfo("Contact Details",
                            f"Name: {name}\n"
                            f"Phone: {details.get('phone', '')}\n"
                            f"Email: {details.get('email', '')}\n"
                            f"Address: {details.get('address', '')}")
    except IndexError:
        pass

# Load existing contacts
contacts = load_contacts()

# Tkinter GUI
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Search
tk.Label(root, text="Search by Name").pack()
search_entry = tk.Entry(root, width=30)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)
tk.Button(root, text="Show All", command=update_listbox).pack(pady=5)

# Listbox to show contacts
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)
listbox.bind("<Double-1>", show_contact_details)

# Initial load
update_listbox()

root.mainloop()
