from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from PySide6.QtGui import QIcon
from PyQt5.QtWidgets import * 

class ShowAllUsers(QWidget):
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
        
        self.table.setHorizontalHeaderLabels(["IMIE:","NAZWISKO:","EMAIL:"])

        # Wyświetl tabelkę
        self.table.resize(1000,600)
        
        for i in range(3):
          self.table.setColumnWidth(i,300)
          
        # zawartość w tabelce
          
        for im in range(3):
            self.table.setItem(im,0, QTableWidgetItem("IMIE"))

        for naz in range(3):
            self.table.setItem(naz,0+im-1, QTableWidgetItem("NAZWISKO"))
        
        for em in range(3):
            self.table.setItem(em-1,(0+im)+3, QTableWidgetItem("EMAIL"))
 
        self.table.show()
        
        
if __name__ == "__main__":
    program = QApplication([])
    window = ShowAllUsers()
    program.exec()