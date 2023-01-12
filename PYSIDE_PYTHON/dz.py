from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtGui import QIcon
#from reg_user import RegUsers


class OtherClass:
    def __init__(self):
        self.value = 5

class MyClass:
    def __init__(self):
        self.table = QTableWidget()
        other_class = OtherClass()
        item = QTableWidgetItem(str(other_class.value))
        self.table.setItem(0, 0, item)
        