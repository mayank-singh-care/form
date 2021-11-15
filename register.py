from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk
import pymysql
import re


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.l, self.u, self.p, self.d = 0, 0, 0, 0
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # Bg Image
        self.bg = ImageTk.PhotoImage(file="b.png")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
        # Left Image
        self.left = ImageTk.PhotoImage(file="c1.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # ----REGISTER FRAME
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # ------Row1
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.text_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.text_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_lname.place(x=370, y=130, width=250)

        # -----Row2
        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.text_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.text_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_email.place(x=370, y=200, width=250)

        # ------Row3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmb_quest['values'] = ("Select","Your First Pet Name","Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.text_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_answer.place(x=370, y=270, width=250)

        # ------Row4
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.text_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.text_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_cpassword.place(x=370, y=340, width=250)

        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=50, y=380)
        self.btn_img = ImageTk.PhotoImage(file="r2.png")
        btn_reg = Button(frame1, image=self.btn_img, bd=0, cursor="hand2",command=self.register_data).place(x=50, y=420)
        btn_login = Button(self.root, text="Sign In",command=self.login_window, font=("times new roman", 20), bd=0, cursor="hand2").place(x=190, y=535, width=180)

    def login_window(self):
        self.root.destroy()
        import login

    def clear(self):
        self.text_fname.delete(0, END),
        self.text_lname.delete(0, END),
        self.text_contact.delete(0, END),
        self.text_email.delete(0, END),
        self.cmb_quest.current(0),
        self.text_answer.delete(0, END),
        self.text_password.delete(0, END)

    def check(self, s):
        self.l, self.u, self.p, self.d = 0, 0, 0, 0
        if len(s) >= 8:
            for i in s:
                if i.islower():
                    self.l += 1
                if i.isupper():
                    self.u += 1
                if i.isdigit():
                    self.d += 1
                if i == '@' or i == '$' or i == '_':
                    self.p += 1
        if self.l >= 1 and self.u >= 1 and self.p >= 1 and self.d >= 1 and self.l + self.p + self.u + self.d == len(s):
            return True
        else:
            return False

    def register_data(self):
        if self.text_fname.get() == "" or self.text_contact.get() == "" or self.text_email.get() == "" or self.cmb_quest.get() == "Select" or self.text_answer.get() == "" or self.text_password.get() == "" or self.text_cpassword.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.text_password.get() != self.text_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif not self.check(self.text_password.get()):
            messagebox.showerror("Error", "Invalid Password, must follow Minimum 8 characters.The alphabets must be between [a-z] At least one alphabet should be of Upper Case [A-Z] At least 1 number or digit between [0-9]. At least 1 character from [ _ or @ or $ ].", parent=self.root)
        elif re.fullmatch(self.regex, self.text_email.get()) == None:
            messagebox.showerror("Error", "Invalid Email", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms & Conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="users")
                cur = con.cursor()
                cur.execute("select * from user where email=%s", self.text_email.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "User Already Exist, Please Try With Another Email", parent=self.root)
                else:
                    cur.execute("insert into user (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.text_fname.get(),
                                 self.text_lname.get(),
                                 self.text_contact.get(),
                                 self.text_email.get(),
                                 self.cmb_quest.get(),
                                 self.text_answer.get(),
                                 self.text_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to : {str(es)}", parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()
