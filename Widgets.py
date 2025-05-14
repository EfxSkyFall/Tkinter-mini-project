import tkinter as tk


class Quizlabel(tk.Label):
    def __init__(self,parent, label_text):
        super().__init__(parent)

        self.configure(text=label_text)

        self.grid(sticky='nsew', padx=10,pady=10)
    
