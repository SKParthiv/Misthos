import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3
from classes.quest import Quest

class QuestView:
    def __init__(self, root, user_email):
        self.root = root
        self.user_email = user_email
        self.create_ui()

    def create_ui(self):
        self.root.title("Quest View")

        # Quest List
        self.quest_list_frame = tk.Frame(self.root)
        self.quest_list_frame.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.quest_list_frame, text="Quests:").grid(row=0, column=0, sticky="w")
        self.quest_listbox = tk.Listbox(self.quest_list_frame, width=50, height=20)
        self.quest_listbox.grid(row=1, column=0, sticky="w")
        self.load_quests()

        # Quest Creation
        self.quest_creation_frame = tk.Frame(self.root)
        self.quest_creation_frame.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.quest_creation_frame, text="Create New Quest:").grid(row=0, column=0, columnspan=2, sticky="w")
        tk.Label(self.quest_creation_frame, text="Title:").grid(row=1, column=0, sticky="w")
        self.title_entry = tk.Entry(self.quest_creation_frame)
        self.title_entry.grid(row=1, column=1, sticky="w")
        tk.Label(self.quest_creation_frame, text="Description:").grid(row=2, column=0, sticky="w")
        self.description_entry = tk.Entry(self.quest_creation_frame)
        self.description_entry.grid(row=2, column=1, sticky="w")
        tk.Label(self.quest_creation_frame, text="Due Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w")
        self.due_date_entry = tk.Entry(self.quest_creation_frame)
        self.due_date_entry.grid(row=3, column=1, sticky="w")
        tk.Label(self.quest_creation_frame, text="Due Time (HH:MM):").grid(row=4, column=0, sticky="w")
        self.due_time_entry = tk.Entry(self.quest_creation_frame)
        self.due_time_entry.grid(row=4, column=1, sticky="w")
        tk.Button(self.quest_creation_frame, text="Create Quest", command=self.create_quest).grid(row=5, column=0, columnspan=2, pady=10)

    def load_quests(self):
        self.quest_listbox.delete(0, tk.END)
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM quests WHERE user_email = ?', (self.user_email,))
        quests_data = c.fetchall()
        conn.close()
        for quest_data in quests_data:
            quest = Quest(*quest_data[1:])
            self.quest_listbox.insert(tk.END, f"{quest.title} - Due: {quest.due_date} {quest.due_time}")

    def create_quest(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        due_time = self.due_time_entry.get()
        reward = Quest.generate_reward(self.user_email, title, description)
        punishment = Quest.generate_punishment(self.user_email, title, description)
        new_quest = Quest(title, description, None, reward, punishment, self.user_email, due_date, due_time)
        new_quest.save()
        self.load_quests()

if __name__ == "__main__":
    root = tk.Tk()
    quest_view = QuestView(root, "user@example.com")
    root.mainloop()
