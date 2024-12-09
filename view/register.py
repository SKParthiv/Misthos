import tkinter as tk
from tkinter import messagebox
from classes.user import User, Player
from view.login import Login

class Register:
    def __init__(self, root, show_dashboard, show_initial_screen):
        self.root = root
        self.show_dashboard = show_dashboard
        self.show_initial_screen = show_initial_screen
        self.create_ui()

    def create_ui(self):
        self.root.title("Register")

        tk.Label(self.root, text="Real Name:").grid(row=0, column=0, sticky="w")
        self.real_name_entry = tk.Entry(self.root)
        self.real_name_entry.grid(row=0, column=1, sticky="w")
        tk.Label(self.root, text="Age:").grid(row=1, column=0, sticky="w")
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1, sticky="w")
        tk.Label(self.root, text="Education Level:").grid(row=2, column=0, sticky="w")
        self.education_lvl_entry = tk.Entry(self.root)
        self.education_lvl_entry.grid(row=2, column=1, sticky="w")
        tk.Label(self.root, text="Email:").grid(row=3, column=0, sticky="w")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=3, column=1, sticky="w")
        tk.Label(self.root, text="Password:").grid(row=4, column=0, sticky="w")
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=4, column=1, sticky="w")
        tk.Label(self.root, text="Field of Education:").grid(row=5, column=0, sticky="w")
        self.field_of_education_entry = tk.Entry(self.root)
        self.field_of_education_entry.grid(row=5, column=1, sticky="w")
        tk.Label(self.root, text="Hobbies:").grid(row=6, column=0, sticky="w")
        self.hobbies_entry = tk.Entry(self.root)
        self.hobbies_entry.grid(row=6, column=1, sticky="w")
        tk.Label(self.root, text="School Attending:").grid(row=7, column=0, sticky="w")
        self.school_attending_entry = tk.Entry(self.root)
        self.school_attending_entry.grid(row=7, column=1, sticky="w")
        tk.Label(self.root, text="Likes:").grid(row=8, column=0, sticky="w")
        self.likes_entry = tk.Entry(self.root)
        self.likes_entry.grid(row=8, column=1, sticky="w")
        tk.Label(self.root, text="Dislikes:").grid(row=9, column=0, sticky="w")
        self.dislikes_entry = tk.Entry(self.root)
        self.dislikes_entry.grid(row=9, column=1, sticky="w")
        tk.Label(self.root, text="Player Name:").grid(row=10, column=0, sticky="w")
        self.player_name_entry = tk.Entry(self.root)
        self.player_name_entry.grid(row=10, column=1, sticky="w")
        tk.Button(self.root, text="Register", command=self.register).grid(row=11, column=0, columnspan=2, pady=10)

    def register(self):
        real_name = self.real_name_entry.get()
        age = self.age_entry.get()
        education_lvl = self.education_lvl_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        field_of_education = self.field_of_education_entry.get()
        hobbies = self.hobbies_entry.get()
        school_attending = self.school_attending_entry.get()
        likes = self.likes_entry.get()
        dislikes = self.dislikes_entry.get()
        player_name = self.player_name_entry.get()

        # Create a Player object with default stats
        player = Player(player_name, strength=5, agility=5, stamina=5, vitality=5, intelligence=5, lvl=1, exp=0)

        user = User(real_name, age, education_lvl, email, password, field_of_education, hobbies, school_attending, likes, dislikes, player)
        user.create_table()
        user.save()
        messagebox.showinfo("Register", "Registration successful!")
        self.root.destroy()
        root = tk.Tk()
        Login(root, self.show_dashboard, self.show_initial_screen)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    register = Register(root)
    root.mainloop()
