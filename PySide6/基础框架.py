from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()


        mainlayout = QVBoxLayout()
        self.setLayout(mainlayout)

if __name__ == '__main__':
    app = QApplication([])#sys.argv
    window = MyWindow()
    window.show()
    app.exec()