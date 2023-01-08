from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog
from interface_login import LoginWindowUser

class RegWindowUser(QWidget):
    def __init__(self,parent=None):
        super(RegWindowUser,self).__init__(parent)
        
        # elementy interfejsu
        self.label_username = QLabel("                     🐷NAZWA UŻYTKOWNIKA🐷:")
        self.line_edit_username = QLineEdit()
        self.label_password = QLabel("                                      🐷HASŁO🐷:")
        self.label_confirm_password = QLabel("                            🐷POWTÓRZ HASŁO🐷:")
        self.line_edit_password = QLineEdit()
        self.line_edit_confirm_password = QLineEdit()
        self.line_edit_password.setEchoMode(QLineEdit.Password) # zakropkowanie wpisanego hasla
        self.line_edit_confirm_password.setEchoMode(QLineEdit.Password) # zakropkowanie wpisanego hasla
        self.button_register = QPushButton("🐽🐽ZAREJESTRUJ SIĘ🐽🐽")
        self.button_login = QPushButton("🐽🐽ZALOGUJ SIĘ🐽🐽")
        
        
        # self.setFixedHeight(width(width=600))
        
        # kolorki ziuuu - text
        self.label_username.setStyleSheet("color: white; font-weight: bold; font-size: 19px;")
        self.label_password.setStyleSheet("color: white; font-weight: bold; font-size: 19px;")
        self.label_confirm_password.setStyleSheet("color: white; font-weight: bold; font-size: 19px;")
        
        # kolorki ziuu - tabelki
        self.line_edit_username.setStyleSheet("color: yellow; font-weight: bold; font-size: 19px;")
        self.line_edit_password.setStyleSheet("color: yellow; font-weight: bold; font-size: 19px;")
        self.line_edit_confirm_password.setStyleSheet("color: yellow; font-weight: bold; font-size: 19px;")
        
        # kolorki ziuu - logowanie zaloguj button
        self.button_register.setStyleSheet("background-color: pink;color: yellow; font-weight: bold; font-size: 19px;")
        self.button_login.setStyleSheet("background-color: pink;color: yellow; font-weight: bold; font-size: 19px;")
        
            
        # layout i elementy do niego
        layout = QVBoxLayout()
        
        layout.addWidget(self.label_username)
        layout.addWidget(self.line_edit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.line_edit_password)
        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.line_edit_confirm_password)
        layout.addWidget(self.button_register)
        layout.addWidget(self.button_login)
        
        # layout na widget
        self.setLayout(layout)
        
        self.button_login.clicked.connect(self.login_panel)
           
    def login_panel(self):
        panel_control = QDialog(self)
        login_upper = LoginWindowUser()
        login_upper.setLayout(panel_control.layout())
        panel_control.resize(500,400)
            
        panel_control.exec()
        
        self.button_register.clicked.connect(self.clicked_button_text)
        
        
    def clicked_button_text(self):
        self.button.register("!ZAREJESTROWANO!")
        
             
        # window.resize(x,y) -> zmiana rozmiaru okna
