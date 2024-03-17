from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QFormLayout,QPushButton,QLabel,QLineEdit


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()

        #登录界面


        self.mainlayout = QVBoxLayout()
        self.userlayout = QHBoxLayout()
        self.userlayout.addWidget(QLabel('用户名'))
        self.userlayout.addWidget(QLineEdit())
        self.mainlayout.addLayout(self.userlayout)
        self.mainlayout.addWidget(QLabel('密码'))
        self.mainlayout.addWidget(QLineEdit())
        self.mainlayout.addWidget(QPushButton('登录'))
        self.setLayout(self.mainlayout)
        

if __name__ == '__main__':
    app =QApplication([])
    window = Mywindow()
    window.show()
    app.exec()