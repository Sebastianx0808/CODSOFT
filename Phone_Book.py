import tkinter as tk
from tkinter import messagebox, simpledialog
from pymongo import MongoClient
import re
from tabulate import tabulate


client = MongoClient('mongodb://localhost:27017/')
db = client['contact_manager']
contacts_collection = db['contacts']


contact_ids = []


def validate_name(name):
    return re.match(r'^[A-Za-z\s]+$', name) is not None

def validate_phone(phone):
    return re.match(r'^\d{10}$', phone) is not None

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not validate_name(name):
        messagebox.showerror("Error", "Invalid name. Name should only contain letters and spaces.")
        return
    if not validate_phone(phone):
        messagebox.showerror("Error", "Invalid phone number. Please enter a 10-digit phone number.")
        return
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email address.")
        return

    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts_collection.insert_one(contact)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_fields()


def view_contacts():
    contacts = contacts_collection.find({})
    contact_list.delete(0, tk.END)
    global contact_ids
    contact_ids = [] 
    for contact in contacts:
        contact_list.insert(tk.END, f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
        contact_ids.append(contact['_id']) 

def update_contact_popup():
    selected_contact = contact_list.curselection()
    if selected_contact:
        contact_index = selected_contact[0]
        contact_id = contact_ids[contact_index]
        contact = contacts_collection.find_one({'_id': contact_id})
        if contact:
            update_window = tk.Toplevel(root)
            update_window.title("Update Contact")

            
            tk.Label(update_window, text="Name:", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
            name_entry_popup = tk.Entry(update_window)
            name_entry_popup.insert(0, contact['name'])
            name_entry_popup.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(update_window, text="Phone:", font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
            phone_entry_popup = tk.Entry(update_window)
            phone_entry_popup.insert(0, contact['phone'])
            phone_entry_popup.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(update_window, text="Email:", font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=10, pady=5)
            email_entry_popup = tk.Entry(update_window)
            email_entry_popup.insert(0, contact['email'])
            email_entry_popup.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(update_window, text="Address:", font=("Helvetica", 12, "bold")).grid(row=3, column=0, padx=10, pady=5)
            address_entry_popup = tk.Entry(update_window)
            address_entry_popup.insert(0, contact['address'])
            address_entry_popup.grid(row=3, column=1, padx=10, pady=5)

            
            def save_contact():
                updated_name = name_entry_popup.get().strip()
                updated_phone = phone_entry_popup.get().strip()
                updated_email = email_entry_popup.get().strip()
                updated_address = address_entry_popup.get().strip()

                if not validate_name(updated_name):
                    messagebox.showerror("Error", "Invalid name. Name should only contain letters and spaces.")
                    return
                if not validate_phone(updated_phone):
                    messagebox.showerror("Error", "Invalid phone number. Please enter a 10-digit phone number.")
                    return
                if not validate_email(updated_email):
                    messagebox.showerror("Error", "Invalid email address.")
                    return

                updated_contact = {
                    'name': updated_name,
                    'phone': updated_phone,
                    'email': updated_email,
                    'address': updated_address
                }
                contacts_collection.update_one({'_id': contact_id}, {'$set': updated_contact})
                messagebox.showinfo("Success", "Contact updated successfully!")
                update_window.destroy()
                view_contacts()

            
            save_button = tk.Button(update_window, text="Save", font=("Helvetica", 12), command=save_contact, bg="#4CAF50", fg="white")
            save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

        else:
            messagebox.showerror("Error", "Contact not found.")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")


def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        contact_index = selected_contact[0]
        contacts_collection.delete_one({'_id': contact_ids[contact_index]})
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_fields()
        view_contacts()
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contacts():
    search_window = tk.Toplevel(root)
    search_window.title("Search Contacts")
    
    tk.Label(search_window, text = "Search by Name or Phone Number: ", font = ("Helvetica", 12, "bold")).grid(row =0, column=0, padx=10, pady=5)
    search_entry = tk.Entry(search_window, font=("Helvetica", 12))
    search_entry.grid(row=2, column=0, padx=10, pady=5)
    
    def perform_search():
        query = search_entry.get().strip()
        search_results = contacts_collection.find({
            '$or': [
                {'name': {'$regex': f'.*{query}.*', '$options': 'i'}},
                {'phone': {'$regex': f'.*{query}.*'}}
            ]
        })
        
        
        
        
        table_data = [[contact['name'], contact['phone'], contact['email'], contact['address']] for contact in search_results]

        
        search_results_str = tabulate(table_data, headers=["Name", "Phone", "Email", "Address"], tablefmt="grid")

        
        search_result_label = tk.Label(search_window, text=search_results_str, font=("Helvetica", 12))
        search_result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        
    search_button = tk.Button(search_window, text="Search", font=("Helvetica", 12), command=perform_search, bg="#4CAF50", fg="white")
    search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="WE")



root = tk.Tk()
root.title("Contact Manager")
root.configure(bg="#f0f0f0")


tk.Label(root, text="Name:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="W")
name_entry = tk.Entry(root, font=("Helvetica", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="W")
phone_entry = tk.Entry(root, font=("Helvetica", 12))
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="W")
email_entry = tk.Entry(root, font=("Helvetica", 12))
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="W")
address_entry = tk.Entry(root, font=("Helvetica", 12))
address_entry.grid(row=3, column=1, padx=10, pady=5)


contact_list = tk.Listbox(root, width=50, font=("Helvetica", 12))
contact_list.grid(row=4, column=0, columnspan=2, padx=10, pady=5)


add_button = tk.Button(root, text="Add Contact", font=("Helvetica", 12), command=add_contact, bg="#4CAF50", fg="white")
add_button.grid(row=5, column=0, padx=10, pady=5, sticky="WE")

view_button = tk.Button(root, text="View Contacts", font=("Helvetica", 12), command=view_contacts, bg="#2196F3", fg="white")
view_button.grid(row=5, column=1, padx=10, pady=5, sticky="WE")

update_button = tk.Button(root, text="Update Contact", font=("Helvetica", 12), command=update_contact_popup, bg="#FFC107", fg="black")
update_button.grid(row=6, column=0, padx=10, pady=5, sticky="WE")

delete_button = tk.Button(root, text="Delete Contact", font=("Helvetica", 12), command=delete_contact, bg="#F44336", fg="white")
delete_button.grid(row=6, column=1, padx=10, pady=5, sticky="WE")

search_button = tk.Button(root, text="Search Contacts", font=("Helvetica", 12), command=search_contacts, bg="#607D8B", fg="white")
search_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="WE")


root.mainloop()
