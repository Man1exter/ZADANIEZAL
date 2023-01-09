from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QHeaderView, QMessageBox, QTableWidget, QTableWidgetItem, QWidget
from PySide6.QtGui import QColor
from PySide6.QtGui import QIcon

class ShowAllUsers(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.table = QTableWidget()
        
        self.table.setColumnCount(2) # nieograniczone kolumny max [3 -> od 0]
        self.table.setRowCount(0) # nieograniczone wiersze
        
        #for i in range(10):
            #for j in range(10):  # dodawanie le do tabelki!
                #item = QTableWidgetItem(f"({i}, {j})")
                #self.table.setItem(i, j, item)

        # Dodaj kolumnę i wiersz do tabelki
        self.table.insertColumn(0)
        self.table.insertRow(0)
        
        self.table.setHorizontalHeaderLabels(["IMIE:","NAZWISKO:","EMAIL:"])

        # Wyświetl tabelkę
        self.table.resize(925,550)
        
        for i in range(3):
          self.table.setColumnWidth(i,300)
        
        self.table.show()
        
        
if __name__ == "__main__":
    program = QApplication([])
    window = ShowAllUsers()
    program.exec()