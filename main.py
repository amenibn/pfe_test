from tkinter import *
from PIL import Image, ImageTk

class Window():
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1200x800')
        btn = Button(self.root, text="login", command=self.login_form, width="20", height="5", bg="blue")
        btn.place(x=0, y=0)
        render = ImageTk.PhotoImage(Image.open("images\\bg1.png").resize((1200, 750)))
        img = Label(self.root, image=render)
        img.image = render
        img.place(x=0, y=80)

        self.root.mainloop()
    def login_form(self):
        for widget in self.root.winfo_children():
            print(widget)
        exit()

app=Window()
