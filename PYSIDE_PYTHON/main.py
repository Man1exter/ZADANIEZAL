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
    
    
# DAWID - IMIE , HASLO - 8f1f4de58504e49babb0c7d11195d685710ad1fa444707b1d68e58068c909d29
# admin - imie, haslo - 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918