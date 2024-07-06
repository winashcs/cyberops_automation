import tkinter as tk
import keyboard
import os

def record_keyboard():
    r = keyboard.record(until="escape")
    t = keyboard.get_typed_strings(r)
    x = "".join(t)
    save_to_file(x)

def save_to_file(text):
    script_dir = os.path.dirname(__file__)  # Absolute path of the script's directory
    file_path = os.path.join(script_dir, "record.txt")
    with open(file_path, 'a') as f:
        f.write(text + '\n')

# Create the GUI window
root = tk.Tk()
root.title("Keyboard Recorder")

# Create a button to start recording
record_button = tk.Button(root, text="Start Recording", command=record_keyboard)
record_button.pack(pady=20)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

# Start the GUI main loop
root.mainloop()

