from tkinter import *

window = Tk()

window.title("GUI text")
window.minsize(width=500, height=500)


my_label = Label(text="Test Label", font=("Arial", 24, "bold"))

my_label.pack()

my_label["text"] = "New Text"

def button_clicked():
    my_label["text"] = input.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()


input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()

