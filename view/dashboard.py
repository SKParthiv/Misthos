
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime
from classes.user import User
from classes.quest import Quest

class Dashboard:
    def __init__(self, root, user_email):
        self.root = root
        self.user = User.get_user_by_email(user_email)
        self.create_ui()

    def create_ui(self):
        self.root.title("Dashboard")
        
        # Player Avatar
        avatar_image = Image.open(self.user.player.avatar.image_path)
        avatar_image = avatar_image.resize((100, 100), Image.ANTIALIAS)
        avatar_photo = ImageTk.PhotoImage(avatar_image)
        avatar_label = tk.Label(self.root, image=avatar_photo)
        avatar_label.image = avatar_photo
        avatar_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        # Player Stats
        stats_frame = tk.Frame(self.root)
        stats_frame.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(stats_frame, text=f"Player: {self.user.player.player_name}").grid(row=0, column=0, sticky="w")
        tk.Label(stats_frame, text=f"Level: {self.user.player.lvl}").grid(row=1, column=0, sticky="w")
        tk.Label(stats_frame, text=f"EXP: {self.user.player.exp}").grid(row=2, column=0, sticky="w")
        tk.Label(stats_frame, text=f"HP: {self.user.player.hp}").grid(row=3, column=0, sticky="w")
        tk.Label(stats_frame, text=f"MP: {self.user.player.mp}").grid(row=4, column=0, sticky="w")
        tk.Label(stats_frame, text=f"SP: {self.user.player.sp}").grid(row=5, column=0, sticky="w")
        tk.Label(stats_frame, text=f"Strength: {self.user.player.strength}").grid(row=6, column=0, sticky="w")
        tk.Label(stats_frame, text=f"Agility: {self.user.player.agility}").grid(row=7, column=0, sticky="w")
        tk.Label(stats_frame, text=f"Stamina: {self.user.player.stamina}").grid(row=8, column=0, sticky="w")
        tk.Label(stats_frame, text=f"Vitality: {self.user.player.vitality}").grid(row=9, column=0, sticky="w")
        tk.Label(stats_frame, text=f"Intelligence: {self.user.player.intelligence}").grid(row=10, column=0, sticky="w")

        # Today's Quests
        quests_frame = tk.Frame(self.root)
        quests_frame.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(quests_frame, text="Today's Quests:").grid(row=0, column=0, sticky="w")
        today = datetime.now().date()
        quests = self.get_todays_quests(today)
        for i, quest in enumerate(quests):
            tk.Label(quests_frame, text=f"{quest.title} - Due: {quest.due_date} {quest.due_time}").grid(row=i+1, column=0, sticky="w")

    def get_todays_quests(self, today):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM quests WHERE user_email = ? AND due_date = ?', (self.user.email, today))
        quests_data = c.fetchall()
        conn.close()
        quests = [Quest(*data[1:]) for data in quests_data]
        return quests

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root, "user@example.com")
    root.mainloop()