from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from classes.user import User, Player
from view.login import Login

class Register(QWidget):
    def __init__(self, show_dashboard, show_initial_screen):
        super().__init__()
        self.show_dashboard = show_dashboard
        self.show_initial_screen = show_initial_screen
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Register")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Real Name:"))
        self.real_name_entry = QLineEdit()
        layout.addWidget(self.real_name_entry)

        layout.addWidget(QLabel("Age:"))
        self.age_entry = QLineEdit()
        layout.addWidget(self.age_entry)

        layout.addWidget(QLabel("Education Level:"))
        self.education_lvl_entry = QLineEdit()
        layout.addWidget(self.education_lvl_entry)

        layout.addWidget(QLabel("Email:"))
        self.email_entry = QLineEdit()
        layout.addWidget(self.email_entry)

        layout.addWidget(QLabel("Password:"))
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_entry)

        layout.addWidget(QLabel("Field of Education:"))
        self.field_of_education_entry = QLineEdit()
        layout.addWidget(self.field_of_education_entry)

        layout.addWidget(QLabel("Hobbies:"))
        self.hobbies_entry = QLineEdit()
        layout.addWidget(self.hobbies_entry)

        layout.addWidget(QLabel("School Attending:"))
        self.school_attending_entry = QLineEdit()
        layout.addWidget(self.school_attending_entry)

        layout.addWidget(QLabel("Likes:"))
        self.likes_entry = QLineEdit()
        layout.addWidget(self.likes_entry)

        layout.addWidget(QLabel("Dislikes:"))
        self.dislikes_entry = QLineEdit()
        layout.addWidget(self.dislikes_entry)

        layout.addWidget(QLabel("Player Name:"))
        self.player_name_entry = QLineEdit()
        layout.addWidget(self.player_name_entry)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register)
        layout.addWidget(register_button)

        self.setLayout(layout)

    def register(self):
        real_name = self.real_name_entry.text()
        age = int(self.age_entry.text())
        education_lvl = self.education_lvl_entry.text()
        email = self.email_entry.text()
        password = self.password_entry.text()
        field_of_education = self.field_of_education_entry.text()
        hobbies = self.hobbies_entry.text()
        school_attending = self.school_attending_entry.text()
        likes = self.likes_entry.text()
        dislikes = self.dislikes_entry.text()
        player_name = self.player_name_entry.text()

        player = Player(player_name, strength=5, agility=5, stamina=5, vitality=5, intelligence=5, lvl=1, exp=0)
        user = User(real_name, age, education_lvl, email, password, field_of_education, hobbies, school_attending, likes, dislikes, player)
        user.create_table()
        user.save()
        QMessageBox.information(self, "Register", "Registration successful!")
        self.show_initial_screen()
