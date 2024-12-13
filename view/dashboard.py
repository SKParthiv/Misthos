from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PIL import Image
from datetime import datetime
import sqlite3
from classes.user import User
from classes.quest import Quest

class Dashboard(QWidget):
    def __init__(self, user_email):
        super().__init__()
        self.user = User.get_user_by_email(user_email)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Dashboard")
        layout = QVBoxLayout()

        # Player Avatar
        avatar_layout = QHBoxLayout()
        avatar_image = Image.open(self.user.player.avatar.image_path)
        avatar_image = avatar_image.resize((100, 100), Image.ANTIALIAS)
        avatar_pixmap = QPixmap.fromImage(avatar_image.toqimage())
        avatar_label = QLabel()
        avatar_label.setPixmap(avatar_pixmap)
        avatar_layout.addWidget(avatar_label)

        # Player Stats
        stats_layout = QVBoxLayout()
        stats_layout.addWidget(QLabel(f"Player: {self.user.player.player_name}"))
        stats_layout.addWidget(QLabel(f"Level: {self.user.player.lvl}"))
        stats_layout.addWidget(QLabel(f"EXP: {self.user.player.exp}"))
        stats_layout.addWidget(QLabel(f"HP: {self.user.player.hp}"))
        stats_layout.addWidget(QLabel(f"MP: {self.user.player.mp}"))
        stats_layout.addWidget(QLabel(f"SP: {self.user.player.sp}"))
        stats_layout.addWidget(QLabel(f"Strength: {self.user.player.strength}"))
        stats_layout.addWidget(QLabel(f"Agility: {self.user.player.agility}"))
        stats_layout.addWidget(QLabel(f"Stamina: {self.user.player.stamina}"))
        stats_layout.addWidget(QLabel(f"Vitality: {self.user.player.vitality}"))
        stats_layout.addWidget(QLabel(f"Intelligence: {self.user.player.intelligence}"))

        avatar_layout.addLayout(stats_layout)
        layout.addLayout(avatar_layout)

        # Today's Quests
        layout.addWidget(QLabel("Today's Quests:"))
        today = datetime.now().date()
        quests = self.get_todays_quests(today)
        for quest in quests:
            layout.addWidget(QLabel(f"{quest.title} - Due: {quest.due_date} {quest.due_time} - Priority: {quest.priority}"))

        self.setLayout(layout)

    def get_todays_quests(self, today):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM quests WHERE user_email = ? AND due_date = ? ORDER BY priority DESC', (self.user.email, today))
        quests_data = c.fetchall()
        conn.close()
        quests = [Quest(*data[1:]) for data in quests_data]
        return quests

if __name__ == "__main__":
    app = QApplication([])
    dashboard = Dashboard("user@example.com")
    dashboard.show()
    app.exec()