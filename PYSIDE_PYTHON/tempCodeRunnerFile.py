if __name__ == "__main__":
    program = QApplication([])
    window = MainWindow()
    
    window.resize(400,300)
    window.setWindowTitle("🐷 WYPOŻYCZALNIA ŚWINEK")
    window.setStyleSheet("background-color: lightblue;")
    window.setWindowIcon(QIcon("pig.png"))
    
    window.show()
    program.exec()