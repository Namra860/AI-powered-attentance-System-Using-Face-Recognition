from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"c:\Users\namra\Face recognition system\college_images\facial-recognition-banner.jpg.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"C:\Users\namra\Face recognition system\college_images\f_det.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="dark green", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)

    # ====================== Attendance ====================
    
    
    def mark_attendance(self, i, r, n, d):
        today = datetime.now().strftime("%d/%m/%Y")
        found = False

        with open("namrata.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            for line in myDataList:
                data = line.strip().split(",")
                if len(data) > 5 and data[0] == i and data[5] == today:
                    found = True
                    break

            if not found:
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{today},present")

    # ===================== Face Recognition ====================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Namra2608@", database="facerecognitiondb")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Student_id, Roll, Name, Department FROM student WHERE Student_id=%s", (id,))
                result = my_cursor.fetchone()
                conn.close()

                if result:
                    i, r, n, d = [str(item) if item else "Unknown" for item in result]
                else:
                    i, r, n, d = "Unknown", "Unknown", "Unknown", "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    # Store unknown faces if not already recorded
                    with open(r"namrata.csv", "r+", newline="\n") as f:
                        unknown_faces = f.readlines()
                        already_marked = False
                        for line in unknown_faces:
                            if "Unknown" in line and datetime.now().strftime("%d/%m/%Y") in line:
                                already_marked = True
                                break
                        if not already_marked:
                            now = datetime.now()
                            d1 = now.strftime("%d/%m/%Y")
                            dtString = now.strftime("%H:%M:%S")
                            f.writelines(f"\nUnknown,Unknown,Unknown,Unknown,{dtString},{d1},present")

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("✅ Starting the Face Recognition System...")
    root = Tk()
    root.state('zoomed')
    root.lift()
    root.focus_force()
    app = Face_Recognition(root)
    root.mainloop()
    print("✅ Window closed successfully.")
