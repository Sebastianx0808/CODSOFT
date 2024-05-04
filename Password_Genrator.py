import tkinter as tk
import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    length = int(length_entry.get())
    password = "".join(random.sample(characters, length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)import tkinter as tk
import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    length = int(length_entry.get())  # Get the length of the password from the Entry widget
    password = "".join(random.sample(characters, length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

root.mainloop()


password_entry = tk.Entry(root, width=30)
password_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

root.mainloop()
