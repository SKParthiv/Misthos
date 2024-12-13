from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget
from PyQt6.QtCore import Qt
from classes.quest import Quest

class QuestView(QWidget):
    def __init__(self, user_email):
        super().__init__()
        self.user_email = user_email
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Quest View")
        layout = QVBoxLayout()

        # Quest Creation
        layout.addWidget(QLabel("Create New Quest:"))
        layout.addWidget(QLabel("Title:"))
        self.title_entry = QLineEdit()
        layout.addWidget(self.title_entry)
        layout.addWidget(QLabel("Description:"))
        self.description_entry = QLineEdit()
        layout.addWidget(self.description_entry)
        layout.addWidget(QLabel("Due Date (YYYY-MM-DD):"))
        self.due_date_entry = QLineEdit()
        layout.addWidget(self.due_date_entry)
        layout.addWidget(QLabel("Due Time (HH:MM):"))
        self.due_time_entry = QLineEdit()
        layout.addWidget(self.due_time_entry)
        layout.addWidget(QLabel("Priority (1-3):"))
        self.priority_entry = QLineEdit()
        layout.addWidget(self.priority_entry)
        create_button = QPushButton("Create Quest")
        create_button.clicked.connect(self.create_quest)
        layout.addWidget(create_button)

        # Pending Quests List
        layout.addWidget(QLabel("Pending Quests:"))
        self.pending_quests_listbox = QListWidget()
        layout.addWidget(self.pending_quests_listbox)
        self.load_pending_quests()

        self.setLayout(layout)

    def load_pending_quests(self):
        self.pending_quests_listbox.clear()
        pending_quests = Quest.get_pending_quests(self.user_email)
        for quest in pending_quests:
            self.pending_quests_listbox.addItem(f"{quest.title} - Due: {quest.due_date} {quest.due_time} - Priority: {quest.priority}")

    def create_quest(self):
        title = self.title_entry.text()
        description = self.description_entry.text()
        due_date = self.due_date_entry.text()
        due_time = self.due_time_entry.text()
        priority = int(self.priority_entry.text())
        reward = Quest.generate_reward(priority)
        punishment = Quest.generate_punishment(priority)
        new_quest = Quest(title, description, None, reward, punishment, self.user_email, due_date, due_time, priority)
        new_quest.create_table()
        new_quest.save()
        new_quest.save_to_db()
        self.load_pending_quests()

if __name__ == "__main__":
    app = QApplication([])
    quest_view = QuestView("user@example.com")
    quest_view.show()
    app.exec()
