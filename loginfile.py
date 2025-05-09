from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
import mysql.connector
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from facerecognitionsystem import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\namra\Face recognition system\college_images\loginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#002B53")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\namra\Face recognition system\college_images\log1.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53",borderwidth=0)
        lb1img1.place(x=730,y=175, width=100,height=100)

        get_str = Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=95,y=100)

        
        #label1 
        username =lb1= Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=70,y=155)

        #entry1 
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        
        #label2 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=70,y=225)

        #entry2 
        self.txtpwd=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=40,y=250,width=270)

        #=======================Icon Image==========================

        img2=Image.open(r"C:\Users\namra\Face recognition system\college_images\log1.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lb1img2 = Label(image=self.photoimage2,bg="#002B53",borderwidth=0)
        lb1img2.place(x=650,y=320, width=25,height=25)

        img3=Image.open(r"C:\Users\namra\Face recognition system\college_images\log1.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lb1img3 = Label(image=self.photoimage3,bg="#002B53",borderwidth=0)
        lb1img3.place(x=650,y=395, width=25,height=25)

         # Creating Button Login
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=110,y=300,width=120,height=35)


        # Creating Button Registration
        loginbtn=Button(frame,text="New User Register",command=self.reg,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="#002B53",activeforeground="white",activebackground="black")
        loginbtn.place(x=15,y=350,width=160)


        # Creating Button Forget
        loginbtn=Button(frame,text="Forget Password",command=self.forget_pwd,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="#002B53",activeforeground="white",activebackground="black")
        loginbtn.place(x=10,y=370,width=160)

    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
            
        else:
            #messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(host="localhost",username="root",password="Namra2608@",database="facerecognitiondb")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM regteach WHERE email=%s and password=%s",(
                                                                            self.txtuser.get(),
                                                                            self.txtpwd.get()
                                                                         ))
            
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid username and pwd")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admins")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

   #=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.txt_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.txt_new_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn =mysql.connector.connect(host="localhost",username="root",password="Namra2608@",database="facerecognitiondb")
            mycursor = conn.cursor()
            query=("SELECT * FROM regteach WHERE email=%s and security_q=%s and security_a=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.txt_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("UPDATE regteach SET password=%s where email=%s")
                value=(self.txt_new_passw.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been reset, Please login with new Password!",parent=self.root2)
                self.root2.destroy()
                
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            
            conn = mysql.connector.connect(host="localhost",username="root",password="Namra2608@",database="facerecognitiondb")
            mycursor = conn.cursor()
            query=("SELECT * FROM regteach WHERE email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)

                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=50,y=80)

                self.combo_ssq = ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_ssq["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_ssq.place(x=50,y=110,width=250)
                self.combo_ssq.current(0)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=50,y=150)

                 #entry2 
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                 #label2 
                newpass =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                newpass.place(x=50,y=220)

                 #entry2 
                self.txt_new_passw=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_passw.place(x=50,y=250,width=250)

                loginbtn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=100,y=290)




class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

          # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cnum = StringVar()
        self.var_email = StringVar()
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()
        self.var_cpwd = StringVar()
        self.var_check = IntVar()

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\namra\Face recognition system\college_images\bgReg.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # left img
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\namra\Face recognition system\college_images\bird.jpeg")
        left_label = Label(self.root, image=self.bg1)
        left_label.place(x=50, y=100, width=470,height=550)

        # Main Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        title = Label(frame, text="REGISTER HERE", font=("times new roman", 30, "bold"), fg="#002B53", bg="White")
        title.place(x=20, y=20)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=50,y=100)

        #entry1 
        self.txt_fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname_entry.place(x=50,y=130,width=250)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=370,y=100)

        #entry2 
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        
        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=50,y=170)

        #entry1 
        self.txt_cnum=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txt_cnum.place(x=50,y=200,width=250)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=370,y=170)

        #entry2 
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=50,y=240)

        #Combo Box1
        self.combo_ssq = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_ssq["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_ssq.place(x=50,y=270,width=250)
        self.combo_ssq.current(0)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=370,y=240)

        #entry2 
        self.txt_security=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=50,y=310)

        #entry1 
        self.txt_pwd=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txt_pwd.place(x=50,y=340,width=250)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=370,y=310)

        #entry2 
        self.txt_cpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txt_cpwd.place(x=370,y=340,width=250)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),onvalue=1,offvalue=0,fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=50,y=380)


        # ================Creating Button Register
        img=Image.open(r"C:\Users\namra\OneDrive\Desktop\Face recognition system\college_images\register-button-png-18466.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)

        

        img1=Image.open(r"C:\Users\namra\OneDrive\Desktop\Face recognition system\college_images\Screenshot 2025-05-08 001029.png")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select":
            messagebox.showerror("Error", "All Fields are Required!")
        elif self.var_pwd.get()!=self.var_cpwd.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
           # messagebox.showerror("Success","Welcome friends")
            conn = mysql.connector.connect(host="localhost",username="root",password="Namra2608@",database="facerecognitiondb")
            my_cursor = conn.cursor()
            query=("SELECT * FROM regteach WHERE email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row !=None:
                messagebox.showerror("Error","user already exist, pleasw try another email")
            else:
                my_cursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_cnum.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_ssq.get(),
                                                                                        self.var_sa.get(),
                                                                                        self.var_pwd.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

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
    main()