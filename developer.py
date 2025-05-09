from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text ="DEVELOPER",font =("times new roman",35,"bold"),bg = "white",fg ="Blue")
        title_lbl.place(x=0, y=0,width=1530,height = 45)

        
        img_top = Image.open(r"c:\Users\namra\Face recognition system\college_images\bg (1).png")
        
        img_top = img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 1530,height=720)

        #=======frame===========
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000, y=0,width =500,height = 600)

        img_top1 = Image.open(r"c:\Users\namra\Face recognition system\college_images\std1 (1).jpg")
        
        img_top1 = img_top1.resize((200,300), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame,image = self.photoimg_top1)
        f_lbl.place(x=300,y=0,width = 200,height=200)
    #=============developer info====================
        
        dev_label = Label(main_frame,text="Hello, my name is Namrata", font =("times new roman",20,"bold"),fg = "blue",bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame,text="I am full stack developer", font =("times new roman",20,"bold"),fg = "blue",bg="white")
        dev_label.place(x=0,y=40)

        img1 = Image.open(r"c:\Users\namra\Face recognition system\college_images\Face-Recognition-Software (2).png")
        img1 = img1.resize((500,390), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(main_frame,image = self.photoimg1)
        f_lbl.place(x=0,y=210,width = 500,height=390)




if __name__ == "__main__":
    print("✅ Starting the Face Recognition System...")  # Debug message
    root = Tk()
    root.state('zoomed')  # Open the window in fullscreen mode
    root.lift()
    root.focus_force()
    app = Developer(root)
    root.mainloop()
    print("✅ Window closed successfully.")  # Debug message after closing the window
