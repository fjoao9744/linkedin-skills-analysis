import tkinter as tk

class Tela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        
        self.input = tk.Entry(self)
        self.input.pack()
        
        self.button = tk.Button(self, text="Scraping", command=self.start_scraping)
        self.button.pack()
        
        
        self.mainloop()
        
    def start_scraping(self):
        self.button["state"] = "disable"
        
        
tela = Tela()

