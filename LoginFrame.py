from tkinter import *

from PIL import Image, ImageTk
class LoginFrame():
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1200x800')
        self.root.wm_iconbitmap("images\\icon.ico")
        self.user_icon = ImageTk.PhotoImage(Image.open("images\\user.png").resize((50, 50)))
        self.user_pass = ImageTk.PhotoImage(Image.open("images\\pass.png").resize((50, 50)))
        self.user_admin = ImageTk.PhotoImage(Image.open("images\\admin.png").resize((100, 100)))
        self.user_frame = ImageTk.PhotoImage(Image.open("images\\frame.jpg").resize((570, 500)))
        Frame_login = Frame(self.root)
        Frame_login.place( x=2, y=2, anchor=NW, height=250, width=470)
        Label(Frame_login, image=self.user_frame).place(relwidth=1, relheight=1)

        a = Label(Frame_login, text="Username",image=self.user_icon,bg="#26C4EC",fg="white",compound=LEFT,font=("times new roman",15,"bold")).grid(row=0, column=1)
        b = Label(Frame_login, text="Password",image=self.user_pass,bg="#26C4EC",fg="white",compound=LEFT,font=("times new roman",15,"bold")).grid(row=1, column=1)
        a1 = Entry(Frame_login,bd=2,bg="white",relief=RIDGE,font=("",15)).grid(row=0, column=2,padx=20,pady=20)
        b1 = Entry(Frame_login, textvariable="password", show='*',bd=2,bg="white",relief=RIDGE,font=("",15)).grid(row=1, column=2,padx=20,pady=20)
        c = Label(Frame_login, text="Mot de passe oublié ?", bg="#26C4EC", fg="white", compound=LEFT,font=("Helvetica", 12, "bold italic")).grid(row=4, column=2, padx=20,pady=20)
        btn1 = Button(Frame_login, command=self.verify_login(), text="Login",bg="#2EFE2E",fg="white",font=("times new roman",15,"bold"),width=10,height=1).grid(row=3, column=2,padx=20)

        self.root.bind("<Button-1>", self.change_pwd)
        self.root.mainloop()
    def change_pwd(self):
        print("test clic")
        return 0
    def verify_login(self):
        return 0
app=LoginFrame()
