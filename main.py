from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from facerecognitionsystem import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        print("✅ Window is opening...")  # Debug message to confirm script execution

        
        # First Image
        img = Image.open(r"c:\Users\namra\Face recognition system\college_images\facial.jpeg").resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 500,height=130)

        # Second Image
        img1 = Image.open(r"C:\Users\namra\Face recognition system\college_images\threephoto.jpeg").resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"c:\Users\namra\Face recognition system\college_images\img1.jpeg").resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=550, height=130)

        # Background Image
        img3 = Image.open(r"c:\Users\namra\Face recognition system\college_images\river.jpeg").resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title Label
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")\
            .place(x=0, y=0, width=1530, height=45)
        
        #==================time===================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl =Label(title_lbl,font=("times new roman",14,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=130,width=150,height=50)
        time()

        
        #student button

        img4 = Image.open(r"c:\Users\namra\Face recognition system\college_images\gamers.jpeg").resize((220,220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student)
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Detect face button

        img5= Image.open(r"c:\Users\namra\Face recognition system\college_images\boy.jpeg")
        img5 = img5.resize((220,220),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

       
        b1 = Button(bg_img, image= self.photoimg5,cursor = "hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text = "Face Detector",cursor = "hand2",command=self.face_data,font =("times new roman",15,"bold"),bg = "dark blue",fg ="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance Face Button

        img6= Image.open(r"c:\Users\namra\Face recognition system\college_images\attendance.jpg.jpeg")
        img6= img6.resize((220,220),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

       
        b1 = Button(bg_img, image= self.photoimg6,cursor = "hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text = "Attendance",cursor = "hand2",command=self.attendance_data,font =("times new roman",15,"bold"),bg = "dark blue",fg ="white")
        b1_1.place(x=800,y=300,width=220,height=40)

         #Help Desk

        img7= Image.open(r"C:\Users\namra\Face recognition system\college_images\helpdesk.jpeg")
        img7= img7.resize((220,220),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

       
        b1 = Button(bg_img, image= self.photoimg7,cursor = "hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text = "Help Desk",cursor = "hand2",command=self.help_data,font =("times new roman",15,"bold"),bg = "dark blue",fg ="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Train Face Button
        img8= Image.open(r"C:\Users\namra\Face recognition system\college_images\train data.jpeg")
        img8= img8.resize((220,220),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

       
        b1 = Button(bg_img, image= self.photoimg8,cursor = "hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1 = Button(bg_img, text = "Train Data",cursor = "hand2",command=self.train_data,font =("times new roman",15,"bold"),bg = "dark blue",fg ="white")
        b1_1.place(x=200,y=580,width=220,height=40)

         #Photo Face Button
        img9= Image.open(r"C:\Users\namra\Face recognition system\college_images\photo.jpeg")
        img9= img9.resize((220,220),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

       
        b1 = Button(bg_img, image= self.photoimg9,cursor = "hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1 = Button(bg_img, text = "Photos",cursor = "hand2",command=self.open_img,font =("times new roman",15,"bold"),bg = "dark blue",fg ="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #DEveloper button
        img10= Image.open(r"C:\Users\namra\Face recognition system\college_images\developer.jpeg")
        img10= img10.resize((220,220),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

       
        b1 = Button(bg_img, image= self.photoimg10,cursor = "hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1 = Button(bg_img, text = "Developer",cursor = "hand2",command=self.developer_data,font =("times new roman",15,"bold"),bg = "dark blue",fg ="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Exit button
        img11= Image.open(r"C:\Users\namra\Face recognition system\college_images\exit.jpeg")
        img11= img11.resize((220,220),Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

       
        b1 = Button(bg_img, image= self.photoimg11,cursor = "hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1 = Button(bg_img, text = "Exit",cursor = "hand2",command=self.iExit,font =("times new roman",15,"bold"),bg = "dark blue",fg ="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile(r"C:\Users\namra\Face recognition system\data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

     #========================functions buttons======================================

    def student(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


        

if __name__ == "__main__":
    print("✅ Starting the Face Recognition System...")  # Debug message
    root = Tk()
    root.state('zoomed')  # Open the window in fullscreen mode
    root.lift()
    root.focus_force()
    app = Face_Recognition_System(root)
    root.mainloop()
    print("✅ Window closed successfully.")  # Debug message after closing the window
