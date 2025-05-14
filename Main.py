import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Quiz Main: ')
        self.geometry('800x800')

        for i in range(3):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
            

        











root = MainApp()
root.mainloop()
