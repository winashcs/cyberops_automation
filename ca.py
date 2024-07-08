from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import string
import random
import pyperclip
import pyautogui
import os
import time
import rotatescreen

# Define the path to the hosts file on Windows
hosts_file_path = r'C:/Windows/System32/drivers/etc/hosts'

class CA:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768+0+0')
        self.root.title('CyberOps Automation')
        self.root.iconbitmap('images/icon.ico')
        
        # Title and logos
        title = Label(self.root, text='CyberOps Automation', font=('Lucida Handwriting', 70, 'bold'), bg='#1178bd', fg='#ffd414')
        title.place(x=0, y=0, width=1366, height=130)
        
        # Images for functions and logos
        self.images = ['images/1.jpg', 'images/2.jpg', 'images/3.jpg', 'images/4.jpg', 'images/5.jpg', 'images/6.jpg', 'images/7.jpg', 'images/logo.png']
        self.function_labels = []
        self.load_images()
        self.animate()
        
        # Frame for function selection and display
        frame2 = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        frame2.place(x=0, y=326, width=1366, height=379)
        
        # Frame for function selection
        frame2_1 = LabelFrame(frame2, bd=2, relief=RIDGE, bg='black')
        frame2_1.place(x=0, y=12, width=680, height=350)
        
        sl1=Image.open('images/logo.png')
        sl1=sl1.resize((350,350), Image.LANCZOS)
        self.sl11=ImageTk.PhotoImage(sl1)
        self.sl111=Label(frame2_1,image=self.sl11,bg='black')
        self.sl111.grid(row=0, column=0, padx=10, pady=5, sticky='w') 
        
        # Label for function selection
        label_function = Label(frame2_1, text="Select   ▶", font=('Arial',17,'bold'), bg='black', fg='#fec101')
        label_function.grid(row=0, column=1, padx=10, pady=5, sticky='e')
        
        # Function selection combo box
        self.function_selection = ttk.Combobox(frame2_1, values=[
            "Encrypt Message",
            "Decrypt Message",
            "Keyboard Recorder",
            "Random Clicks",
            "Password Generator",
            "Password Validator",
            "Screen Rotation",
            "Website Blocker"
        ], state="readonly", font=('Arial', 9))
        self.function_selection.grid(row=0, column=2, padx=10, pady=5, sticky='w')
        self.function_selection.bind("<<ComboboxSelected>>", self.select_function)
        frame2_1.grid_columnconfigure(0, weight=1) 
        frame2_1.grid_columnconfigure(1, weight=1)
        frame2_1.grid_columnconfigure(2, weight=1)
        frame2_1.grid_rowconfigure(0, weight=1) 
        
        # Frame for function display
        self.frame2_2 = LabelFrame(frame2, bd=2, relief=RIDGE, bg='white')
        self.frame2_2.place(x=683, y=12, width=680, height=350)
        
        self.c = list(string.digits + string.ascii_letters + string.punctuation + " ")
        self.key = self.c.copy()
        random.shuffle(self.key)
    
    def load_images(self):
        self.image_objects = []
        for idx, img_path in enumerate(self.images):
            image = Image.open(img_path)
            image = image.resize((196, 196), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label = Label(self.root, image=photo)
            label.image = photo
            label.place(x=idx * 196, y=130, width=196, height=196)
            self.function_labels.append(label)
            self.image_objects.append((label, photo, idx * 196))
    
    def animate(self):
        for idx, (label, photo, current_x) in enumerate(self.image_objects):
            new_x = current_x - 1
            label.place_configure(x=new_x, y=130)
            self.image_objects[idx] = (label, photo, new_x)
            if new_x <= -196:
                label.place_configure(x=1366)
                self.image_objects[idx] = (label, photo, 1366)
        self.root.after(25, self.animate)
    
    def select_function(self, event):
        selected_function = self.function_selection.get()
        if selected_function == "Encrypt Message":
            self.select_encrypt()
        elif selected_function == "Decrypt Message":
            self.select_decrypt()
        elif selected_function == "Keyboard Recorder":
            self.select_keyboard_recorder()
        elif selected_function == "Random Clicks":
            self.select_random_actions()
        elif selected_function == "Password Generator":
            self.select_password_generator()
        elif selected_function == "Password Validator":
            self.select_password_validator()
        elif selected_function == "Screen Rotation":
            self.select_screen_rotation()
        elif selected_function == "Website Blocker":
            self.select_website_blocker()
    
    def select_encrypt(self):
        self.clear_frame2_2()
        self.encrypt_frame = Frame(self.frame2_2, bg='white')
        self.encrypt_frame.pack()
        
        # Image for Encrypt Message
        image_encrypt = Image.open('images/1.jpg')
        image_encrypt = image_encrypt.resize((200, 200), Image.LANCZOS)
        photo_encrypt = ImageTk.PhotoImage(image_encrypt)
        label_image_encrypt = Label(self.encrypt_frame, image=photo_encrypt, bg='white')
        label_image_encrypt.image = photo_encrypt
        label_image_encrypt.pack(side=LEFT, padx=20)
        
        # Function details for Encrypt Message
        label_message = Label(self.encrypt_frame, text="Enter message:")
        label_message.pack()
        
        self.entry_message = Entry(self.encrypt_frame, width=50)
        self.entry_message.pack()
        
        button_encrypt = Button(self.encrypt_frame, text="Encrypt", command=self.encrypt_message)
        button_encrypt.pack()
        
        self.label_encrypted = Label(self.encrypt_frame, text="")
        self.label_encrypted.pack()
        
        button_copy = Button(self.encrypt_frame, text="Copy", command=self.copy_message)
        button_copy.pack()
    
    def encrypt_message(self):
        plain_text = self.entry_message.get()
        cipher_text = ""
        for l in plain_text:
            index = self.c.index(l)
            cipher_text += self.key[index]
        self.label_encrypted.config(text="Encrypted message: " + cipher_text)
    
    def decrypt_message(self):
        cipher_text = self.entry_message.get()
        plain_text = ""
        for l in cipher_text:
            index = self.key.index(l)
            plain_text += self.c[index]
        self.label_encrypted.config(text="Decrypted message: " + plain_text)
    
    def copy_message(self):
        message_to_copy = self.label_encrypted.cget("text")
        message_to_copy = message_to_copy.split(": ")[1]
        pyperclip.copy(message_to_copy)
        messagebox.showinfo("Copy", "Message copied to clipboard!")
    
    def select_decrypt(self):
        self.clear_frame2_2()
        self.decrypt_frame = Frame(self.frame2_2, bg='white')
        self.decrypt_frame.pack()
        
        # Image for Decrypt Message
        image_decrypt = Image.open('images/1.jpg')
        image_decrypt = image_decrypt.resize((200, 200), Image.LANCZOS)
        photo_decrypt = ImageTk.PhotoImage(image_decrypt)
        label_image_decrypt = Label(self.decrypt_frame, image=photo_decrypt, bg='white')
        label_image_decrypt.image = photo_decrypt
        label_image_decrypt.pack(side=LEFT, padx=20)
        
        # Function details for Decrypt Message
        label_message = Label(self.decrypt_frame, text="Enter message:")
        label_message.pack()
        
        self.entry_message = Entry(self.decrypt_frame, width=50)
        self.entry_message.pack()
        
        button_decrypt = Button(self.decrypt_frame, text="Decrypt", command=self.decrypt_message)
        button_decrypt.pack()
        
        self.label_encrypted = Label(self.decrypt_frame, text="")
        self.label_encrypted.pack()
        
        button_copy = Button(self.decrypt_frame, text="Copy", command=self.copy_message)
        button_copy.pack()
    
    def select_keyboard_recorder(self):
        self.clear_frame2_2()
        self.keyboard_recorder = Frame(self.frame2_2, bg='white')
        self.keyboard_recorder.pack()
        
        # Image for Keyboard Recorder
        image_keyboard = Image.open('images/2.jpg')
        image_keyboard = image_keyboard.resize((200, 200), Image.LANCZOS)
        photo_keyboard = ImageTk.PhotoImage(image_keyboard)
        label_image_keyboard = Label(self.keyboard_recorder, image=photo_keyboard, bg='white')
        label_image_keyboard.image = photo_keyboard
        label_image_keyboard.pack(side=LEFT, padx=20)
        
        # Function details for Keyboard Recorder
        self.record_button = Button(self.keyboard_recorder, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=20)
        
        self.exit_button = Button(self.keyboard_recorder, text="Exit", command=self.exit_application)
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
    
    def select_random_actions(self):
        self.clear_frame2_2()
        self.random_actions = Frame(self.frame2_2, bg='white')
        self.random_actions.pack()
        
        # Image for Random Clicks
        image_random = Image.open('images/3.jpg')
        image_random = image_random.resize((200, 200), Image.LANCZOS)
        photo_random = ImageTk.PhotoImage(image_random)
        label_image_random = Label(self.random_actions, image=photo_random, bg='white')
        label_image_random.image = photo_random
        label_image_random.pack(side=LEFT, padx=20)
        
        # Function details for Random Clicks
        label_iterations = Label(self.random_actions, text="Enter the number of iterations:")
        label_iterations.pack(pady=10)
        
        self.entry_iterations = Entry(self.random_actions, width=20)
        self.entry_iterations.pack(pady=5)
        
        button_start = Button(self.random_actions, text="Start", command=self.start_random_actions)
        button_start.pack(pady=10)
    
    def start_random_actions(self):
        num_iterations = self.entry_iterations.get()
        self.perform_random_actions(num_iterations)
    
    def perform_random_actions(self, num_iterations):
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
            pyautogui.hotkey('win', 'd')
            time.sleep(2)
            pyautogui.hotkey('win', 'r')
            time.sleep(2)
    
    def select_password_generator(self):
        self.clear_frame2_2()
        self.password_generator = Frame(self.frame2_2, bg='white')
        self.password_generator.pack()
        
        # Image for Password Generator
        image_password = Image.open('images/4.jpg')
        image_password = image_password.resize((200, 200), Image.LANCZOS)
        photo_password = ImageTk.PhotoImage(image_password)
        label_image_password = Label(self.password_generator, image=photo_password, bg='white')
        label_image_password.image = photo_password
        label_image_password.pack(side=LEFT, padx=20)
        
        # Function details for Password Generator
        label_length = Label(self.password_generator, text="Enter password length:")
        label_length.pack(pady=10)
        
        self.entry_length = Entry(self.password_generator, width=20)
        self.entry_length.pack(pady=5)
        
        button_generate = Button(self.password_generator, text="Generate Password", command=self.generate_password_button)
        button_generate.pack(pady=10)
        
        self.password_display = Label(self.password_generator, text="")
        self.password_display.pack(pady=10)
        
        self.copy_button = Button(self.password_generator, text="Copy Password", command=self.copy_to_clipboard, state=DISABLED)
        self.copy_button.pack(pady=10)
    
    def generate_password_button(self):
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            password = self.generate_password(length)
            self.password_display.config(text=f"Generated Password:\n{password}")
            self.copy_button.config(state=NORMAL)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def copy_to_clipboard(self):
        password = self.password_display.cget("text").split('\n')[1]
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    
    def select_password_validator(self):
        self.clear_frame2_2()
        self.password_validator = Frame(self.frame2_2, bg='white')
        self.password_validator.pack()
        
        # Image for Password Validator
        image_validator = Image.open('images/5.jpg')
        image_validator = image_validator.resize((200, 200), Image.LANCZOS)
        photo_validator = ImageTk.PhotoImage(image_validator)
        label_image_validator = Label(self.password_validator, image=photo_validator, bg='white')
        label_image_validator.image = photo_validator
        label_image_validator.pack(side=LEFT, padx=20)
        
        # Function details for Password Validator
        label_password = Label(self.password_validator, text="Enter your password:")
        label_password.pack(pady=10)
        
        self.entry_password = Entry(self.password_validator, show="*")
        self.entry_password.pack(pady=5)
        
        button_validate = Button(self.password_validator, text="Validate Password", command=self.validate_password)
        button_validate.pack(pady=10)
    
    def validate_password(self):
        password = self.entry_password.get()
        validation_result = self.pv(password)
        messagebox.showinfo("Password Validation Result", validation_result)
    
    def pv(self, password):
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
    
    def select_screen_rotation(self):
        self.clear_frame2_2()
        self.screen_rotation = Frame(self.frame2_2, bg='white')
        self.screen_rotation.pack()
        
        # Image for Screen Rotation
        image_rotation = Image.open('images/6.jpg')
        image_rotation = image_rotation.resize((200, 200), Image.LANCZOS)
        photo_rotation = ImageTk.PhotoImage(image_rotation)
        label_image_rotation = Label(self.screen_rotation, image=photo_rotation, bg='white')
        label_image_rotation.image = photo_rotation
        label_image_rotation.pack(side=LEFT, padx=20)
        
        # Function details for Screen Rotation
        label_rotations = Label(self.screen_rotation, text="Enter the number of rotations:")
        label_rotations.pack(pady=10)
        
        self.entry_rotations = Entry(self.screen_rotation, width=20)
        self.entry_rotations.pack(pady=5)
        
        button_rotate = Button(self.screen_rotation, text="Rotate Screen", command=self.rotate_screen)
        button_rotate.pack(pady=10)
    
    def rotate_screen(self):
        try:
            num_rotations = int(self.entry_rotations.get())
            if num_rotations <= 0:
                raise ValueError("Number of rotations must be a positive integer.")
            
            self.perform_screen_rotations(num_rotations)
            messagebox.showinfo("Rotation Complete", f"Screen rotated {num_rotations} times.")
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def perform_screen_rotations(self, num_rotations):
        p = rotatescreen.get_primary_display()
        rotation_angles = [90, 180, 270, 0]
        
        for _ in range(num_rotations):
            for angle in rotation_angles:
                p.rotate_to(angle)
                time.sleep(0.5)
    
    def select_website_blocker(self):
        self.clear_frame2_2()
        self.website_blocker = Frame(self.frame2_2, bg='white')
        self.website_blocker.pack()
        
        # Image for Website Blocker
        image_website = Image.open('images/7.jpg')
        image_website = image_website.resize((200, 200), Image.LANCZOS)
        photo_website = ImageTk.PhotoImage(image_website)
        label_image_website = Label(self.website_blocker, image=photo_website, bg='white')
        label_image_website.image = photo_website
        label_image_website.pack(side=LEFT, padx=20)
        
        # Function details for Website Blocker
        label_website = Label(self.website_blocker, text="Enter website (e.g., example.com):")
        label_website.pack(pady=10)
        
        self.entry_website = Entry(self.website_blocker, width=30)
        self.entry_website.pack(pady=5)
        
        button_block = Button(self.website_blocker, text="Block Website", command=lambda: self.block_website(self.entry_website.get()))
        button_block.pack(pady=5)
        
        button_list = Button(self.website_blocker, text="List Blocked Websites", command=self.list_blocked_websites)
        button_list.pack(pady=5)
        
        button_unblock = Button(self.website_blocker, text="Unblock Website", command=lambda: self.unblock_website(self.entry_website.get()))
        button_unblock.pack(pady=5)
    
    def block_website(self, website):
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
    
    def list_blocked_websites(self):
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
    
    def unblock_website(self, website):
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
    
    def clear_frame2_2(self):
        for widget in self.frame2_2.winfo_children():
            widget.destroy()

# Initialize the application
if __name__ == "__main__":
    root = Tk()
    obj = CA(root)
    root.mainloop()
