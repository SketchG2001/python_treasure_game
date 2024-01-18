from tkinter import *


def miles_to_killo():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Killo")
window.config(padx=20, pady=20)
# window.minsize(width=500, height=500)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="km")
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_killo)
calculate_button.grid(row=2, column=1)

window.mainloop()
