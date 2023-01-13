from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtGui import QIcon
import sqlite3
import sys

class Piggy(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        
        form = QFormLayout()
        self.pig1 = QLineEdit()
        form.addRow("PROSIAK 🐷:", self.pig1)
        self.pig2 = QLineEdit()
        form.addRow("WIETNAMKA 🐷:", self.pig2)
        self.pig3 = QLineEdit()
        #self.password_edit.setEchoMode(QLineEdit.Password)
        form.addRow("SKARBONKA 🐷:", self.pig3)
        self.pig4 = QLineEdit()
        form.addRow("CHRUMKA 🐷:", self.pig4)
        self.pig5 = QLineEdit()
        form.addRow("SYBERYJSKA 🐷:", self.pig5)
        self.pig6 = QLineEdit()
        form.addRow("KAMBODŻANSKA 🐷:", self.pig6)
        
        self.pig1.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.pig2.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.pig3.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.pig4.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.pig5.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.pig6.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        
        button_box = QHBoxLayout()
        self.accept_pig = QPushButton("🐷 ZATWIERDZ WYNAJEM 🐷")
        button_box.addWidget(self.accept_pig)
        self.accept_pig.clicked.connect(self.accept_pig_confirm)
        self.cancel_button = QPushButton("🐷 ANULUJ WYNAJEM 🐷")
        self.cancel_button.clicked.connect(self.reject)
        button_box.addWidget(self.cancel_button)
        self.cancel_button.clicked.connect(self.del_pig_con)
        
        self.accept_pig.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.cancel_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(button_box)
        
        
    def accept_pig_confirm(self):
        QMessageBox.warning(self, "Uwaga", "WYNAJEM ZAAKCEPTOWANY") 
        
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("PRAGMA table_info(UŻYTKOWNICY)")
        columns = [tup[1] for tup in self.cursor.fetchall()]

        columns_to_add = ["PROSIAK", "WIETNAMKA", "SKARBONKA", "CHRUMKA", "SYBERYJSKA", "KAMBODŻANSKA"]

        for column in columns_to_add:
           if column not in columns:
              self.cursor.execute(f"ALTER TABLE UŻYTKOWNICY ADD COLUMN {column} TEXT")
              print(f"Column '{column}' added to table 'UŻYTKOWNICY'.")
        else:
           print(f"Column '{column}' already exists in table 'UŻYTKOWNICY'.")

        self.conn.commit()
        self.conn.close()
        
        sys.exit()
        
    def del_pig_con(self):
        QMessageBox.warning(self, "Uwaga", "WYNAJEM ANULOWANY")
        
        
#if __name__ == "__main__":
    #program = QApplication([])
    #window = Piggy()
    
    #window.resize(400,300)
    #window.setWindowTitle("🐷 WYPOŻYCZALNIA ŚWINEK")
    #window.setStyleSheet("background-color: lightblue;")
    #window.setWindowIcon(QIcon("pig.png"))
    
    #window.show()
    #program.exec()