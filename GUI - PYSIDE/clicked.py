from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.button = QPushButton('Otwórz nowe okno')
        self.button.clicked.connect(self.on_button_clicked)

        self.setCentralWidget(self.button)

    def on_button_clicked(self):
        new_window = QMainWindow()
        new_window.show()

if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec_()

