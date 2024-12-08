import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry, Calendar
from PIL import Image, ImageTk
import json

class App(tk.Tk):
    """Main application class."""
    def __init__(self):
        super().__init__()
        self.title("Pixel Task Manager")
        self.geometry("1024x768")
        self.configure(bg="#1E1E1E")

        # Initialize views
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.main_frame = MainFrame(self)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Display default view (Dashboard)
        self.show_view("Dashboard")

    def show_view(self, view_name):
        """Switch to a specific view."""
        self.main_frame.switch_view(view_name)

class Sidebar(tk.Frame):
    """Sidebar for navigation."""
    def __init__(self, master):
        super().__init__(master, bg="#2C3E50", width=200)

        # Button definitions for navigation
        views = ["Dashboard", "Calendar", "Quests", "Goals", "Settings & Profile"]
        for view in views:
            btn = tk.Button(self, text=view, command=lambda v=view: master.show_view(v),
                            bg="#34495E", fg="white", font=("Courier", 14), pady=10)
            btn.pack(fill=tk.X, pady=2, padx=5)

        # Additional action buttons
        tk.Button(self, text="Refresh App", command=self.refresh_app, 
                  bg="#E67E22", fg="white", font=("Courier", 12)).pack(fill=tk.X, pady=5)
        tk.Button(self, text="Exit App", command=self.exit_app,
                  bg="#E74C3C", fg="white", font=("Courier", 12)).pack(fill=tk.X, pady=5)

    def refresh_app(self):
        """Simulate refreshing the application."""
        messagebox.showinfo("Refresh", "Application refreshed successfully!")

    def exit_app(self):
        """Exit the application."""
        self.master.destroy()

class MainFrame(tk.Frame):
    """Main frame for displaying different views."""
    def __init__(self, master):
        super().__init__(master, bg="#ECF0F1")
        self.views = {
            "Dashboard": DashboardView(self),
            "Calendar": CalendarView(self),
            "Quests": QuestView(self),
            "Goals": GoalView(self),
            "Settings & Profile": SettingsProfileView(self)
        }

        # Initialize all views as hidden
        for view in self.views.values():
            view.pack_forget()

    def switch_view(self, view_name):
        """Display the selected view."""
        for name, view in self.views.items():
            if name == view_name:
                view.pack(fill=tk.BOTH, expand=True)
            else:
                view.pack_forget()

class DashboardView(tk.Frame):
    """Dashboard view."""
    def __init__(self, master):
        super().__init__(master, bg="#1E1E1E")
        tk.Label(self, text="Dashboard", font=("Courier", 24, "bold"), fg="white", bg="#1E1E1E").pack(pady=20)

        # Display player stats
        self.stats_frame = tk.Frame(self, bg="#1E1E1E")
        self.stats_frame.pack(pady=10)

        self.level_label = tk.Label(self.stats_frame, text="Level: 1", font=("Courier", 14), fg="white", bg="#1E1E1E")
        self.level_label.grid(row=0, column=0, padx=10)

        self.exp_label = tk.Label(self.stats_frame, text="EXP: 0/100", font=("Courier", 14), fg="white", bg="#1E1E1E")
        self.exp_label.grid(row=0, column=1, padx=10)

        self.intelligence_label = tk.Label(self.stats_frame, text="Intelligence: 10", font=("Courier", 14), fg="white", bg="#1E1E1E")
        self.intelligence_label.grid(row=1, column=0, padx=10)

        self.strength_label = tk.Label(self.stats_frame, text="Strength: 10", font=("Courier", 14), fg="white", bg="#1E1E1E")
        self.strength_label.grid(row=1, column=1, padx=10)

        self.agility_label = tk.Label(self.stats_frame, text="Agility: 10", font=("Courier", 14), fg="white", bg="#1E1E1E")
        self.agility_label.grid(row=2, column=0, padx=10)

        self.stamina_label = tk.Label(self.stats_frame, text="Stamina: 10", font=("Courier", 14), fg="white", bg="#1E1E1E")
        self.stamina_label.grid(row=2, column=1, padx=10)

        self.health_label = tk.Label(self.stats_frame, text="Health: 100", font=("Courier", 14), fg="white", bg="#1E1E1E")
        self.health_label.grid(row=3, column=0, padx=10)

        # Experience bar
        self.exp_bar = ttk.Progressbar(self.stats_frame, orient="horizontal", length=200, mode="determinate")
        self.exp_bar.grid(row=3, column=1, padx=10)
        self.exp_bar["value"] = 0
        self.exp_bar["maximum"] = 100

        # Buttons for dashboard actions
        tk.Button(self, text="Show Dashboard Summary", command=self.show_summary,
                  font=("Courier", 14), bg="#3498DB", fg="white").pack(pady=10)
        tk.Button(self, text="Open Today's Tasks", command=self.open_tasks,
                  font=("Courier", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def show_summary(self):
        """Method to simulate fetching dashboard summary."""
        messagebox.showinfo("Dashboard Summary", "Today's Tasks: 3\nUpcoming Events: 2")

    def open_tasks(self):
        """Method to simulate opening today's tasks."""
        messagebox.showinfo("Today's Tasks", "No tasks for today!")

    def update_stats(self, player):
        """Update the displayed stats based on the player object."""
        self.level_label.config(text=f"Level: {player.level}")
        self.exp_label.config(text=f"EXP: {player.exp}/{player.level * 100}")
        self.intelligence_label.config(text=f"Intelligence: {player.intelligence}")
        self.strength_label.config(text=f"Strength: {player.strength}")
        self.agility_label.config(text=f"Agility: {player.agility}")
        self.stamina_label.config(text=f"Stamina: {player.stamina}")
        self.health_label.config(text=f"Health: {player.health}")
        self.exp_bar["value"] = player.exp
        self.exp_bar["maximum"] = player.level * 100

class CalendarView(tk.Frame):
    """Calendar view."""
    def __init__(self, master):
        super().__init__(master, bg="#1E1E1E")
        tk.Label(self, text="Calendar", font=("Courier", 24, "bold"), fg="white", bg="#1E1E1E").pack(pady=20)
        self.calendar = Calendar(self, selectmode='day', year=2023, month=10, day=5)
        self.calendar.pack(pady=20)

class QuestView(tk.Frame):
    """Quest view."""
    def __init__(self, master):
        super().__init__(master, bg="#1E1E1E")
        tk.Label(self, text="Quests", font=("Courier", 24, "bold"), fg="white", bg="#1E1E1E").pack(pady=20)

        # Input fields for quests
        self.title_input = tk.Entry(self, font=("Courier", 14))
        self.title_input.insert(0, "Quest Title")
        self.title_input.pack(pady=5)

        self.description_input = tk.Text(self, height=5, font=("Courier", 14))
        self.description_input.insert(tk.END, "Quest Description")
        self.description_input.pack(pady=5)

        self.priority_dropdown = ttk.Combobox(self, values=["High", "Medium", "Low"], font=("Courier", 14))
        self.priority_dropdown.set("Select Priority")
        self.priority_dropdown.pack(pady=5)

        self.due_date_picker = DateEntry(self, font=("Courier", 14))
        self.due_date_picker.pack(pady=5)

        tk.Button(self, text="Add Quest", command=self.add_quest,
                  font=("Courier", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def add_quest(self):
        """Simulate adding a quest."""
        title = self.title_input.get()
        description = self.description_input.get("1.0", tk.END).strip()
        priority = self.priority_dropdown.get()
        due_date = self.due_date_picker.get_date()
        if title and description and priority != "Select Priority":
            quest = Quest(self.master.user.id, title, description, due_date.isoformat(), priority, "General")
            quest.save()
            messagebox.showinfo("Quest Added", f"Title: {title}\nPriority: {priority}\nDue: {due_date}\nDifficulty: {quest.difficulty}\nRewards: {quest.rewards}")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")

class GoalView(tk.Frame):
    """Goal view."""
    def __init__(self, master):
        super().__init__(master, bg="#1E1E1E")
        tk.Label(self, text="Goals", font=("Courier", 24, "bold"), fg="white", bg="#1E1E1E").pack(pady=20)

        # Input fields for goals
        self.title_input = tk.Entry(self, font=("Courier", 14))
        self.title_input.insert(0, "Goal Title")
        self.title_input.pack(pady=5)

        self.description_input = tk.Text(self, height=5, font=("Courier", 14))
        self.description_input.insert(tk.END, "Goal Description")
        self.description_input.pack(pady=5)

        self.priority_dropdown = ttk.Combobox(self, values=["High", "Medium", "Low"], font=("Courier", 14))
        self.priority_dropdown.set("Select Priority")
        self.priority_dropdown.pack(pady=5)

        tk.Button(self, text="Add Goal", command=self.add_goal,
                  font=("Courier", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def add_goal(self):
        """Simulate adding a goal."""
        title = self.title_input.get()
        description = self.description_input.get("1.0", tk.END).strip()
        priority = self.priority_dropdown.get()
        if title and description and priority != "Select Priority":
            messagebox.showinfo("Goal Added", f"Title: {title}\nPriority: {priority}")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")

class SettingsProfileView(tk.Frame):
    """Settings and user profile view."""
    def __init__(self, master):
        super().__init__(master, bg="#1E1E1E")
        tk.Label(self, text="Settings & Profile", font=("Courier", 24, "bold"), fg="white", bg="#1E1E1E").pack(pady=20)

        # User profile input fields
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

        tk.Button(self, text="Save Profile", command=self.save_profile,
                  font=("Courier", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def save_profile(self):
        """Simulate saving profile data."""
        name = self.name_input.get()
        age = self.age_input.get()
        job_designation = self.job_designation_input.get()
        preferences = self.preferences_input.get("1.0", tk.END).strip()
        if name and age.isdigit() and job_designation and preferences:
            try:
                preferences_dict = json.loads(preferences)
                # Assuming `user` is an instance of the User class
                user.update_info(name=name, age=int(age))
                user.update_job_designation(job_designation)
                user.update_preferences(preferences_dict)
                messagebox.showinfo("Profile Saved", f"Name: {name}\nAge: {age}\nJob: {job_designation}")
            except json.JSONDecodeError:
                messagebox.showwarning("Input Error", "Preferences must be valid JSON!")
        else:
            messagebox.showwarning("Input Error", "Please provide valid name, age, job designation, and preferences!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
