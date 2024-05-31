from PySide6 import *
from 聊天_ui import Ui_widget

class Mywindow(Ui_widget):
    def __int__(self):
        self.setupUi(self)
        self.setWindowTitle("一个聊天软件")


if __name__ == '__main__':
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()