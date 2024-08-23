from tkinter import *
import tkinter
import random
import string
import tkinter.messagebox
root = Tk()
root.title("BlackEye Password Generator")
root.geometry("500x500")
root.config(background="skyblue")

pass_length = StringVar()
pass_string = StringVar()


password_list = string.ascii_letters + string.digits + string.punctuation
password = [i for i in password_list]
def generate_pass():
    pass_string.set("")
    char = pass_length.get()
    if char == '':
        char = 0
    else:char = int(char)
    s = pass_string.get()
    while len(s) < char:
        a = password[random.randrange(0,len(password))]
        s += a
    pass_string.set(s)  


def help_about():
    tkinter.messagebox.showinfo("Help about Black Eye","Black was developed by marvecodes in 2024 for the purpose of good an secure password at the age of fourteen")
len_password = Label(root,text="Write the length of password you want")
len_password.config(font=("Futura",14,'italic'))
len_password.place(x=0,y=0)
len_password.config(background="skyblue")


input_pass = Entry(root,font=("Courier",14),textvariable=pass_length) 
input_pass.place(x=0,y=30)

generate_password = Button(root,text="Generate",command=generate_pass)
generate_password.place(x=0,y=50)

password_var = Label(root,text="This is your password")
password_var.config(font=("Arial",14,"italic"))
password_var.place(x=0,y=90)
password_var.config(background="skyblue")

password_full = Entry(root,font=("Futura",14),textvariable=pass_string)
password_full.place(x=0,y=150)

exit_ = Button(root,text="Exit",command=root.destroy)
help_ = Button(root,text="Help",command=help_about)
help_.place(x=250,y=300)
exit_.place(x=250,y=250)
root.mainloop()
