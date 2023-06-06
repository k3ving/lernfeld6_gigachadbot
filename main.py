import tkinter
import dictionaries
from tkinter import *
from tkinter import scrolledtext


def chat():
    root = Tk()
    root.title("Chatbot")
    window_width = 500
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    # frame = Frame(master=root)
    # frame.pack()

    chat_box = scrolledtext.ScrolledText(root, state=tkinter.DISABLED, cursor="arrow")
    chat_box.pack(fill=tkinter.BOTH, expand=True)

    show_options("Start", chat_box)

    root.mainloop()
        
    
def show_options(key, root):
    answer = dictionaries.answers[key]

    options = answer.get_options()

    label = Label(master=root, text=answer.answer)
    label.pack(pady=5)

    for option in options:
        button = Button(master=root, text=option, command=lambda: show_options(option, root))
        button.pack(pady=2)


chat()
