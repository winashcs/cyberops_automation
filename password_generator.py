import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

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
        password_display.config(text=f"Generated Password:\n{password}")
        copy_button.config(state=tk.NORMAL)  # Enable copy button
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    password = password_display.cget("text").split('\n')[1]  # Extract the password
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Random Password Generator")

label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=10)

entry_length = tk.Entry(root, width=20)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password_button)
button_generate.pack(pady=10)

password_display = tk.Label(root, text="")
password_display.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=10)

root.mainloop()

