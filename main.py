from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    print("")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        encryptLabel = Label(screen1, text="ENCRYPT",
              font="arial", fg="white", bg="#ed3833")
        encryptLabel.place(x=10, y=0)

        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE,
                     wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)

    elif password=="":
        messagebox.showerror("Encryption", "Please Enter the Password")
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")





def main_screen():

    global screen
    global text1
    global code

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encryption App")

    def reset():
        code.set("")
        text1.delete(1.0, END)

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
                     bg= "#ed3833", fg= "white", bd= 0,
                     command=encrypt)
    button1.place(x= 10, y= 250)

    button2 = Button(text= "DECRYPT", height= 2, width= 23, 
                     bg= "#00bd56", fg= "white", bd= 0,
                     command=decrypt)
    button2.place(x= 200, y= 250)

    button3 = Button(text= "RESET", height= 2, width= 50, 
                     bg= "#1089ff", fg= "white", bd= 0, 
                     command= reset)
    button3.place(x= 10, y= 300)

    screen.mainloop()

main_screen()