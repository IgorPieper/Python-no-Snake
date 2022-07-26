from tkinter import *


def convert():
    miles_value = input1.get()
    try:
        km_value = int(miles_value) * 1.609
    except ValueError:
        km_value = 0
    output.config(text=km_value)


# Making a window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=120)

# Making a text
miles = Label(text=" ")
miles.grid(row=0, column=2)

# Making an input
input1 = Entry(width=10)
input1.insert(END, string=0)
input1.grid(row=1, column=1)

# Making a text
miles = Label(text=" Miles")
miles.grid(row=1, column=2)

# Making a text
equal = Label(text="   is equal to     ")
equal.grid(row=2, column=0)

# Making a text
output = Label(text=0)
output.grid(row=2, column=1)

# Making a text
km = Label(text="   Km")
km.grid(row=2, column=2)

# Making a button
button = Button(text="Calculate", bg="white", command=convert)
button.grid(row=3, column=1)

window.mainloop()
