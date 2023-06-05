import dicts
import answer as ans
from tkinter import *

start_dict = {
    "Absturz": ans.Answer("Ein Absturz. Welche der folgenden Dinge trifft zu?", ["Meow", "Neow"]),
    "Problem bei Login": ans.Answer("Probleme beim Login. Was trifft am ehesten zu?", ["Falscher Nutzername", "Falsche Email"])
}

def chat():
    print("Hallo. Wie kann ich behilflich sein?")

    for x in start_dict:
        print(x)

    show_options(input("Eingabe: "), True)

    done = False

    while not done:
        user_input = input("Eingabe: ")

        if user_input.lower() == "done" or user_input == "":
            done = True
            break

        show_options(user_input, False)
        
    
def show_options(key, start):
    if start:
        answer = start_dict[key]
    else:
        answer = dicts.answers[key]

    options = answer.get_options()

    for x in options:
        print(x)

root = Tk()
root.title("Chatbot")

frame = Tk.frame(master=root, width=500, height=500, bg='gray')
frame.pack()

w = Label(root, text="Hello bois")

w.pack()

root.mainloop()

# chat()