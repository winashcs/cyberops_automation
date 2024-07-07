import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import pyperclip
import os
import pyautogui
import rotatescreen
import time

# Encryption and Decryption Functions
def encrypt_message():
    plain_text = entry_message.get()
    cipher_text = ""
    for l in plain_text:
        index = c.index(l)
        cipher_text += key[index]
    label_encrypted.config(text="Encrypted message: " + cipher_text)

def decrypt_message():
    cipher_text = entry_message.get()
    plain_text = ""
    for l in cipher_text:
        index = key.index(l)
        plain_text += c[index]
    label_encrypted.config(text="Decrypted message: " + plain_text)

def copy_message():
    message_to_copy = label_encrypted.cget("text")
    message_to_copy = message_to_copy.split(": ")[1]  # Get the actual message part
    pyperclip.copy(message_to_copy)
    messagebox.showinfo("Copy", "Message copied to clipboard!")

# Keylogger
class KeyboardRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Recorder")

        self.record_button = ttk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=20)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.exit_application)
        self.exit_button.pack()

        self.recording = False
        self.recorded_text = ""

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.record_button.config(text="Stop Recording")
            self.root.bind("<Key>", self.on_key_press)
        else:
            self.recording = False
            self.record_button.config(text="Start Recording")
            self.root.unbind("<Key>")

            if self.recorded_text:
                self.save_to_file(self.recorded_text)
                self.recorded_text = ""

    def on_key_press(self, event):
        if self.recording:
            self.recorded_text += event.char

    def save_to_file(self, text):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "record.txt")
        with open(file_path, 'a') as f:
            f.write(text + '\n')

    def exit_application(self):
        if self.recording:
            messagebox.showwarning("Warning", "Please stop recording before exiting.")
        else:
            self.root.destroy()

# Mouse Pointer Malware
def perform_random_actions(num_iterations):
    pyautogui.FAILSAFE = False

    try:
        num_iterations = int(num_iterations)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")
        return

    for _ in range(num_iterations):
        h = random.randint(0, 1080)
        w = random.randint(0, 1920)
        pyautogui.click(w, h, duration=0.3)
        pyautogui.hotkey('winleft', 'm')

# Password Generator
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
    password = password_display.cget("text").split('\n')[1]
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Password Validator
def pv(password):
    if len(password) < 8:
        return "Your password must contain minimum 8 characters"
    
    has_alpha = False
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isalpha():
            has_alpha = True
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "@_!#$%^&*()<>?/|}{~:][":
            has_special = True
    
    if not has_alpha:
        return "Your password should contain alphabets"
    elif not has_lower:
        return "Your password should have lowercase"
    elif not has_upper:
        return "Your password should have uppercase"
    elif not has_digit:
        return "Your password should contain digits"
    elif not has_special:
        return "Your password does not have special characters"
    else:
        return "Password successful"

def validate_password():
    password = entry_password.get()
    validation_result = pv(password)
    messagebox.showinfo("Password Validation Result", validation_result)

# Screen Rotating Malware
def perform_screen_rotations(num_rotations):
    p = rotatescreen.get_primary_display()
    rotation_angles = [90, 180, 270, 0]
    
    for _ in range(num_rotations):
        for angle in rotation_angles:
            p.rotate_to(angle)
            time.sleep(0.5)

# Website Blocker
hosts_file_path = r"C:\Windows\System32\Drivers\etc\hosts"

def block_website(website):
    try:
        with open(hosts_file_path, 'r') as f:
            content = f.read()

        if any(website in line for line in content.splitlines()):
            messagebox.showinfo("Already Blocked", f"{website} is already blocked.")
        else:
            with open(hosts_file_path, 'a') as f:
                f.write(f"127.0.0.1 {website}\n")
            messagebox.showinfo("Blocked Successfully", f"{website} has been blocked successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def list_blocked_websites():
    try:
        with open(hosts_file_path, 'r') as f:
            content = f.readlines()

        blocked_websites = [line.strip().split()[1] for line in content if line.strip().startswith('127.0.0.1')]

        if blocked_websites:
            messagebox.showinfo("Blocked Websites", "Currently blocked websites:\n" + "\n".join(blocked_websites))
        else:
            messagebox.showinfo("Blocked Websites", "No websites are currently blocked.")

    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def unblock_website(website):
    try:
        with open(hosts_file_path, 'r') as f:
            lines = f.readlines()

        with open(hosts_file_path, 'w') as f:
            for line in lines:
                if not line.strip().startswith('127.0.0.1 ' + website):
                    f.write(line)
        
        messagebox.showinfo("Unblocked Successfully", f"{website} has been unblocked successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

# Main Application
class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")

        self.label = ttk.Label(root, text="Select an Option:")
        self.label.pack(pady=10)

        options = [
            "Encryption/Decryption",
            "Keylogger",
            "Mouse Pointer Malware",
            "Password Generator",
            "Password Validator",
            "Screen Rotating Malware",
            "Website Blocker"
        ]
        self.selected_option = tk.StringVar()
        self.menu = ttk.Combobox(root, textvariable=self.selected_option, values=options, state="readonly", width=30)
        self.menu.pack()

        self.menu.bind("<<ComboboxSelected>>", self.menu_option_selected)

        self.switch_button = ttk.Button(root, text="Switch Functionality", state=tk.DISABLED, command=self.switch_functionality)
        self.switch_button.pack(pady=10)

    def menu_option_selected(self, event=None):
        selection = self.selected_option.get()
        self.switch_button.config(state=tk.NORMAL)
        if selection == "Encryption/Decryption":
            self.setup_encryption_decryption()
        elif selection == "Keylogger":
            self.setup_keylogger()
        elif selection == "Mouse Pointer Malware":
            self.setup_mouse_pointer_malware()
        elif selection == "Password Generator":
            self.setup_password_generator()
        elif selection == "Password Validator":
            self.setup_password_validator()
        elif selection == "Screen Rotating Malware":
            self.setup_screen_rotating_malware()
        elif selection == "Website Blocker":
            self.setup_website_blocker()

    def switch_functionality(self):
        self.root.destroy()
        new_root = tk.Tk()
        new_app = MainApplication(new_root)
        new_root.mainloop()

    def setup_encryption_decryption(self):
        global c, key, entry_message, label_encrypted

        c = string.digits + string.ascii_letters + string.punctuation + " "
        c = list(c)
        key = c.copy()
        random.shuffle(key)

        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=10)

        label_message = ttk.Label(frame, text="Enter message:")
        label_message.grid(row=0, column=0, padx=5, pady=5)

        entry_message = ttk.Entry(frame, width=50)
        entry_message.grid(row=0, column=1, padx=5, pady=5)

        button_encrypt = ttk.Button(frame, text="Encrypt", command=encrypt_message)
        button_encrypt.grid(row=1, column=0, padx=5, pady=5)

        button_decrypt = ttk.Button(frame, text="Decrypt", command=decrypt_message)
        button_decrypt.grid(row=1, column=1, padx=5, pady=5)

        label_encrypted = ttk.Label(frame, text="")
        label_encrypted.grid(row=2, columnspan=2, padx=5, pady=5)

        button_copy = ttk.Button(frame, text="Copy", command=copy_message)
        button_copy.grid(row=3, columnspan=2, padx=5, pady=5)

    def setup_keylogger(self):
        root = tk.Tk()
        app = KeyboardRecorder(root)
        root.mainloop()

    def setup_mouse_pointer_malware(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=10)

        label_iterations = ttk.Label(frame, text="Enter number of iterations:")
        label_iterations.grid(row=0, column=0, padx=5, pady=5)

        entry_iterations = ttk.Entry(frame, width=20)
        entry_iterations.grid(row=0, column=1, padx=5, pady=5)

        button_start = ttk.Button(frame, text="Start", command=lambda: perform_random_actions(entry_iterations.get()))
        button_start.grid(row=1, columnspan=2, padx=5, pady=5)

    def setup_password_generator(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=10)

        label_length = ttk.Label(frame, text="Enter password length:")
        label_length.grid(row=0, column=0, padx=5, pady=5)

        global entry_length, password_display, copy_button

        entry_length = ttk.Entry(frame, width=20)
        entry_length.grid(row=0, column=1, padx=5, pady=5)

        button_generate = ttk.Button(frame, text="Generate Password", command=generate_password_button)
        button_generate.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        password_display = ttk.Label(frame, text="")
        password_display.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        copy_button = ttk.Button(frame, text="Copy Password", command=copy_to_clipboard, state=tk.DISABLED)
        copy_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def setup_password_validator(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=10)

        label_password = ttk.Label(frame, text="Enter your password:")
        label_password.grid(row=0, column=0, padx=5, pady=5)

        global entry_password
        entry_password = ttk.Entry(frame, show="*")
        entry_password.grid(row=0, column=1, padx=5, pady=5)

        button_validate = ttk.Button(frame, text="Validate Password", command=validate_password)
        button_validate.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def setup_screen_rotating_malware(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=10)

        label_rotations = ttk.Label(frame, text="Enter number of rotations:")
        label_rotations.grid(row=0, column=0, padx=5, pady=5)

        global entry_rotations

        entry_rotations = ttk.Entry(frame, width=20)
        entry_rotations.grid(row=0, column=1, padx=5, pady=5)

        button_rotate = ttk.Button(frame, text="Rotate Screen", command=lambda: perform_screen_rotations(int(entry_rotations.get())))
        button_rotate.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def setup_website_blocker(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=10)

        label_website = ttk.Label(frame, text="Enter website (e.g., example.com):")
        label_website.grid(row=0, column=0, padx=5, pady=5)

        global entry_website
        entry_website = ttk.Entry(frame, width=30)
        entry_website.grid(row=0, column=1, padx=5, pady=5)

        button_block = ttk.Button(frame, text="Block Website", command=lambda: block_website(entry_website.get()))
        button_block.grid(row=1, column=0, padx=5, pady=5)

        button_list = ttk.Button(frame, text="List Blocked Websites", command=list_blocked_websites)
        button_list.grid(row=1, column=1, padx=5, pady=5)

        button_unblock = ttk.Button(frame, text="Unblock Website", command=lambda: unblock_website(entry_website.get()))
        button_unblock.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Main Program Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
