from tkinter import *
#
# window = Tk()
#
# window.title("GUI text")
# window.minsize(width=500, height=500)
#
#
# my_label = Label(text="Test Label", font=("Arial", 24, "bold"))
#
# my_label.pack()
#
# my_label["text"] = "New Text"
#
# def button_clicked():
#     my_label["text"] = input.get()
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
#
#
# input = Entry(width=10)
# input.pack()
# print(input.get())
#
#
# window.mainloop()

window2 = Tk()

window2.title("Mile to Kilometer Converter")
window2.minsize(width=500, height=500)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

my_label = Label(text="Miles", font=("Arial", 18, "bold"))
my_label.grid(column=2, row=0)

left_text = Label(text="is equal to", font=("Arial", 18, "bold"))
left_text.grid(column=0, row=1)

def do_calculation():
    result = float(user_input.get()) * 1.609
    calculated_num.config(text=f"{result}")

button = Button(text="Calculate", command=do_calculation)
button.grid(column=1, row=3)

right_text = Label(text="is equal to", font=("Arial", 18, "bold"))
right_text.grid(column=2, row=1)

calculated_num = Label(text="0")
calculated_num.grid(column=1, row=1)

window2.mainloop()