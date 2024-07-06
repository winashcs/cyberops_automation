import tkinter as tk
from tkinter import messagebox

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

root = tk.Tk()
root.title("Password Validator")

label_password = tk.Label(root, text="Enter your password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

button_validate = tk.Button(root, text="Validate Password", command=validate_password)
button_validate.pack(pady=10)

root.mainloop()
