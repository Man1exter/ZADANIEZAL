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
        #self.accept_pig.clicked.connect(self.up_to_base)
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
        
        pig1_data = self.pig1.text()
        pig2_data = self.pig2.text()
        pig3_data = self.pig3.text()
        pig4_data = self.pig4.text()
        pig5_data = self.pig5.text()
        pig6_data = self.pig6.text()
        
        selected_name = self.name_select.currentText()
        
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
           
           
        self.cursor.execute("UPDATE UŻYTKOWNICY SET PROSIAK = ?, WIETNAMKA = ?, SKARBONKA = ?, CHRUMKA = ?, SYBERYJSKA = ?, KAMBODŻANSKA = ?, WHERE IMIE = ?", (pig1_data, pig2_data, pig3_data, pig4_data, pig5_data, pig6_data, selected_name))
        self.conn.commit()

        self.conn.commit()
        self.conn.close()
        
        sys.exit()
        
    def del_pig_con(self):
        QMessageBox.warning(self, "Uwaga", "WYNAJEM ANULOWANY")
        
        
    #def up_to_base(self):
        #self.conn = sqlite3.connect('mydatabase.db')
        #self.cursor = self.conn.cursor()
        
       # pig1_data = self.pig1.text()
        #pig2_data = self.pig2.text()
       # pig3_data = self.pig3.text()
       # pig4_data = self.pig4.text()
       # pig5_data = self.pig5.text()
       # pig6_data = self.pig6.text()
        
        #selected_name = self.name_select.currentText()
   
        #self.cursor.execute('''CREATE TABLE IF NOT EXISTS UŻYTKOWNICY (IMIE TEXT, EMAIL TEXT, HASLO TEXT, PROSIAK TEXT, WIETNAMKA TEXT, SKARBONKA TEXT, CHRUMKA TEXT, SYBERYJSKA TEXT, KAMBODŻANSKA TEXT)''')
        #self.conn.commit()
        
        #self.cursor.execute('''SELECT * FROM UŻYTKOWNICY WHERE PROSIAK=? AND WIETNAMKA=? AND SKARBONKA=? AND CHRUMKA=? AND SYBERYJSKA=? AND KAMBODŻANSKA=?''', (self.#pig1,self.pig2,self.pig3,self.pig4,self.pig5,self.pig6))
        
        #self.cursor.execute('''INSERT INTO UŻYTKOWNICY (PROSIAK, WIETNAMKA, SKARBONKA, CHRUMKA, SYBERYJSKA, KAMBODŻANSKA) VALUES (?,?,?,?,?,?)''', (self.pig1,self.#pig2,self.pig3,self.pig4,self.pig5,self.pig6))
        
        #self.cursor.execute("INSERT INTO UŻYTKOWNICY (PROSIAK, WIETNAMKA, SKARBONKA, CHRUMKA, SYBERYJSKA, KAMBODŻANSKA) VALUES (?,?,?,?,?,?)", (pig1_data, #pig2_data, pig3_data, pig4_data, pig5_data, pig6_data))
        
        #elf.cursor.execute("INSERT INTO UŻYTKOWNICY (PROSIAK, WIETNAMKA, SKARBONKA, CHRUMKA, SYBERYJSKA, KAMBODŻANSKA) VALUES (%s, %s, %s, %s, %s, %s)", #(pig1_data, pig2_data, pig3_data, pig4_data, pig5_data, pig6_data))
        
        
        #self.conn.commit()
       # self.conn.close()
        