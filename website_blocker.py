import tkinter as tk
from tkinter import messagebox

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

# Function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Website Blocker")

    label = tk.Label(root, text="Choose an action:")
    label.pack(pady=10)

    button_block = tk.Button(root, text="Block Website", command=lambda: block_website(entry_website.get()))
    button_block.pack(pady=5)

    button_list = tk.Button(root, text="List Blocked Websites", command=list_blocked_websites)
    button_list.pack(pady=5)

    button_unblock = tk.Button(root, text="Unblock Website", command=lambda: unblock_website(entry_website.get()))
    button_unblock.pack(pady=5)

    label_website = tk.Label(root, text="Enter website (e.g., example.com):")
    label_website.pack(pady=5)

    entry_website = tk.Entry(root, width=30)
    entry_website.pack(pady=5)

    root.mainloop()

# Start the GUI
create_gui()
