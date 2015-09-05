__author__ = 'JayantArora'


from tkinter import *



def main_window():
    window = Tk()
    window.geometry("600x300")
    window.config(background="light green")

    water = Frame(window, height=200, width=100)
    water.config(background="blue")
    water.pack(padx=50, pady=50)
    window.mainloop()




main_window()