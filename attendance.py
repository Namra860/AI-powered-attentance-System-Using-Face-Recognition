from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
import csv

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ====================Variables====================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ===============Images=============================
        img = Image.open("college_images/banner.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        img1 = Image.open("college_images/tree.jpeg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        img3 = Image.open("college_images/bg2.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # =================Left Frame=======================
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("college_images/scenery.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        # ============Labels and Entries===================
        Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 13, "bold")).grid(row=0, column=1, padx=10, pady=5)

        Label(left_inside_frame, text="Roll:", bg="white", font=("comicsansns", 11, "bold")).grid(row=0, column=2, padx=4, pady=8)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_roll, font=("comicsansns", 13, "bold")).grid(row=0, column=3, pady=8)

        Label(left_inside_frame, text="Name:", bg="white", font=("comicsansns", 13, "bold")).grid(row=1, column=0)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_name, font=("comicsansns", 13, "bold")).grid(row=1, column=1, pady=8)

        Label(left_inside_frame, text="Department:", bg="white", font=("comicsansns", 13, "bold")).grid(row=1, column=2)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_dep, font=("comicsansns", 13, "bold")).grid(row=1, column=3, pady=8)

        Label(left_inside_frame, text="Time:", bg="white", font=("comicsansns", 13, "bold")).grid(row=2, column=0)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_time, font=("comicsansns", 13, "bold")).grid(row=2, column=1, pady=8)

        Label(left_inside_frame, text="Date:", bg="white", font=("comicsansns", 13, "bold")).grid(row=2, column=2)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_date, font=("comicsansns", 13, "bold")).grid(row=2, column=3, pady=8)

        Label(left_inside_frame, text="Attendance Status", bg="white", font=("comicsansns", 13, "bold")).grid(row=3, column=0)
        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font=("comicsansns", 13, "bold"), state='readonly')
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)

        btn_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=300, width=715, height=35)

        Button(btn_frame, text="Import CSV", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # =============Right Frame=====================
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=700, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        for col in ("id", "roll", "name", "department", "time", "date", "attendance"):
            self.AttendanceReportTable.heading(col, text=col.title())
            self.AttendanceReportTable.column(col, width=100)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if fln:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetch_data(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root, defaultextension=".csv")
            with open(fln, mode='w', newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
            messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content.get("values", [])
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    app = Attendance(root)
    root.mainloop()
