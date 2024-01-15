from tkinter import *
import base64
import os

def main_screen():
    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encryption App")

    label = Label(
        text="Enter text for encryption and decryption",
        fg="black", font = ("calbri", 13))
    
    label.place(x=10, y=10)

    text1 = Text(font= "Robote 20", bg= "white", relief= GROOVE, wrap= WORD)
    text1.place(x=10, y=50, width= 355, height= 100)

    screen.mainloop()

main_screen()