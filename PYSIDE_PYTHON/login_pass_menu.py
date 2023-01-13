from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from reg_user import ShowAllUsers
from dz import Piggy

class MenuPassLog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        form = QFormLayout()
        self.name_edit = QLineEdit()
        form.addRow("IMIE 🐷:", self.name_edit)
        self.password_edit = QLineEdit()
        form.addRow("HASŁO 🐷:", self.password_edit)
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        self.name_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.password_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        
        self.register_button = QPushButton("🐖 ZALOGUJ 🐖")
        self.register_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: orange;")
        self.register_button.clicked.connect(self.confirmation_pass)
        
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.register_button)
        self.setLayout(layout)
        
    def confirmation_pass(self):
        self.accept()
        if self.name_edit.text() == "admin" and self.password_edit.text() == "admin":
            QMessageBox.information(self, "Informacja", "ZALOGOWANO JAKO ADMINISTRATOR SYSTEMU!")
            window = ShowAllUsers(self)
        else:
            QMessageBox.information(self, "Informacja", "ZALOGOWANO UŻYTKOWNIKA!")
            winaccept = Piggy(self)
            winaccept.show()
        
        
        

        
