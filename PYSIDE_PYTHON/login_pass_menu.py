from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QHeaderView, QMessageBox, QTableWidget, QTableWidgetItem, QWidget
from PySide6.QtGui import QIcon
from show_users import ShowAllUsers

class MenuPassLog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        form = QFormLayout()
        self.name_edit = QLineEdit()
        form.addRow("IMIE 🐷:", self.name_edit)
        self.password_edit = QLineEdit()
        form.addRow("HASŁO 🐷:", self.password_edit)
        
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
        meth_base = ShowAllUsers(self)
        QMessageBox.information(self, "Informacja", "ZALOGOWANO UŻYTKOWNIKA")
        
        # jezeli login i haslo to h:admin l:admin wyswietl wszystkich uzytkownikow do modyfikacji ich
        # jezeli to random osoba przejdz do wynajmu swinek
        
        
        

        
