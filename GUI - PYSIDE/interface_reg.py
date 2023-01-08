from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class RegWindowUser(QWidget):
    def __init__(self):
        super().__init__()
        
        # elementy interfejsu
        self.label_username = QLabel("                     NAZWA UŻYTKOWNIKA🐷:")
        self.line_edit_username = QLineEdit()
        self.label_password = QLabel("                                      HASŁO🐷:")
        self.label_confirm_password = QLabel("                             POTWIERDZ HASŁO🐷:")
        self.line_edit_password = QLineEdit()
        self.line_edit_confirm_password = QLineEdit()
        # self.line_edit_password.setEchoMode(QLineEdit.Password) # zakropkowanie wpisanego hasla
        self.button_register = QPushButton("🐽🐽ZAREJESTRUJ SIĘ🐽🐽")
        # self.setFixedHeight(width(width=600))
        
        # kolorki ziuuu - text
        self.label_username.setStyleSheet("color: white; font-weight: bold; font-size: 19px;")
        self.label_password.setStyleSheet("color: white; font-weight: bold; font-size: 19px;")
        self.label_confirm_password.setStyleSheet("color: white; font-weight: bold; font-size: 19px;")
        
        # kolorki ziuu - tabelki
        self.line_edit_username.setStyleSheet("color: yellow; font-weight: bold; font-size: 19px;")
        self.line_edit_password.setStyleSheet("color: yellow; font-weight: bold; font-size: 19px;")
        self.line_edit_confirm_password.setStyleSheet("color: yellow; font-weight: bold; font-size: 19px;")
        
        # kolorki ziuu - logowanie REJESTRACJA button
        self.button_register.setStyleSheet("background-color: pink;color: yellow; font-weight: bold; font-size: 19px;")
        
        # layout i elementy do niego
        layout = QVBoxLayout()
        
        layout.addWidget(self.label_username)
        layout.addWidget(self.line_edit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.line_edit_password)
        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.line_edit_confirm_password)
        layout.addWidget(self.button_register)
        
        # layout na widget
        self.setLayout(layout)
            
        # window.resize(x,y) -> zmiana rozmiaru okna
        
if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("WYNAJEM SWINEK NA GODZINE v1.0.1")
    
    # stworzona instancja
    login_widget = RegWindowUser() 
    
    login_widget.resize(500, 400)
    login_widget.setStyleSheet("background-color: black;")
    #login_widget.setStyleSheet("color: red; font-weight: bold; font-size: 30px;")

    login_widget.show()
    
    app.exec()