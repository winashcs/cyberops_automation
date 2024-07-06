import tkinter as tk
from tkinter import messagebox
import os

class KeyboardRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Recorder")

        self.record_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=20)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_application)
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

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardRecorder(root)
    root.mainloop()

