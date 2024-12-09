import tkinter as tk
from tkinter import ttk
from classes.user import User

class Settings:
    def __init__(self, root, user_email):
        self.root = root
        self.user = User.get_user_by_email(user_email)
        self.create_ui()

    def create_ui(self):
        self.root.title("Settings")

        # User Details
        details_frame = tk.Frame(self.root)
        details_frame.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(details_frame, text="Edit User Details:").grid(row=0, column=0, columnspan=2, sticky="w")
        tk.Label(details_frame, text="Real Name:").grid(row=1, column=0, sticky="w")
        self.real_name_entry = tk.Entry(details_frame)
        self.real_name_entry.insert(0, self.user.real_name)
        self.real_name_entry.grid(row=1, column=1, sticky="w")
        tk.Label(details_frame, text="Age:").grid(row=2, column=0, sticky="w")
        self.age_entry = tk.Entry(details_frame)
        self.age_entry.insert(0, self.user.age)
        self.age_entry.grid(row=2, column=1, sticky="w")
        tk.Label(details_frame, text="Education Level:").grid(row=3, column=0, sticky="w")
        self.education_lvl_entry = tk.Entry(details_frame)
        self.education_lvl_entry.insert(0, self.user.education_lvl)
        self.education_lvl_entry.grid(row=3, column=1, sticky="w")
        tk.Label(details_frame, text="Email:").grid(row=4, column=0, sticky="w")
        self.email_entry = tk.Entry(details_frame)
        self.email_entry.insert(0, self.user.email)
        self.email_entry.grid(row=4, column=1, sticky="w")
        tk.Label(details_frame, text="Password:").grid(row=5, column=0, sticky="w")
        self.password_entry = tk.Entry(details_frame, show="*")
        self.password_entry.insert(0, self.user.password)
        self.password_entry.grid(row=5, column=1, sticky="w")
        tk.Label(details_frame, text="Field of Education:").grid(row=6, column=0, sticky="w")
        self.field_of_education_entry = tk.Entry(details_frame)
        self.field_of_education_entry.insert(0, self.user.field_of_education)
        self.field_of_education_entry.grid(row=6, column=1, sticky="w")
        tk.Label(details_frame, text="Hobbies:").grid(row=7, column=0, sticky="w")
        self.hobbies_entry = tk.Entry(details_frame)
        self.hobbies_entry.insert(0, self.user.hobbies)
        self.hobbies_entry.grid(row=7, column=1, sticky="w")
        tk.Label(details_frame, text="School Attending:").grid(row=8, column=0, sticky="w")
        self.school_attending_entry = tk.Entry(details_frame)
        self.school_attending_entry.insert(0, self.user.school_attending)
        self.school_attending_entry.grid(row=8, column=1, sticky="w")
        tk.Label(details_frame, text="Likes:").grid(row=9, column=0, sticky="w")
        self.likes_entry = tk.Entry(details_frame)
        self.likes_entry.insert(0, self.user.likes)
        self.likes_entry.grid(row=9, column=1, sticky="w")
        tk.Label(details_frame, text="Dislikes:").grid(row=10, column=0, sticky="w")
        self.dislikes_entry = tk.Entry(details_frame)
        self.dislikes_entry.insert(0, self.user.dislikes)
        self.dislikes_entry.grid(row=10, column=1, sticky="w")
        tk.Button(details_frame, text="Save Changes", command=self.save_changes).grid(row=11, column=0, columnspan=2, pady=10)

    def save_changes(self):
        self.user.real_name = self.real_name_entry.get()
        self.user.age = self.age_entry.get()
        self.user.education_lvl = self.education_lvl_entry.get()
        self.user.email = self.email_entry.get()
        self.user.password = self.password_entry.get()
        self.user.field_of_education = self.field_of_education_entry.get()
        self.user.hobbies = self.hobbies_entry.get()
        self.user.school_attending = self.school_attending_entry.get()
        self.user.likes = self.likes_entry.get()
        self.user.dislikes = self.dislikes_entry.get()
        self.user.save()

if __name__ == "__main__":
    root = tk.Tk()
    settings = Settings(root, "user@example.com")
    root.mainloop()
