from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    try:
        file = open(file="data.txt", mode="a")
    except FileNotFoundError:
        file = open(file="data.txt", mode="w")

    web = website_input.get()
    mail = mail_input.get()
    passwd = pass_input.get()

    if web and mail and passwd:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \n Email: {mail} \n "
                                                          f"Password: {passwd} \n\n Is it okay to save?")
        file.write(f"{web} / {mail} / {passwd}\n")
    else:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")

    file.close()

    website_input.delete(0, END)
    pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=16)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# First line

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=39)
website_input.grid(row=1, column=1, columnspan=2, pady=3)
website_input.focus()

# Second Line

mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0, pady=3)

mail_input = Entry(width=39)
mail_input.grid(row=2, column=1, columnspan=2, pady=3)
mail_input.insert(0, "igorpieper01@gmail.com")

# Third Line

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0, pady=3)

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1, pady=3)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2, pady=3)

# Fourth Line

add_button = Button(text="Add", width="36", command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=3)

window.mainloop()
