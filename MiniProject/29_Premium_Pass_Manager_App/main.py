import io
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    web = website_input.get()
    mail = mail_input.get()
    passwd = pass_input.get()

    new_data = {web: {
        "email": mail,
        "password": passwd,
    }}

    if web and mail and passwd:
        messagebox.askokcancel(title=web, message=f"These are the details entered: \n Email: {mail} \n "
                                                  f"Password: {passwd} \n\n Is it okay to save?")

        try:
            file = open(file="data.json", mode="r")
        except FileNotFoundError:
            file = open(file="data.json", mode="w")
        file.close()

        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        except io.UnsupportedOperation:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
    else:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")

    website_input.delete(0, END)
    pass_input.delete(0, END)


# ---------------------------- SEARCH BUTTON ------------------------------- #

def search():
    web = website_input.get()

    try:
        file = open(file="data.json", mode="r")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data available for this site")
    else:
        data = json.load(file)
        if web in data:
            print(data[web])
            messagebox.askokcancel(title=web, message=f" Email: {data[web]['email']} \n "
                                                      f"Password: {data[web]['password']} \n")
        else:
            messagebox.showinfo(title="Oops", message="No data available for this site")
        file.close()

# ---------------------------- UI SETUP ------------------------------- #

BG_COLOR = "#5D576B"
BUTTON_COLOR = "#D4483B"
INPUT_COLOR = "#3A3042"
FONT_COLOR = "#E4E3D3"

window = Tk()
window.title("Password Manager")
window.geometry("530x380")
window.config(padx=20, pady=16, bg=BG_COLOR)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BG_COLOR)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# First line

website_label = Label(text="Website:", width=18, bg=BG_COLOR, fg=FONT_COLOR)
website_label.grid(row=1, column=0)

website_input = Entry(width=21, bg=INPUT_COLOR, fg=FONT_COLOR)
website_input.grid(row=1, column=1, pady=3, padx=(49, 0))
website_input.focus()

search_button = Button(text="Search", command=search, width=16, bg=BUTTON_COLOR, fg=FONT_COLOR)
search_button.grid(row=1, column=2, pady=3)

# Second Line

mail_label = Label(text="Email/Username:", bg=BG_COLOR, fg=FONT_COLOR)
mail_label.grid(row=2, column=0, pady=3)

mail_input = Entry(width=43, bg=INPUT_COLOR, fg=FONT_COLOR)
mail_input.grid(row=2, column=1, columnspan=2, pady=3, padx=(59, 0))
mail_input.insert(0, "igorpieper01@gmail.com")

# Third Line

pass_label = Label(text="Password:", bg=BG_COLOR, fg=FONT_COLOR)
pass_label.grid(row=3, column=0, pady=3)

pass_input = Entry(width=21, bg=INPUT_COLOR, fg=FONT_COLOR)
pass_input.grid(row=3, column=1, pady=3, padx=(49, 0))

pass_button = Button(text="Generate Password", command=generate_password, width=16, bg=BUTTON_COLOR, fg=FONT_COLOR)
pass_button.grid(row=3, column=2, pady=3)

# Fourth Line

add_button = Button(text="Add", width="36", command=save, bg=BUTTON_COLOR, fg=FONT_COLOR)
add_button.grid(row=4, column=1, columnspan=2, pady=3, padx=(59, 0))

window.mainloop()
