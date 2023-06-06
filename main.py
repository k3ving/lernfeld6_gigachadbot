import tkinter
import dictionaries
from tkinter import *
from tkinter import scrolledtext

button_group_dictionary = {}
button_group_count = 0


def chat():
    root = Tk()
    root.title("Chatbot")
    window_width = 500
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    chat_box = scrolledtext.ScrolledText(root, state=tkinter.DISABLED, cursor="arrow")
    chat_box.pack(fill=tkinter.BOTH, expand=True)

    show_options("Start", chat_box)

    root.mainloop()


def show_options(key, root):
    global button_group_count
    answer = dictionaries.answers[key]

    options = answer.get_options()

    label = Label(master=root, text=answer.answer)
    label.pack(pady=5)

    button_group = []

    for option in options:
        button = Button(master=root,
                        text=option,
                        bd=1, relief="solid",
                        pady=2, padx=2,
                        command=lambda o=option: button_click(o, button_group_count, root))
        button.pack(pady=2)
        button_group.append(button)

    button_group_count += 1
    button_group_dictionary[button_group_count] = button_group


def button_click(option, button_group_id, root):
    print(option)
    toggle_button_group(option, button_group_id)
    show_options(option, root)


def toggle_button_group(option, button_group_id):
    button_group = button_group_dictionary.get(button_group_id)

    for button in button_group:
        if button["text"] == option:
            button.configure(bg="#b3ffb3")
        button.configure(state=tkinter.DISABLED)


chat()
