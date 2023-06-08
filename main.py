import tkinter
import dictionaries
from database import *
from tkinter import *

button_group_dictionary = {}
button_group_count = 0
chat_history = []

# Creates window

def chat():
    root = Tk()
    root.title("Chatbot")
    window_width = 500
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    container = Frame(root)
    canvas = Canvas(container)
    scrollbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    scrollable_frame.bind_all("<MouseWheel>", on_mousewheel)

    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(fill=BOTH, expand=True)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    canvas.create_window((0, 0), window=scrollable_frame, anchor=N)

    show_options("Start", scrollable_frame)

    root.mainloop()


def show_options(key, root):
    global button_group_count
    
    # Gets answer with key(parameter) and dictionary
    
    answer = dictionaries.answers[key]
    
    # Gets option from answer

    options = answer.get_options()
    
    # Defines master of object

    label = Label(master=root, text=answer.answer)
    label.pack(pady=5)

    button_group = []
    
    # Uses loop for drawing buttons
    
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

# Implements functionality of button
    
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


def create_ticket():
    db = Database()
    chat_history_string = ""

    for message in chat_history:
        chat_history_string += f"{message};"

    ticket = Ticket(2, chat_history_string)
    db.write(ticket)


chat()
