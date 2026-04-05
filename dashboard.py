from tkinter import *
from tkinter import Label
from tkinter import messagebox
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from PIL import Image, ImageTk
import os
import math
from tkinter import  ttk
from tkinter import font
from tkinter import ttk
from PIL import  ImageDraw
from datetime import*
import pymysql
import sqlite3
import time


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # --icons--
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # --title--
        title = Label(self.root, text="Student Result Management System",padx=10,compound=LEFT,image= self.logo_dash ,font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)
        
        #--menu--
        M_Frame = LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10, y=70, relwidth=0.99, height=80)

        btn_course=Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_course).place(x=20, y=5, width=130, height=40)
        btn_student=Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_student).place(x=240, y=5, width=130, height=40)
        btn_result=Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_result).place(x=460, y=5, width=130, height=40)
        btn_view=Button(M_Frame, text="View Performance", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_report).place(x=680, y=5, width=170, height=40)
        btn_logout=Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2", command=self.logout).place(x=900, y=5, width=130, height=40)
        btn_exit=Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2", command=self.exit_).place(x=1120, y=5, width=130, height=40)

        #--content_window--
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((900, 280), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img,bd=0)
        self.lbl_bg.place(x=370, y=180, width=900, height=280)

        #--Update_Details--
        
        
        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]",font=("goudy old style", 15),bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=490, width=255, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]",font=("goudy old style", 15),bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=490, width=255, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]",font=("goudy old style", 15),bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=490, width=255, height=100)


        self.lbl=Label(self.root, text="\nWebCode Clock" ,font=("Book Antiqua", 25, "bold"),fg="white",compound=BOTTOM,bg="#081923", bd=0)
        self.lbl.place(x=10, y=150, height=450, width=350)
        self.working()
        
        #--Footer--
        footer = Label(self.root, text="🏫 SRMS-Student Result Management System\nContact Us for any Technical Issues: 📞 +91 9336789190",font=("goudy old style", 12), bg="#003366", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[ {str(len(cr))} ]")
            
            cur.execute("select * from student")
            st=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[ {str(len(st))} ]")
            

            cur.execute("select * from result")
            rs=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[ {str(len(rs))} ]")

            self.lbl_course.after(200, self.update_details)
           
            
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def clock_image(self, hr, min_, sec_):
        clock=Image.new("RGB", (400, 400), (8, 25, 35))
        draw=ImageDraw.Draw(clock)

        # Ensure this folder and file exist
        bg=Image.open("images/c.png")
        bg=bg.resize((300, 300), Image.LANCZOS)
        clock.paste(bg, (50,50))
        
        origin=200,200
        draw.line((origin, 200+50*math.sin(math.radians(hr)), 200-50*math.cos(math.radians(hr))), fill="#DF005E", width=4)
        draw.line((origin, 200+80*math.sin(math.radians(min_)), 200-80*math.cos(math.radians(min_))), fill="white", width=3)
        draw.line((origin, 200+100*math.sin(math.radians(sec_)), 200-100*math.cos(math.radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def working(self):
        
        if not self.lbl.winfo_exists():
            return

        h= datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        
        self.clock_image(hr, min_, sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        
        # 2. Check again before updating and scheduling next loop
        if self.lbl.winfo_exists():
            self.lbl.config(image=self.img)
            self.lbl.after(200, self.working)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)  

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win) 

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)    

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)    

    def logout(self):
        op= messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root) 
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op= messagebox.askyesno("Confirm", "Do you really want to exit?", parent=self.root) 
        if op==True:
            self.root.destroy()
           
        

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
