from tkinter import *

class LoginFrame():
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1200x800')
        a = Label(self.root, text="username").grid(row=0, column=0)
        b = Label(self.root, text="password").grid(row=1, column=0)
        a1= Entry(self.root).grid(row=0, column=1)
        b1= Entry(self.root,textvariable="password", show='*').grid(row=1, column=1)
        btn1 = Button(self.root, command=self.verify_login(), text="Login").grid(row=3, column=1)
        c =Label(self.root, text="mot de passe oublié").grid(row=4, column=1)
        self.root.bind("<Button-1>",self.change_pwd)
        self.root.mainloop()
    def change_pwd(self):
        print("test clic")
        return 0
    def verify_login(self):
        return 0
app=LoginFrame()
