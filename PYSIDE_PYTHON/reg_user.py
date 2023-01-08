from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QHeaderView
from PySide6.QtSql import QSqlQueryModel, QSqlQuery

class RegUsers(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # layout formularza rejestracyjnego
        form = QFormLayout()
        self.name_edit = QLineEdit()
        form.addRow("IMIE 🐷:", self.name_edit)
        self.email_edit = QLineEdit()
        form.addRow("EMAIL 🐷:", self.email_edit)
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        form.addRow("HASŁO 🐷:", self.password_edit)
        
        self.name_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.email_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.password_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")

        button_box = QHBoxLayout()
        self.register_button = QPushButton("🐷 ZAREJESTRUJ SIĘ 🐷")
        self.register_button.clicked.connect(self.register)
        button_box.addWidget(self.register_button)
        self.cancel_button = QPushButton("🐷 ANULUJ 🐷")
        self.cancel_button.clicked.connect(self.reject)
        button_box.addWidget(self.cancel_button)
        
        

        # layout laczenie all
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(button_box)

    def register(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()

        print(f"Zarejestrowano nowego użytkownika: {name}, {email}, {password}")
        self.accept()