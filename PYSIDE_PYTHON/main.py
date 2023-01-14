from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtGui import QIcon
from log_users import MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    program = QApplication([])
    window = MainWindow()
    
    window.resize(400,300)
    window.setWindowTitle("🐷 WYPOŻYCZALNIA ŚWINEK")
    window.setStyleSheet("background-color: lightblue;")
    window.setWindowIcon(QIcon("pig.png"))
    
    window.show()
    program.exec()