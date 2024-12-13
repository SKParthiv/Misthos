from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from classes.user import User

class Settings(QWidget):
    def __init__(self, user_email):
        super().__init__()
        self.user = User.get_user_by_email(user_email)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Settings")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Edit User Details:"))
        layout.addWidget(QLabel("Real Name:"))
        self.real_name_entry = QLineEdit()
        self.real_name_entry.setText(self.user.real_name)
        layout.addWidget(self.real_name_entry)

        layout.addWidget(QLabel("Age:"))
        self.age_entry = QLineEdit()
        self.age_entry.setText(str(self.user.age))
        layout.addWidget(self.age_entry)

        layout.addWidget(QLabel("Education Level:"))
        self.education_lvl_entry = QLineEdit()
        self.education_lvl_entry.setText(self.user.education_lvl)
        layout.addWidget(self.education_lvl_entry)

        layout.addWidget(QLabel("Email:"))
        self.email_entry = QLineEdit()
        self.email_entry.setText(self.user.email)
        layout.addWidget(self.email_entry)

        layout.addWidget(QLabel("Password:"))
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_entry.setText(self.user.password)
        layout.addWidget(self.password_entry)

        layout.addWidget(QLabel("Field of Education:"))
        self.field_of_education_entry = QLineEdit()
        self.field_of_education_entry.setText(self.user.field_of_education)
        layout.addWidget(self.field_of_education_entry)

        layout.addWidget(QLabel("Hobbies:"))
        self.hobbies_entry = QLineEdit()
        self.hobbies_entry.setText(self.user.hobbies)
        layout.addWidget(self.hobbies_entry)

        layout.addWidget(QLabel("School Attending:"))
        self.school_attending_entry = QLineEdit()
        self.school_attending_entry.setText(self.user.school_attending)
        layout.addWidget(self.school_attending_entry)

        layout.addWidget(QLabel("Likes:"))
        self.likes_entry = QLineEdit()
        self.likes_entry.setText(self.user.likes)
        layout.addWidget(self.likes_entry)

        layout.addWidget(QLabel("Dislikes:"))
        self.dislikes_entry = QLineEdit()
        self.dislikes_entry.setText(self.user.dislikes)
        layout.addWidget(self.dislikes_entry)

        save_button = QPushButton("Save Changes")
        save_button.clicked.connect(self.save_changes)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_changes(self):
        self.user.real_name = self.real_name_entry.text()
        self.user.age = int(self.age_entry.text())
        self.user.education_lvl = self.education_lvl_entry.text()
        self.user.email = self.email_entry.text()
        self.user.password = self.password_entry.text()
        self.user.field_of_education = self.field_of_education_entry.text()
        self.user.hobbies = self.hobbies_entry.text()
        self.user.school_attending = self.school_attending_entry.text()
        self.user.likes = self.likes_entry.text()
        self.user.dislikes = self.dislikes_entry.text()
        self.user.save()
