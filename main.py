from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from view.login import Login
from view.dashboard import Dashboard
from view.settings import Settings
from view.quest_view import QuestView
from classes.user import User
from game.gameUI import Game
from view.register import Register

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user_email = None
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Misthos")
        self.central_widget.setLayout(QVBoxLayout())  # Initialize the layout
        self.show_initial_screen()

    def show_initial_screen(self):
        self.clear_layout()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to Misthos"))
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.show_login)
        layout.addWidget(login_button)
        register_button = QPushButton("Register")
        register_button.clicked.connect(self.show_register)
        layout.addWidget(register_button)
        self.central_widget.setLayout(layout)

    def show_login(self):
        self.clear_layout()
        login = Login(self.show_dashboard, self.show_initial_screen)
        self.central_widget.setLayout(login.layout())

    def show_register(self):
        self.clear_layout()
        register = Register(self.show_dashboard, self.show_initial_screen)
        self.central_widget.setLayout(register.layout())

    def show_dashboard(self, user_email):
        self.user_email = user_email
        self.clear_layout()
        dashboard = Dashboard(user_email)
        self.central_widget.setLayout(dashboard.layout())

    def show_settings(self):
        self.clear_layout()
        settings = Settings(self.user_email)
        self.central_widget.setLayout(settings.layout())

    def show_quest_view(self):
        self.clear_layout()
        quest_view = QuestView(self.user_email)
        self.central_widget.setLayout(quest_view.layout())

    def clear_layout(self):
        layout = self.central_widget.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    layout.removeItem(item)

if __name__ == "__main__":
    app = QApplication([])
    main_app = MainApp()
    main_app.show()
    app.exec()