from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # Bg Image
        self.bg = ImageTk.PhotoImage(file="b.png")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
        # Left Image
        self.left = ImageTk.PhotoImage(file="c3.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # ----REGISTER FRAME
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=480, y=100, width=700, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 25, "bold"), bg="white", fg="green").place(x=50, y=30)

        email = Label(login_frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.text_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.text_email.place(x=50, y=130, width=300, height=35)

        password = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.text_password = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.text_password.place(x=50, y=200, width=300, height=35)

        btn_reg = Button(login_frame, text="Register New Account?", command=self.register_window, font=("times new roman", 15), bg="white", bd=0, fg="red").place(x=50, y=250)
        self.btn_img = ImageTk.PhotoImage(file="l2.png")
        btn_log = Button(login_frame, image=self.btn_img, bd=0, cursor="hand2", command=self.login_data).place(x=50, y=310)

    def clear(self):
        self.text_email.delete(0, END),
        self.text_password.delete(0, END)

    def register_window(self):
        self.root.destroy()
        import register

    def login_data(self):
        if self.text_email.get() == "" or self.text_password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="users")
                cur = con.cursor()
                cur.execute("select * from user where email=%s and password=%s", (self.text_email.get(), self.text_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Email & Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to : {str(es)}", parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()
