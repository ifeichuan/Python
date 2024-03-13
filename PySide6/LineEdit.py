from PySide6.QtWidgets import QApplication,QWidget,QLineEdit,QVBoxLayout
from PySide6.QtCore import Qt

from BlurWindow.blurWindow import GlobalBlur

class MyWindow(QWidget):
    def  __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        line = QLineEdit(self)
        line.setPlaceholderText("请输入内容")
        GlobalBlur(self.winId(),Dark=True,QWidget=self)
        self.setStyleSheet("background-color:rgba(0,0,0,0)")
        

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()