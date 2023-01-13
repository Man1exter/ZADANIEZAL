from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PySide6.QtWidgets import *
from PySide6.QtSql import *
import hashlib
from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from PySide6.QtGui import QIcon
import sqlite3
class RegUsers(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # layout formularza rejestracyjnego
        form = QFormLayout()
        self.name_edit = QLineEdit()
        form.addRow("IMIE 🐷:", self.name_edit)
        self.email_edit = QLineEdit()
        form.addRow("EMAIL 🐷:", self.email_edit)
        self.password_edit = QLineEdit()
        form.addRow("HASŁO 🐷:", self.password_edit)
        
        self.name = ""
        self.email = ""
        self.password = ""
                 
        self.name_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.email_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.password_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")

        button_box = QHBoxLayout()
        self.register_button = QPushButton("🐷 ZAREJESTRUJ SIĘ 🐷")
        self.register_button.clicked.connect(self.register)
        button_box.addWidget(self.register_button)
        self.cancel_button = QPushButton("🐷 ANULUJ 🐷")
        self.cancel_button.clicked.connect(self.reject)
        button_box.addWidget(self.cancel_button)
        
        self.register_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.cancel_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")

        # layout laczenie all
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(button_box)
        # layout.addWidget(self.password_edit)
        
    def register(self):
        self.name = self.name_edit.text()
        self.email = self.email_edit.text()
        self.password = self.password_edit.text()
        
        print(f"Zarejestrowano nowego użytkownika: {self.name}, {self.email}, {self.password}")
        self.accept()
        
        self.hashed_password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
 
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS UŻYTKOWNICY (IMIE TEXT, EMAIL TEXT, HASLO TEXT)''')
        self.conn.commit()
        
        self.cursor.execute('''SELECT * FROM UŻYTKOWNICY WHERE IMIE=? AND EMAIL=?''', (self.name, self.email))
        
        self.user_base = self.cursor.fetchone()
        
        if self.user_base:
            QMessageBox.warning(self, "Uwaga", f"Użytkownik {self.name} już istnieje!")
        else:
            self.cursor.execute('''INSERT INTO UŻYTKOWNICY (IMIE, EMAIL, HASLO) VALUES (?,?,?)''', (self.name, self.email, self.hashed_password))
            QMessageBox.information(self,"information","ZAREJESTROWANO UŻYTKOWNIKA W BAZIE!")
            QMessageBox.information(self,"Hashed password",self.hashed_password)
        
        self.conn.commit()
        self.conn.close()
                        
class ShowAllUsers(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.table = QTableWidget()
        
        self.col = 0
        self.row = 0
        
        self.table.setColumnCount(8) 
        self.table.setRowCount(99) 

        # Dodaj kolumnę i wiersz do tabelki
        self.table.insertColumn(0)
        self.table.insertRow(0)
        
        self.table.setHorizontalHeaderLabels(["IMIE:","HASŁO:","EMAIL:","PROSIAK", "WIETNAMKA", "SKARBONKA", "CHRUMKA", "SYBERYJSKA", "KAMBODŻANSKA"])

        # Wyświetl tabelkę (zmiana rozmiaru)
        self.table.resize(1600,850)
        
        for i in range(3):
          self.table.setColumnWidth(i,300)      
          
    # def loaddata - ładowanie z bazy danych do tabelki pyside6
      #con = sqlite3.connect("data.sqlite")
      # cursor = con.cursor()
      # sqlquery = " SELECT * FROM worldcities LIMIT 50"
      
      # self.tableWidget.setRowCount(50)
      # tablerow = 0
      # for row in cur.execute(sqlquer):
        ##self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            #self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[0]))
            #self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[0]))
            # tablerow += 1
            
        self.table.show()
        
#if __name__ == "__main__":
    #program = QApplication([])
    #window = ShowAllUsers()
    #program.exec()
        

