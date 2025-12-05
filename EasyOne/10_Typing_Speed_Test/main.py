import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample texts
TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests help improve accuracy and efficiency.",
    "Practice every day and you can easily reach one hundred words per minute.",
    "Python is a great programming language for building desktop applications."
]


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x400")

        self.start_time = None
        self.sample_text = random.choice(TEXTS)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Type the following text:", font=("Arial", 14)).pack(pady=10)

        self.text_display = tk.Text(self.root, height=5, width=80, font=("Arial", 12), wrap="word")
        self.text_display.insert("1.0", self.sample_text)
        self.text_display.config(state="disabled")
        self.text_display.pack(pady=5)

        tk.Label(self.root, text="Your typing:", font=("Arial", 14)).pack(pady=5)

        self.user_input = tk.Text(self.root, height=5, width=80, font=("Arial", 12), wrap="word")
        self.user_input.pack(pady=5)
        self.user_input.bind("<KeyPress>", self.start_timer)

        tk.Button(self.root, text="Check result", font=("Arial", 14),
                  command=self.calculate_speed).pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showwarning("Error", "You must start typing to begin the test!")
            return

        end_time = time.time()
        time_taken = end_time - self.start_time

        typed_text = self.user_input.get("1.0", "end").strip()
        num_words = len(typed_text.split())

        wpm = (num_words / time_taken) * 60 if time_taken > 0 else 0

        # Calculate accuracy
        correct_chars = 0
        for a, b in zip(self.sample_text, typed_text):
            if a == b:
                correct_chars += 1

        accuracy = (correct_chars / len(self.sample_text)) * 100

        messagebox.showinfo(
            "Typing Test Result",
            f"Words per minute (WPM): {wpm:.2f}\n"
            f"Time taken: {time_taken:.2f} seconds\n"
            f"Word count: {num_words}\n"
            f"Accuracy: {accuracy:.2f}%"
        )

        # Reset for next test
        self.start_time = None
        self.sample_text = random.choice(TEXTS)
        self.text_display.config(state="normal")
        self.text_display.delete("1.0", "end")
        self.text_display.insert("1.0", self.sample_text)
        self.text_display.config(state="disabled")
        self.user_input.delete("1.0", "end")


if __name__ == "__main__":
    root = tk.Tk()
    TypingSpeedApp(root)
    root.mainloop()
