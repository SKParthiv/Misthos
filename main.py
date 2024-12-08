from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import tkinter as tk
from tkinter import messagebox
import json
from view.game_UI import main as start_story_mode_game
from view.UI import DashboardView
from view.UI import CalendarView
from view.UI import QuestView
from view.UI import GoalView
from view.UI import SettingsProfileView
from models.models import User

def google_login():
    """Authenticate user with Google account."""
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', 
        scopes=['https://www.googleapis.com/auth/userinfo.profile']
    )
    credentials = flow.run_local_server(port=0)
    service = build('oauth2', 'v2', credentials=credentials)
    user_info = service.userinfo().get().execute()
    return user_info

class LoginScreen(tk.Frame):
    """Login screen for the application."""
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Login", font=("Courier", 24, "bold")).pack(pady=20)
        tk.Button(self, text="Login with Google", command=self.google_login, font=("Courier", 14)).pack(pady=10)

    def google_login(self):
        user_info = google_login()
        self.master.user_info = user_info
        self.master.show_view("Register")

class RegisterScreen(tk.Frame):
    """Register screen for the application."""
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Register", font=("Courier", 24, "bold")).pack(pady=20)
        self.name_input = tk.Entry(self, font=("Courier", 14))
        self.name_input.insert(0, "Your Name")
        self.name_input.pack(pady=5)
        self.age_input = tk.Entry(self, font=("Courier", 14))
        self.age_input.insert(0, "Your Age")
        self.age_input.pack(pady=5)
        self.job_designation_input = tk.Entry(self, font=("Courier", 14))
        self.job_designation_input.insert(0, "Job Designation")
        self.job_designation_input.pack(pady=5)
        self.preferences_input = tk.Text(self, height=5, font=("Courier", 14))
        self.preferences_input.insert(tk.END, "Preferences (JSON format)")
        self.preferences_input.pack(pady=5)
        tk.Button(self, text="Register", command=self.register, font=("Courier", 14)).pack(pady=10)

    def register(self):
        name = self.name_input.get()
        age = self.age_input.get()
        job_designation = self.job_designation_input.get()
        preferences = self.preferences_input.get("1.0", tk.END).strip()
        if name and age.isdigit() and job_designation and preferences:
            try:
                preferences_dict = json.loads(preferences)
                user = User(name, int(age), preferences_dict, job_designation)
                user.save()
                self.master.user = user
                self.master.show_view("Dashboard")
            except json.JSONDecodeError:
                messagebox.showwarning("Input Error", "Preferences must be valid JSON!")
        else:
            messagebox.showwarning("Input Error", "Please provide valid name, age, job designation, and preferences!")

class App(tk.Tk):
    """Main application class."""
    def __init__(self):
        super().__init__()
        self.title("Pixel Task Manager")
        self.geometry("1024x768")
        self.configure(bg="#1E1E1E")
        self.user_info = None
        self.user = None

        # Initialize views
        self.views = {
            "Login": LoginScreen(self),
            "Register": RegisterScreen(self),
            "Dashboard": DashboardView(self),
            "Calendar": CalendarView(self),
            "Quests": QuestView(self),
            "Goals": GoalView(self),
            "Settings & Profile": SettingsProfileView(self)
        }

        # Display default view (Login)
        self.show_view("Login")

    def show_view(self, view_name):
        """Switch to a specific view."""
        for name, view in self.views.items():
            if name == view_name:
                view.pack(fill=tk.BOTH, expand=True)
            else:
                view.pack_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()
    start_story_mode_game()
