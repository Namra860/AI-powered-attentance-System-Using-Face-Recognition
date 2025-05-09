from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re
import hashlib

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
                messagebox.showerror("Error","user already exist, please try another email")
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





if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
