import dictionaries
from tkinter import *

def chat():
    root = Tk()
    root.title("Chatbot")

    frame = Frame(master=root, width=750, height=600)
    frame.pack()

    for x in dicts:
        print(x)

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


chat()

frame = Tk.frame(master=root, width=500, height=500, bg='gray')
frame.pack()

w = Label(root, text="Hello bois")

w.pack()

root.mainloop()
