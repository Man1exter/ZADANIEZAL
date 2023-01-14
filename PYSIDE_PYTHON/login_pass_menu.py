from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from reg_user import ShowAllUsers
import sqlite3
import sys

class MenuPassLog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        form = QFormLayout()
        self.name_edit = QLineEdit()
        form.addRow("IMIE 🐷:", self.name_edit)
        self.password_edit = QLineEdit()
        form.addRow("HASŁO 🐷:", self.password_edit)
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        # self.name_edit = self.name_edit.text()
        
        self.name_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        self.password_edit.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: yellow;")
        
        self.register_button = QPushButton("🐖 ZALOGUJ 🐖")
        self.register_button.setStyleSheet("color: red; font-weight: bold; font-size: 20px; background-color: orange;")
        self.register_button.clicked.connect(self.confirmation_pass)
        
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.register_button)
        self.setLayout(layout)
        
    def confirmation_pass(self):
        
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()
        self.user_base = self.cursor.fetchone()
        
        self.accept()
        if self.name_edit.text() == "admin" and self.password_edit.text() == "admin":
            QMessageBox.information(self, "Informacja", "ZALOGOWANO JAKO ADMINISTRATOR SYSTEMU!")
            self.windowx = ShowAllUsers()
            self.windowx.show()
        else:
            QMessageBox.information(self, "Informacja", "ZALOGOWANO UŻYTKOWNIKA!")
            winaccept = Piggy(self)
            winaccept.show()
            
        self.conn.commit()
        self.conn.close()
        
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
        
        pig1_data = int(self.pig1.text())
        pig2_data = int(self.pig2.text())
        pig3_data = int(self.pig3.text())
        pig4_data = int(self.pig4.text())
        pig5_data = int(self.pig5.text())
        pig6_data = int(self.pig6.text())
        
        self.class2 = MenuPassLog()
        self.name_edit_co = self.class2.name_edit.text()

        if self.name_edit_co == "":
           QMessageBox.warning(self, "Uwaga", "Wybierz imię z listy")
        elif pig1_data == "" or pig2_data == "" or pig3_data == "" or pig4_data == "" or pig5_data == "" or pig6_data == "":
           QMessageBox.warning(self, "Uwaga", "Uzupełnij wszystkie pola")
        else:
          try:
            pig1_data = int(self.pig1.text())
            pig2_data = int(self.pig2.text())
            pig3_data = int(self.pig3.text())
            pig4_data = int(self.pig4.text())
            pig5_data = int(self.pig5.text())
            pig6_data = int(self.pig6.text())
          except ValueError:
            QMessageBox.warning(self, "Uwaga", "Wprowadź liczby")
            return
          else:
            self.conn = sqlite3.connect('mydatabase.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute("PRAGMA table_info(UŻYTKOWNICY)")
            columns = [tup[1] for tup in self.cursor.fetchall()]
            columns_to_add = ["PROSIAK", "WIETNAMKA", "SKARBONKA", "CHRUMKA", "SYBERYJSKA", "KAMBODŻANSKA"]
            for column in columns_to_add:
                if column not in columns:
                    self.cursor.execute(f"ALTER TABLE UŻYTKOWNICY ADD COLUMN {column} INTEGER")
                    print(f"Column '{column}' added to table 'UŻYTKOWNICY'.")
                else:
                    print(f"Column '{column}' already exists in table 'UŻYTKOWNICY'.")
            self.conn.commit()
            
            #data = self.cursor.fetchall()
            
            self.cursor.execute("UPDATE UŻYTKOWNICY SET PROSIAK = ?, WIETNAMKA = ?, SKARBONKA = ?, CHRUMKA = ?, SYBERYJSKA = ?, KAMBODŻANSKA = ?, WHERE IMIE=?", (pig1_data, pig2_data, pig3_data, pig4_data, pig5_data, pig6_data,self.name_edit_co))
            
            self.conn.commit()
            self.conn.close()
            QMessageBox.information(self, "Sukces", "Dane zostały zapisane!")
        
        sys.exit()
        
    def del_pig_con(self):
        QMessageBox.warning(self, "Uwaga", "WYNAJEM ANULOWANY")
        
        

        
