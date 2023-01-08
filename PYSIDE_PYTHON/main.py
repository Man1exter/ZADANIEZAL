from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QHeaderView
from PySide6.QtSql import QSqlQueryModel, QSqlQuery
from PySide6.QtGui import QIcon
from reg_user import RegUsers
from log_users import MainWindow
        
if __name__ == "__main__":
    program = QApplication([])
    window = MainWindow()
    
    window.resize(500,400)
    window.setWindowTitle("🐷 WYPOŻYCZALNIA ŚWINEK")
    window.setStyleSheet("background-color: lightblue;")
    window.setWindowIcon(QIcon("pig.png"))
    
    window.show()
    program.exec()