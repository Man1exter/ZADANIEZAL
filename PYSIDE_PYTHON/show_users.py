from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QHeaderView, QMessageBox, QTableWidget, QTableWidgetItem, QWidget
from PySide6.QtGui import QIcon

class ShowAllUsers(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.table = QTableWidget()
        
        self.table.setColumnCount(2) # nieograniczone kolumny
        self.table.setRowCount(0) # nieograniczone wiersze
        
        self.table.setHorizontalHeaderLabels(["IMIE","NAZWISKO","EMAIL"])
        
        for i in range(10):
            for j in range(10):
                item = QTableWidgetItem(f"({i}, {j})")
                self.table.setItem(i, j, item)

        # Dodaj kolumnę i wiersz do tabelki
        self.table.insertColumn(0)
        self.table.insertRow(0)

        # Wyświetl tabelkę
        self.table.resize(318,250)
        self.table.show()
        
        
if __name__ == "__main__":
    program = QApplication([])
    window = ShowAllUsers()
    program.exec()