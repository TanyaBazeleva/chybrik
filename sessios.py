from tkinter import *
from tkinter import PhotoImage
roof =Tk()
roof.title("chybrik")
roof.geometry("1263x676")
image_path = PhotoImage(file=r"C:\Прога\im.png")
bg_image=Label(roof,image=image_path)
bg_image.pack()

roof.mainloop()