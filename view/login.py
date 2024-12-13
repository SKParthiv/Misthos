from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from classes.user import User

class Login(QWidget):
    def __init__(self, show_dashboard_callback, show_initial_screen_callback):
        super().__init__()
        self.show_dashboard_callback = show_dashboard_callback
        self.show_initial_screen_callback = show_initial_screen_callback
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Email:"))
        self.email_entry = QLineEdit()
        layout.addWidget(self.email_entry)
        layout.addWidget(QLabel("Password:"))
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_entry)
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def login(self):
        email = self.email_entry.text()
        password = self.password_entry.text()
        user = User.get_user_by_email(email)
        if user and user.password == password:
            QMessageBox.information(self, "Login", "Login successful!")
            self.show_dashboard_callback(email)
        else:
            QMessageBox.critical(self, "Login", "Invalid email or password")
            self.show_initial_screen_callback()

if __name__ == "__main__":
    app = QApplication([])
    login = Login(lambda email: print(f"Logged in as {email}"), lambda: print("Showing initial screen"))
    login.show()
    app.exec()
