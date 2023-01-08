from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from interface_login import LoginWindowUser


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("WYNAJEM SWINEK NA GODZINE v1.0.1")
    
    # stworzona instancja
    login_widget = LoginWindowUser() 
    
    login_widget.resize(500, 400)
    login_widget.setStyleSheet("background-color: black;")
    #login_widget.setStyleSheet("color: red; font-weight: bold; font-size: 30px;")

    login_widget.show()
    
    app.exec()