##README

#option to ask another question or quit. "Ask another question or type 'quit' to exit"
#small tkinter interface?

import time
import random
import sys
import tkinter as tk
from functools import partial
root = tk.Tk()

class Main(object):
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x150+500+300")
        self.root.minsize(400, 150)
        self.root.maxsize(400, 150)
        self.root.title("Magic 8-Ball")

        self.body_frame = tk.Frame(self.root, bg="black")
        self.body_frame.pack(anchor='center', fill="both", padx=10, pady=10)

        self.header_label = tk.Label(self.body_frame, text="What is your question?", font=(None, 15, 'bold'))
        
        self.user_entry_var = tk.StringVar()
        self.user_entry = tk.Entry(self.body_frame, textvariable=self.user_entry_var, font=(None, 15, 'bold'))
        self.user_entry.focus_set()
        self.root.bind("<Return>", lambda dots: self.generate_response(dots=""))



        self.output_var = tk.StringVar()
        self.output = tk.Entry(self.body_frame, textvariable=self.output_var, state="disabled", font=(None, 15, 'bold'))

        self.ask_button = tk.Button(self.body_frame, text="Ask", command=self.generate_response, height=2, font=(None, 10, 'bold'))
        self.clear_button = tk.Button(self.body_frame, text="Clear Text", command=self.clear_text, height=2, font=(None, 10, 'bold'))
        self.quit_button = tk.Button(self.body_frame, text="Quit", command=quit_app, height=2, font=(None, 10, 'bold'))

        self.body_frame.grid_columnconfigure(0, weight=1)
        self.body_frame.grid_columnconfigure(1, weight=1)
        self.body_frame.grid_columnconfigure(2, weight=1)

        self.header_label.grid(column=0, row=0, sticky='nsew', columnspan=3)
        self.user_entry.grid(column=0, row=1, sticky='nsew', columnspan=3)

        self.output.grid(column=0, row=2, sticky='nsew', columnspan=3)
        self.ask_button.grid(column=0, row=3, sticky='nsew')
        self.clear_button.grid(column=1, row=3, sticky='nsew')
        self.quit_button.grid(column=2, row=3, sticky='nsew')

    def generate_response(self, dots=""):
        list_of_responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        if self.user_entry_var.get() != '':
            if len(dots) < 4:
                self.output_var.set("thinking" + dots)
                dots += "."
                self.root.after(500, lambda: self.generate_response(dots))
            else:
                self.output_var.set(list_of_responses[random.randint(0, len(list_of_responses) - 1)])
        else:
            self.output_var.set("Sorry, I don't understand the question?")

    def clear_text(self):
        self.user_entry_var.set("")
        self.output_var.set("")

def quit_app():
    root.quit()
    root.destroy() #Removes the hidden root window
    sys.exit()


if __name__ == '__main__':
    main = Main(root)
    root.protocol("WM_DELETE_WINDOW", quit_app)
    root.mainloop()