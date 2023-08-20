import tkinter as tk
from tkinter import ttk
from zabezpieczenia import zabezpiecz
from obsluga_przyciskow import *
import math
from functools import partial
from PIL import Image, ImageTk

dokladnosc = 7


def configure_window(window):
    style = ttk.Style()

    window.title("Kalkulator")

    # Ikona Okna
    image = Image.new('RGBA', (1, 1), (1, 1, 1, 1))
    photo = ImageTk.PhotoImage(image)
    window.tk.call('wm', 'iconphoto', window._w, photo)

    # Wielkość Okna
    window.geometry("700x700")
    window.minsize(700, 700)
    window.maxsize(700, 700)

    # Kolor Tła
    window.configure(background="#1e1e1e")

    # Ustawienia Przycisków
    style.configure("Button", background="#ffbd59", font=("Arial", 16))

    # Ustawienia Tekstu
    style.configure("Button", background="#ffbd59", font=("Arial", 16))
    style.configure("TEntry", foreground="white", font=("Arial", 16))

    # Konfiguracja siatki (grid)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    # --------------------------[Pola Tekstowe]-------------------------- #

    # Pole tekstowe 1
    liczba1 = tk.StringVar()
    number_entry = tk.Entry(window, textvariable=liczba1, width=15, font=("Arial", 16), justify="center")
    number_entry.configure(bg="#ffbd59", fg="black")
    number_entry.grid(row=0, column=0, padx=4, pady=10)
    number_entry.focus_set()

    # Pole tekstowe 2
    liczba2 = tk.StringVar()
    number_entry2 = tk.Entry(window, textvariable=liczba2, width=15, font=("Arial", 16), justify="center")
    number_entry2.configure(bg="#ffbd59", fg="black")
    number_entry2.grid(row=0, column=1, padx=4, pady=10)

    # Pole z wynikiem
    liczba3 = tk.DoubleVar()
    number_entry3 = tk.Entry(window, textvariable=liczba3, width=15, font=("Arial", 16), justify="center",
                             state="readonly")
    number_entry3.grid(row=0, column=2, padx=4, pady=10)

    # ----------------------------[Przyciski]----------------------------

    # Przycisk Dodawania
    przycisk1 = tk.Button(window, text="+", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 1))

    przycisk1.grid(row=1, column=0, pady=(0, 5))

    # Przyciski Odejmowania
    przycisk2 = tk.Button(window, text="-", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 2))

    przycisk2.grid(row=1, column=1, pady=(0, 5))

    # Przyciski Usuwania
    przyciskC = tk.Button(window, text="Del", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: usun_wynik(liczba3))

    przyciskC.grid(row=1, column=2, pady=(0, 5))

    # Przyciski Mnożenia
    przycisk3 = tk.Button(window, text="×", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 3))

    przycisk3.grid(row=2, column=0, pady=(0, 5))

    # Przyciski Dzielenia
    przycisk4 = tk.Button(window, text="÷", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 4))

    przycisk4.grid(row=2, column=1, pady=(0, 5))

    # Przyciski Procenta
    przycisk7 = tk.Button(window, text="%", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 7))

    przycisk7.grid(row=2, column=2, pady=(0, 5))

    # Przyciski Potęgowania
    przycisk5 = tk.Button(window, text="x²", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 5))

    przycisk5.grid(row=3, column=0, pady=(0, 5))

    # Przyciski Pierwiastkowania
    przycisk6 = tk.Button(window, text="√", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 6))

    przycisk6.grid(row=3, column=1, pady=(0, 5))

    # Przyciski Silni
    przycisk8 = tk.Button(window, text="!", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 8))

    przycisk8.grid(row=3, column=2, pady=(0, 5))

    # Przyciski Sinus
    przycisk11 = tk.Button(window, text="sin", width=7, bg="#ffbd59", font=("Arial", 16),
                           command=lambda: przyciski(liczba1, liczba2, liczba3, 11))

    przycisk11.grid(row=4, column=0, pady=(0, 5))

    # Przyciski Cosinus
    przycisk12 = tk.Button(window, text="cos", width=7, bg="#ffbd59", font=("Arial", 16),
                           command=lambda: przyciski(liczba1, liczba2, liczba3, 12))

    przycisk12.grid(row=4, column=1, pady=(0, 5))

    # Przyciski Tangens
    przycisk13 = tk.Button(window, text="tg", width=7, bg="#ffbd59", font=("Arial", 16),
                           command=lambda: przyciski(liczba1, liczba2, liczba3, 13))

    przycisk13.grid(row=4, column=2, pady=(0, 5))

    # Przyciski Logarytmu
    przycisk9 = tk.Button(window, text="log", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 9))

    przycisk9.grid(row=5, column=0, pady=(0, 5))

    # Przycisk modulo
    przycisk10 = tk.Button(window, text="mod", width=7, bg="#ffbd59", font=("Arial", 16),
                          command=lambda: przyciski(liczba1, liczba2, liczba3, 10))

    przycisk10.grid(row=5, column=1, pady=(0, 5))