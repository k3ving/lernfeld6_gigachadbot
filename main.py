import dictionaries
from tkinter import *

<<<<<<< HEAD

=======
>>>>>>> 76f86dbdea136cf1601c76f7814e626f189a9483
def chat():
    root = Tk()
    root.title("Chatbot")

<<<<<<< HEAD
    frame = Frame(master=root, width=750, height=600)
    frame.pack()
=======
    for x in dicts:
        print(x)
>>>>>>> 76f86dbdea136cf1601c76f7814e626f189a9483

    start_options = dictionaries.answers["Start"].get_options()

    for option in start_options:
        print(option)
        option_button = Button(master=root, text=option, command=lambda: show_options(option, root))
        option_button.pack()
    root.mainloop()

        
    
def show_options(key, root):
    answer = dictionaries.answers[key]

    options = answer.get_options()

    for option in options:
        button = Button(master=root, text=option, command=lambda: show_options(option, root))
        button.pack()


<<<<<<< HEAD
chat()
=======
frame = Tk.frame(master=root, width=500, height=500, bg='gray')
frame.pack()

w = Label(root, text="Hello bois")

w.pack()

root.mainloop()

# chat()
>>>>>>> 76f86dbdea136cf1601c76f7814e626f189a9483
