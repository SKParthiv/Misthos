import tkinter as tk
from view.login import Login
from view.dashboard import Dashboard
from view.settings import Settings
from view.quest_view import QuestView
from classes.user import User
from game.gameUI import Game
from view.register import Register
from view.login import Login

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Misthos")
        self.user_email = None
        self.show_initial_screen()

    def show_initial_screen(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Welcome to Misthos", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(frame, text="Login", command=self.show_login).pack(pady=10)
        tk.Button(frame, text="Register", command=self.show_register).pack(pady=10)

    def show_login(self):
        self.clear_frame()
        Login(self.root, self.show_dashboard, self.show_initial_screen)

    def show_register(self):
        self.clear_frame()
        Register(self.root, self.show_dashboard, self.show_initial_screen)

    def show_dashboard(self, user_email):
        self.user_email = user_email
        self.clear_frame()
        self.create_sidebar()
        Dashboard(self.root, user_email)

    def show_settings(self):
        self.clear_frame()
        self.create_sidebar()
        Settings(self.root, self.user_email)

    def show_quest_view(self):
        self.clear_frame()
        self.create_sidebar()
        QuestView(self.root, self.user_email)

    def logout(self):
        self.user_email = None
        self.show_login()

    def delete_user(self):
        if self.user_email:
            User.delete_user(self.user_email)
            self.logout()

    def create_sidebar(self):
        sidebar = tk.Frame(self.root, width=200, bg='gray')
        sidebar.pack(side='left', fill='y')

        tk.Button(sidebar, text="Dashboard", command=lambda: self.show_dashboard(self.user_email)).pack(fill='x')
        tk.Button(sidebar, text="Quests", command=self.show_quest_view).pack(fill='x')
        tk.Button(sidebar, text="Settings", command=self.show_settings).pack(fill='x')
        tk.Button(sidebar, text="Logout", command=self.logout).pack(fill='x')
        tk.Button(sidebar, text="Delete User", command=self.delete_user).pack(fill='x')
        tk.Button(sidebar, text="Play Game", command=self.open_game_ui).pack(fill='x')

    def open_game_ui(self):
        self.clear_frame()
        Game()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()