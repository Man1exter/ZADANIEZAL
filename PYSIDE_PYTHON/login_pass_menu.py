from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QHeaderView, QMessageBox
from PySide6.QtGui import QIcon

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
        
        self.register_button = QPushButton("🐖 ZAREJESTRUJ 🐖")
        self.register_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: orange;")
        self.register_button.clicked.connect(self.confirmation_pass)
        
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.register_button)
        self.setLayout(layout)
        
    def confirmation_pass(self):
        self.accept()
        QMessageBox.information(self, "Informacja", "ZALOGOWANO UŻYTKOWNIKA")
        
if __name__ == "__main__":
    program = QApplication([])
    window = MenuPassLog()
    window.setStyleSheet("background-color: lightblue;")
    window.setWindowIcon(QIcon("pig.png"))
    window.show()
    program.exec()