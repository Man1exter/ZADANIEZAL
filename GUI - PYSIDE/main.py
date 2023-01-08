from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow
from interface_login import LoginWindowUser
from interface_reg import RegWindowUser



if __name__ == "__main__":
    app_login = QApplication([])
    app_login.setApplicationName("WYNAJEM SWINEK NA GODZINE v1.0.1")
    
    # stworzona instancja
    login_widget = LoginWindowUser() 
    reg_widget = RegWindowUser() 
    
    login_widget.resize(500, 400)
    login_widget.setStyleSheet("background-color: black;")
    #login_widget.setStyleSheet("color: red; font-weight: bold; font-size: 30px;")

    login_widget.show()
    reg_widget.show()
    
    app_login.exec()