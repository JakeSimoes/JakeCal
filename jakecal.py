from tkinter import *
import tkinter.font as font

# Initializing empty objects as I know no better way.
d = {}
button_dict = {}
root = Tk()
gh = 8
# These next two variables effect the button distance and color.
button_distance = 80
button_color = "#9e2219"
# The window's settings are set
root.configure(bg="white")
root.geometry("300x380")
root.wm_resizable(False, False)
root.title("Jakecal Version 0.3")
# calc_val is set to a automatically updating StringVar and put into label,
# calc_window.
font_size = font.Font(family=None, size=50)
calc_val = StringVar()
calc_window = Label(textvariable=calc_val, font=font_size, wraplength=300,
                    justify="left", bg='white', width=8).pack()

# Copyright protection ;)
bruh = Label(text="Copyright 2020, Jake Inc.")
bruh.pack()
bruh.place(x=0, y=240)
frame = Frame(root)
frame.pack()

# The nine buttons are created from a range using a dictionary template.
for i in range(9):
    d["num{}".format(i)] = Button(frame, text=str(i + 1),
                                  command=lambda num=i: func(str(num + 1)),
                                  height=3, width=6, bg=button_color,
                                  padx=10, pady=10, relief="flat")
    # Because I can't code well if statements are used to assign positions.
    if i <= 2:
        d["num{}".format(i)].grid(row=0, column=i)
    elif 2 < i <= 5:
        d["num{}".format(i)].grid(row=1, column=i - 3)
    else:
        d["num{}".format(i)].grid(row=2, column=i - 6)

# The plus button is initialized and placed into the grid.
plus_button = Button(frame, text="+", command=lambda: func(" + "), height=3,
                     width=6, bg=button_color, padx=10, pady=10, relief="flat")
plus_button.grid(row=2, column=4)

# The minus button is initialized and placed into the grid.
minus_button = Button(frame, text="-", command=lambda: func(" - "), height=3,
                      width=6, bg=button_color, padx=10, pady=10, relief="flat")
minus_button.grid(row=1, column=4)

# The division button is initialized and placed into the grid
division_button = Button(frame, text="/", command=lambda: func(" / "), height=3,
                         width=6, bg=button_color, padx=10, pady=10,
                         relief="flat")
division_button.grid(row=3, column=1)

# The zero button is initialized and placed into the grid
zero_button = Button(frame, text="0", command=lambda: func("0"), height=3,
                     width=6, bg=button_color, padx=10, pady=10, relief="flat")
zero_button.grid(row=3, column=2)

# The equal button is initialized and placed into the grid
equal_button = Button(frame, text="=", command=lambda: func("="), height=3,
                      width=6, bg=button_color, padx=10, pady=10, relief="flat")
equal_button.grid(row=3, column=4)

# The clear button is initialized and placed into the grid
clear_button = Button(frame, text="Clear", command=lambda: clear(), height=3,
                      width=6, bg=button_color, padx=10, pady=10, relief="flat")
clear_button.grid(row=0, column=4)

# The multiply button is initialized and placed into the grid
multiply_button = Button(frame, text="*", command=lambda: func(" * "), height=3,
                         width=6, bg=button_color, padx=10, pady=10,
                         relief="flat")
multiply_button.grid(row=3, column=0)

# The grid's button distance and position is set.
for row in range(3):
    frame.grid_rowconfigure(row, minsize=button_distance)
    frame.grid_columnconfigure(row, minsize=button_distance - 5)
frame.place(relx=0.002, y=65)

# Whenever font_resize is called it makes sure to extend the window when the
# value of calc_val has risen by 8.
def font_resize():
    global calc_window
    global gh
    if len(calc_val.get()) > gh:
        print("bro")
        root.geometry(
            "300x{}".format(380 + round(len(calc_val.get()) / 8) * 75))
        frame.place(relx=0.002, y=65 + round(len(calc_val.get()) / 8) * 75)
        gh += 8
    else:
        pass


def clear():
    global gh
    calc_val.set("")
    root.geometry("300x{}".format(380))
    frame.place(relx=0.002, y=65)
    gh = 8


# Adds the value passed to it to the calc_val string and evaluates it.
def func(i):
    # If the passed value meets all the requirements it is added to calc_val.
    if type(i) is int or (i == "+" or "-") and (i != "="):
        calc_val.set(calc_val.get() + i)
        font_resize()
    else:
        # A check is done to make sure calc_val doesn't start or end in an
        # operator and then the equation is evaluated.
        if (calc_val.get()[1] not in "+-/*") and \
                (calc_val.get()[-2] not in "+-/*"):
            calc_val.set(eval(calc_val.get()))


# Required to be last, maintains the window.
root.mainloop()
