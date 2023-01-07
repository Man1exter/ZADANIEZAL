from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from interface_Start import LoginWindowUser


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("WYNAJEM SWINEK NA GODZINE")
    
    # stworzona instancja
    login_widget = LoginWindowUser() 
    
    login_widget.resize(500, 400)
    login_widget.setStyleSheet("background-color: black;")
    #login_widget.setStyleSheet("color: red; font-weight: bold; font-size: 30px;")

    login_widget.show()
    
    app.exec()