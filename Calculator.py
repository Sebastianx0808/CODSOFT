import tkinter as tk

root = tk.Tk()
root.title("Calculator")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_11 = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_click('+'))
button_12 = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_click('-'))
button_13 = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_click('/'))
button_14= tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click('*'))



button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0)
button_4.grid(row=2, column=1)
button_5.grid(row=3, column=0)
button_6.grid(row=3, column=1)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_11.grid(row=1, column=2)
button_12.grid(row=2, column=2)
button_13.grid(row=3, column=2)
button_14.grid(row=4, column=2)

button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)


button_clear.grid(row=6, column=0, columnspan=2)
button_equal.grid(row=6, column=2, columnspan=2)

root.mainloop()

