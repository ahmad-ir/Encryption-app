from tkinter import *
import base64
import os

def main_screen():
    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encryption App")

    lable1 = Label(
        text="Enter text for encryption and decryption",
        fg="black", font = ("calbri", 13))
    
    lable1.place(x=10, y=10)

    text1 = Text(font= "Robote 20", bg= "white", relief= GROOVE, wrap= WORD)
    text1.place(x=10, y=50, width= 355, height= 100)

    label2 = Label(text= "Enter secret key for encryption and decryption", 
                   fg= "black", font= ("calibri", 13))
    label2.place(x= 10, y= 170)

    code = StringVar()
    entry = Entry(textvariable= code, 
                  width= 19, bd= 0, 
                  font= ("arial", 25), 
                  show= "*")
    entry.place(x=10, y= 200)

    button1 = Button(text= "ENCRYPT", height= 2, width= 23, 
                     bg= "#ed3833", fg= "white", bd= 0)
    button1.place(x= 10, y= 250)

    button2 = Button(text= "DECRYPT", height= 2, width= 23, 
                     bg= "#00bd56", fg= "white", bd= 0)
    button2.place(x= 200, y= 250)

    screen.mainloop()

main_screen()