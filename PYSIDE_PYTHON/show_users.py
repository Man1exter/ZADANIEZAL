from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from PySide6.QtGui import QIcon
from PyQt5.QtWidgets import * 

class ShowAllUsers(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.table = QTableWidget()
        
        self.table.setColumnCount(2) # nieograniczone kolumny max [3 -> od 0]
        self.table.setRowCount(99) # nieograniczone wiersze, jeżeli 0 to nieograniczona ilosc

        # Dodaj kolumnę i wiersz do tabelki
        self.table.insertColumn(0)
        self.table.insertRow(0)
        
        self.table.setHorizontalHeaderLabels(["IMIE:","NAZWISKO:","EMAIL:"])

        # Wyświetl tabelkę
        self.table.resize(925,550)
        
        for i in range(3):
          self.table.setColumnWidth(i,300)
          
        self.table.setItem(0,0, QTableWidgetItem("Name"))
        self.table.setItem(0,1, QTableWidgetItem("Name"))
        self.table.setItem(1,0, QTableWidgetItem("ABC"))
        self.table.setItem(2,0, QTableWidgetItem("ABC"))
        
        self.table.show()
        
        
if __name__ == "__main__":
    program = QApplication([])
    window = ShowAllUsers()
    program.exec()