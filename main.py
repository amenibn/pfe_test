from tkinter import *
from PIL import Image, ImageTk
import json
import random
import string


class Window():
    def __init__(self):
        self.root=Tk()
        self.root.title("Leoni Application")
        self.root.geometry('1280x720')
        self.root.wm_iconbitmap("images\\icon.ico")
        self.user_icon=ImageTk.PhotoImage(Image.open("images\\user.png").resize((50,50)))
        self.user_pass = ImageTk.PhotoImage(Image.open("images\\pass.png").resize((50, 50)))
        self.user_admin= ImageTk.PhotoImage(Image.open("images\\admin.png").resize((100, 100)))
        Leoni = PhotoImage(file="images\\Leoni.png").zoom(5).subsample(15)
        bgimage=ImageTk.PhotoImage(Image.open(r"images\\bgg.jpg").resize((1280,720)))
        ig = ImageTk.PhotoImage(Image.open("images\\login.png").resize((200, 40)))

        Label(self.root,image=bgimage).place(relwidth=1, relheight=1)
        Label(self.root, image=Leoni, bg="#FFFFFF").place(x=630,y=50,anchor=NW)
        Label(self.root, image=self.user_admin, bg="#FFFFFF",text="Administrator",fg="#0B0B61",compound=TOP,font=("Castellar", 20, "bold italic")).place(x=700,y=226,anchor=NW)
        btn = Button(self.root, command=self.login_form, image=ig, bd=0).place(x=740,y=370,anchor=NW)


       # render = ImageTk.PhotoImage(Image.open("images\\bg1.png").resize((1200, 750)))
       # img = Label(self.root, image=render)
       # img.image = render
        #img.place(x=0, y=80)
        #width=300
        #height=300








        #canvas = Canvas(self.root, width=width, height=height , bg=0, y=0ge, border=0 ,highlightthickness=0)
        #canvas.create_image(width/2, height/2, image=image)
        #canvas.pack()

        self.root.mainloop()


    def login_form(self):
        for widgets in self.root.winfo_children():

            if widgets.winfo_name()=="!button":
                widgets.destroy()
        self.user_icon_login = ImageTk.PhotoImage(Image.open("images\\user.png").resize((50, 50)))
        self.user_pass = ImageTk.PhotoImage(Image.open("images\\pass.png").resize((50, 50)))
        self.user_admin = ImageTk.PhotoImage(Image.open("images\\admin.png").resize((100, 100)))
        self.user_frame = ImageTk.PhotoImage(Image.open("images\\frame.jpg").resize((570, 500)))
        Frame_login = Frame(self.root)
        Frame_login.place(x=700, y=420, anchor=NW, height=250, width=470)
        Label(Frame_login, image=self.user_frame).place(relwidth=1, relheight=1)

        a = Label(Frame_login, text="Username", image=self.user_icon_login, bg="#26C4EC", fg="white", compound=LEFT,
                  font=("times new roman", 15, "bold")).grid(row=0, column=1)
        b = Label(Frame_login, text="Password", image=self.user_pass, bg="#26C4EC", fg="white", compound=LEFT,
                  font=("times new roman", 15, "bold")).grid(row=1, column=1)
        a1 = Entry(Frame_login, bd=2, bg="white", relief=RIDGE, font=("", 15)).grid(row=0, column=2, padx=20, pady=20)
        b1 = Entry(Frame_login, textvariable="password", show='*', bd=2, bg="white", relief=RIDGE, font=("", 15)).grid(
            row=1, column=2, padx=20, pady=20)

        btn1 = Button(Frame_login, command=self.verify_login, text="Login", bg="#2EFE2E", fg="white",
                      font=("times new roman", 15, "bold"), width=10, height=1).grid(row=3, column=2, padx=20)
        # c = Label(Frame_login, text="Mot de passe oublié ?", bg="#26C4EC", fg="white", compound=LEFT,
        #           font=("Helvetica", 12, "bold italic")).grid(row=4, column=2, padx=20, pady=20)
        # self.root.bind("<Button-1>", self.change_pwd)
        # c.pack()
        c=Button(Frame_login, command= self.change_pwd, text="mot de passe oubliée").grid(row=4, column=2, padx=20, pady=20)

    def change_pwd(self ):
        def randomString(stringLength=8):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))
        new_password = randomString()
        user={
            "username":"admin",
            "password": new_password
        }

        with open('scripts\confidentials.json', 'w') as json_file:
            json.dump(user, json_file)

        return 0
    def verify_login(self):
        test=True
        with open('scripts\confidentials.json') as f:
             user=json.load(f)
        for widgets in self.root.winfo_children():
            if widgets.winfo_name() == "!frame":
                for i in widgets.winfo_children():

                    if i.winfo_name()=="!entry":
                       if i.get()!=user["username"]:
                           print( "wrong username")
                           test = False
        for widgets in self.root.winfo_children():
            if widgets.winfo_name() == "!frame":
                for i in widgets.winfo_children():

                    if i.winfo_name()=="!entry2":
                       if i.get()!=user["password"]:
                           print("wrong password")
                           test = False


        return test





app=Window()
