import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        password = generate_password(length)
        messagebox.showinfo("Generated Password", f"Generated Password:\n{password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Random Password Generator")

label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=10)

entry_length = tk.Entry(root, width=20)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password_button)
button_generate.pack(pady=10)

root.mainloop()
