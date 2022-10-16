from tkinter import *


def calculate():
    conversion = float(miles_input.get()) * 1.60934
    answer_label.config(text=conversion)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry on grid col=2 row=1
miles_input = Entry(width=10)
miles_input.focus()
miles_input.insert(END, string="0")
miles_input.grid(column=2, row=1)

# Labels on grid col=3 row=1 (Miles), col=1 row=2 (is equal to), col=3 row=2 (Km)
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=1, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

# Updatable label on grid col=2 row=2
answer_label = Label(text=0)
answer_label.grid(column=2, row=2)

# Button on grid col=2 row=3
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=3)

window.mainloop()
