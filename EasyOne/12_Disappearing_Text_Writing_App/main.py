import tkinter as tk
import time
import threading


class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Writing App")
        self.root.geometry("800x600")

        self.last_keypress_time = time.time()

        self.create_widgets()

        self.running = True
        thread = threading.Thread(target=self.check_idle_time)
        thread.daemon = True
        thread.start()

    def create_widgets(self):
        label = tk.Label(
            self.root,
            text="Start typing... Stop for 5 seconds and everything will be erased!",
            font=("Arial", 14)
        )
        label.pack(pady=10)

        # Text box for writing
        self.text_box = tk.Text(self.root, font=("Arial", 16), wrap="word")
        self.text_box.pack(expand=True, fill="both", padx=10, pady=10)

        # Bind typing event
        self.text_box.bind("<KeyPress>", self.reset_timer)

    def reset_timer(self, event=None):
        self.last_keypress_time = time.time()

    def check_idle_time(self):
        while self.running:
            idle_time = time.time() - self.last_keypress_time

            if idle_time > 5:
                self.text_box.delete("1.0", tk.END)
                self.last_keypress_time = time.time()

            time.sleep(0.1)

    def stop(self):
        self.running = False


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)

    def on_close():
        app.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
