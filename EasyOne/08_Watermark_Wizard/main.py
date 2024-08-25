import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageEnhance

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Wizard")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(True, True)

        self.image_path = ""
        self.logo_path = ""
        self.transparency = tk.DoubleVar(value=100)

        self.title_frame = tk.Frame(root, bg="#34495e", pady=10)
        self.title_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.title_label = tk.Label(self.title_frame, text="Watermark Wizard", font=("Arial", 24, "bold"), fg="#ecf0f1", bg="#34495e")
        self.title_label.pack()

        self.main_frame = tk.Frame(root, bg="#2c3e50")
        self.main_frame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.upload_button = tk.Button(self.main_frame, text="Upload Image", command=self.upload_image, font=("Arial", 12), bg="#2980b9", fg="white", padx=20, pady=10)
        self.upload_button.grid(row=0, column=0, pady=10, sticky="ew")

        self.canvas_frame = tk.Frame(self.main_frame)
        self.canvas_frame.grid(row=1, column=0, pady=10, sticky="nsew")

        self.canvas = tk.Canvas(self.canvas_frame, bg="#ecf0f1", bd=0, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.logo_button = tk.Button(self.main_frame, text="Upload Logo", command=self.upload_logo, font=("Arial", 12), bg="#27ae60", fg="white", padx=20, pady=10)
        self.logo_button.grid(row=2, column=0, pady=10, sticky="ew")

        self.transparency_label = tk.Label(self.main_frame, text="Set Watermark Transparency:", font=("Arial", 12), bg="#2c3e50", fg="white")
        self.transparency_label.grid(row=3, column=0, pady=5, sticky="ew")
        self.transparency_slider = tk.Scale(self.main_frame, from_=0, to=100, orient="horizontal", variable=self.transparency, font=("Arial", 12), bg="#2c3e50", fg="white", troughcolor="#34495e")
        self.transparency_slider.grid(row=4, column=0, pady=5, sticky="ew")

        self.apply_button = tk.Button(self.main_frame, text="Apply Watermark", command=self.apply_watermark, font=("Arial", 12), bg="#c0392b", fg="white", padx=20, pady=10)
        self.apply_button.grid(row=5, column=0, pady=10, sticky="ew")

        self.save_button = tk.Button(self.main_frame, text="Save Image", command=self.save_image, font=("Arial", 12), bg="#8e44ad", fg="white", padx=20, pady=10)
        self.save_button.grid(row=6, column=0, pady=10, sticky="ew")

        self.img = None
        self.watermarked_image = None

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.img = Image.open(self.image_path)
            self.display_image(self.img)

    def upload_logo(self):
        self.logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
        if self.logo_path:
            messagebox.showinfo("Logo Uploaded", "Logo uploaded successfully!")

    def display_image(self, img):
        img.thumbnail((600, 400))
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def apply_watermark(self):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please upload an image first.")
            return

        if self.logo_path:
            logo = Image.open(self.logo_path)

            alpha = self.transparency.get() / 100
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
            alpha_channel = logo.split()[3]
            alpha_channel = ImageEnhance.Brightness(alpha_channel).enhance(alpha)
            logo.putalpha(alpha_channel)

            logo = logo.resize((100, 100))
            self.watermarked_image = self.img.copy()
            self.watermarked_image.paste(logo, (self.watermarked_image.width - 110, self.watermarked_image.height - 110), logo)
        else:
            messagebox.showwarning("No Watermark", "Please upload a logo.")

        self.display_image(self.watermarked_image)

    def save_image(self):
        if not self.watermarked_image:
            messagebox.showwarning("No Watermarked Image", "Please apply a watermark first.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_path:
            self.watermarked_image.save(save_path)
            messagebox.showinfo("Image Saved", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
