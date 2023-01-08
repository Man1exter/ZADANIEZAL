from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QHeaderView
from PySide6.QtSql import QSqlQueryModel, QSqlQuery
from reg_user import RegUsers

class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.register_button = QPushButton("🐖 ZAREJESTRUJ SIĘ 🐖")
        self.register_button.clicked.connect(self.show_registration_dialog)
        self.login_button = QPushButton("🐖 ZALOGUJ SIĘ 🐖")
        self.login_button.clicked.connect(self.login)
        self.logout_button = QPushButton("🐖 WYLOGUJ SIĘ 🐖")
        self.logout_button.clicked.connect(self.logout)
        
        self.model = QSqlQueryModel()
        self.refresh_guinea_pigs()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        
        self.register_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.login_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.logout_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout = QVBoxLayout(self)
        #layout.addWidget(QLabel("🐷 WYPOŻYCZALNIA ŚWINEK"))
        layout.addWidget(self.register_button)
        layout.addWidget(self.login_button)
        layout.addWidget(self.logout_button)
        layout.addWidget(self.table_view)
        self.setLayout(layout)
        
    def refresh_guinea_pigs(self):
        query = QSqlQuery("SELECT * FROM guinea_pigs WHERE rented = 0")
        self.model.setQuery(query)

    def show_registration_dialog(self):
        dialog = RegUsers(self)
        dialog.exec_()

    def login(self):
        print("Zalogowano użytkownika")

    def logout(self):
        print("Wylogowano użytkownika")