import tkinter as tk
from tkinter import messagebox
from classes.user import User
from view.register import Register

class Login:
    def __init__(self, root, show_dashboard_callback):
        self.root = root
        self.show_dashboard_callback = show_dashboard_callback
        self.create_ui()

    def create_ui(self):
        self.root.title("Login")

        tk.Label(self.root, text="Email:").grid(row=0, column=0, sticky="w")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=0, column=1, sticky="w")
        tk.Label(self.root, text="Password:").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1, sticky="w")
        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Register", command=self.register).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        user = User.get_user_by_email(email)
        if user and user.password == password:
            messagebox.showinfo("Login", "Login successful!")
            self.show_dashboard_callback(email)
        else:
            messagebox.showerror("Login", "Invalid email or password")

    def register(self):
        self.root.destroy()
        root = tk.Tk()
        Register(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    login = Login(root, lambda email: print(f"Logged in as {email}"))
    root.mainloop()
