from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from show_users import ShowAllUsers
import hashlib
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
        
        self.register_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.cancel_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")

        # layout laczenie all
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(button_box)
        # layout.addWidget(self.password_edit)
        
    def register(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        
        print(f"Zarejestrowano nowego użytkownika: {name}, {email}, {password}")
        self.accept()
        
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        QMessageBox.information(self,"Hashed password",hashed_password)
        
        QMessageBox.information(self,"information","ZAREJESTROWANO UŻYTKOWNIKA W BAZIE!")
        
        people = [{"IMIE":self.name_edit.text(),"EMAIL":self.email_edit.text(),"HASŁO":hashed_password}]

