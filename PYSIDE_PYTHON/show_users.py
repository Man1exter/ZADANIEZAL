from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from PySide6.QtGui import QIcon
import sqlite3


class ShowAllUsers(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.table = QTableWidget()
        
        self.col = 0
        self.row = 0
        
        self.table.setColumnCount(2) # nieograniczone kolumny max [3 -> od 0]
        self.table.setRowCount(99) # nieograniczone wiersze, jeżeli 0 to nieograniczona ilosc

        # Dodaj kolumnę i wiersz do tabelki
        self.table.insertColumn(0)
        self.table.insertRow(0)
        
        self.table.setHorizontalHeaderLabels(["IMIE:","HASŁO:","EMAIL:"])

        # Wyświetl tabelkę (zmiana rozmiaru)
        self.table.resize(1000,600)
        
        for i in range(3):
          self.table.setColumnWidth(i,300)
          
          
          
        # zawartość w tabelce
        
        #self.loaddata()
        
    #def loaddata(self):
        #people = [{"name":"JOHN"}] #itd
        #row = 0
        
        #for p in people:
            #self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(p["name"]))
            #self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(p["age"]))
            #self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(p["nick"]))
            
            #row = row + 1
            
            
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
        
if __name__ == "__main__":
    program = QApplication([])
    window = ShowAllUsers()
    program.exec()