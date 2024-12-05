import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


class App(tk.Tk):
    """Main application class."""
    def __init__(self):
        super().__init__()
        self.title("Productivity App")
        self.geometry("1024x768")

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
        views = ["Dashboard", "Calendar", "Tasks", "Goals", "Settings & Profile"]
        for view in views:
            btn = tk.Button(self, text=view, command=lambda v=view: master.show_view(v),
                            bg="#34495E", fg="white", font=("Arial", 14), pady=10)
            btn.pack(fill=tk.X, pady=2, padx=5)

        # Additional action buttons
        tk.Button(self, text="Refresh App", command=self.refresh_app, 
                  bg="#E67E22", fg="white", font=("Arial", 12)).pack(fill=tk.X, pady=5)
        tk.Button(self, text="Exit App", command=self.exit_app,
                  bg="#E74C3C", fg="white", font=("Arial", 12)).pack(fill=tk.X, pady=5)

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
            "Tasks": TaskView(self),
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
        super().__init__(master, bg="white")
        tk.Label(self, text="Dashboard", font=("Arial", 24, "bold")).pack(pady=20)

        # Buttons for dashboard actions
        tk.Button(self, text="Show Dashboard Summary", command=self.show_summary,
                  font=("Arial", 14), bg="#3498DB", fg="white").pack(pady=10)
        tk.Button(self, text="Open Today's Tasks", command=self.open_tasks,
                  font=("Arial", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def show_summary(self):
        """Method to simulate fetching dashboard summary."""
        messagebox.showinfo("Dashboard Summary", "Today's Tasks: 3\nUpcoming Events: 2")

    def open_tasks(self):
        """Method to simulate opening today's tasks."""
        messagebox.showinfo("Today's Tasks", "No tasks for today!")


class CalendarView(tk.Frame):
    """Calendar view."""
    def __init__(self, master):
        super().__init__(master, bg="white")
        tk.Label(self, text="Calendar", font=("Arial", 24, "bold")).pack(pady=20)

        # Input for calendar event
        self.title_input = tk.Entry(self, font=("Arial", 14))
        self.title_input.insert(0, "Event Title")
        self.title_input.pack(pady=5)

        self.date_picker = DateEntry(self, font=("Arial", 14))
        self.date_picker.pack(pady=5)

        self.description_input = tk.Text(self, height=5, font=("Arial", 14))
        self.description_input.insert(tk.END, "Event Description")
        self.description_input.pack(pady=5)

        tk.Button(self, text="Add Event", command=self.add_event,
                  font=("Arial", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def add_event(self):
        """Simulate adding an event."""
        title = self.title_input.get()
        date = self.date_picker.get_date()
        description = self.description_input.get("1.0", tk.END).strip()
        if title and description:
            messagebox.showinfo("Event Added", f"Title: {title}\nDate: {date}\nDescription: {description}")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")


class TaskView(tk.Frame):
    """Task view."""
    def __init__(self, master):
        super().__init__(master, bg="white")
        tk.Label(self, text="Tasks", font=("Arial", 24, "bold")).pack(pady=20)

        # Input fields for tasks
        self.title_input = tk.Entry(self, font=("Arial", 14))
        self.title_input.insert(0, "Task Title")
        self.title_input.pack(pady=5)

        self.description_input = tk.Text(self, height=5, font=("Arial", 14))
        self.description_input.insert(tk.END, "Task Description")
        self.description_input.pack(pady=5)

        self.priority_dropdown = ttk.Combobox(self, values=["High", "Medium", "Low"], font=("Arial", 14))
        self.priority_dropdown.set("Select Priority")
        self.priority_dropdown.pack(pady=5)

        self.due_date_picker = DateEntry(self, font=("Arial", 14))
        self.due_date_picker.pack(pady=5)

        tk.Button(self, text="Add Task", command=self.add_task,
                  font=("Arial", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def add_task(self):
        """Simulate adding a task."""
        title = self.title_input.get()
        description = self.description_input.get("1.0", tk.END).strip()
        priority = self.priority_dropdown.get()
        due_date = self.due_date_picker.get_date()
        if title and description and priority != "Select Priority":
            messagebox.showinfo("Task Added", f"Title: {title}\nPriority: {priority}\nDue: {due_date}")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")


class GoalView(tk.Frame):
    """Goal view."""
    def __init__(self, master):
        super().__init__(master, bg="white")
        tk.Label(self, text="Goals", font=("Arial", 24, "bold")).pack(pady=20)

        # Input fields for goals
        self.title_input = tk.Entry(self, font=("Arial", 14))
        self.title_input.insert(0, "Goal Title")
        self.title_input.pack(pady=5)

        self.description_input = tk.Text(self, height=5, font=("Arial", 14))
        self.description_input.insert(tk.END, "Goal Description")
        self.description_input.pack(pady=5)

        self.priority_dropdown = ttk.Combobox(self, values=["High", "Medium", "Low"], font=("Arial", 14))
        self.priority_dropdown.set("Select Priority")
        self.priority_dropdown.pack(pady=5)

        tk.Button(self, text="Add Goal", command=self.add_goal,
                  font=("Arial", 14), bg="#2ECC71", fg="white").pack(pady=10)

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
        super().__init__(master, bg="white")
        tk.Label(self, text="Settings & Profile", font=("Arial", 24, "bold")).pack(pady=20)

        # User profile input fields
        self.name_input = tk.Entry(self, font=("Arial", 14))
        self.name_input.insert(0, "Your Name")
        self.name_input.pack(pady=5)

        self.age_input = tk.Entry(self, font=("Arial", 14))
        self.age_input.insert(0, "Your Age")
        self.age_input.pack(pady=5)

        tk.Button(self, text="Save Profile", command=self.save_profile,
                  font=("Arial", 14), bg="#2ECC71", fg="white").pack(pady=10)

    def save_profile(self):
        """Simulate saving profile data."""
        name = self.name_input.get()
        age = self.age_input.get()
        if name and age.isdigit():
            messagebox.showinfo("Profile Saved", f"Name: {name}\nAge: {age}")
        else:
            messagebox.showwarning("Input Error", "Please provide valid name and age!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
