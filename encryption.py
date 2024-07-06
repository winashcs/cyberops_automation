import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

# Function to encrypt a message
def encrypt_message():
    plain_text = entry_message.get()
    cipher_text = ""
    for l in plain_text:
        index = c.index(l)
        cipher_text += key[index]
    label_encrypted.config(text="Encrypted message: " + cipher_text)

# Function to decrypt a message
def decrypt_message():
    cipher_text = entry_message.get()
    plain_text = ""
    for l in cipher_text:
        index = key.index(l)
        plain_text += c[index]
    label_encrypted.config(text="Decrypted message: " + plain_text)

# Function to copy the encrypted or decrypted message to clipboard
def copy_message():
    message_to_copy = label_encrypted.cget("text")
    message_to_copy = message_to_copy.split(": ")[1]  # Get the actual message part
    pyperclip.copy(message_to_copy)
    messagebox.showinfo("Copy", "Message copied to clipboard!")

# Initialize the character sets and key
c = string.digits + string.ascii_letters + string.punctuation + " "
c = list(c)
key = c.copy()
random.shuffle(key)

# Create the main tkinter window
root = tk.Tk()
root.title("Message Encryption/Decryption")

# Create GUI elements
label_message = tk.Label(root, text="Enter message:")
label_message.pack()

entry_message = tk.Entry(root, width=50)
entry_message.pack()

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)
button_encrypt.pack()

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
button_decrypt.pack()

label_encrypted = tk.Label(root, text="")
label_encrypted.pack()

button_copy = tk.Button(root, text="Copy", command=copy_message)
button_copy.pack()

# Start the main tkinter event loop
root.mainloop()
