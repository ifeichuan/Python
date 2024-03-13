from PySide6.QtWidgets import QApplication,QWidget
from 计算器_ui import Ui_Form

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("一个简单的计算器")
        self.result = ''
        self.bind()

    def bind(self):
        self.pushButton.clicked.connect(lambda:self.addNumber('1'))
        self.pushButton_2.clicked.connect(lambda:self.addNumber('2'))
        self.pushButton_3.clicked.connect(lambda:self.addNumber('3'))
        self.pushButton_4.clicked.connect(lambda:self.addNumber('4'))
        self.pushButton_5.clicked.connect(lambda:self.addNumber('5'))
        self.pushButton_6.clicked.connect(lambda:self.addNumber('6'))
        self.pushButton_7.clicked.connect(lambda:self.addNumber('7'))
        self.pushButton_8.clicked.connect(lambda:self.addNumber('8'))
        self.pushButton_9.clicked.connect(lambda:self.addNumber('9'))
        self.pushButton_10.clicked.connect(lambda:self.addNumber('0'))
        self.pushButton_add.clicked.connect(lambda:self.addNumber('+'))
        self.pushButton_minus.clicked.connect(lambda:self.addNumber('-'))
        self.pushButton_div.clicked.connect(lambda:self.addNumber('/'))
        self.pushButton_delete.clicked.connect(lambda:self.back())
        self.pushButton_mult.clicked.connect(lambda:self.addNumber('*'))
        self.pushButton_yu.clicked.connect(lambda:self.addNumber('%'))
        self.pushButton_equal.clicked.connect(lambda:self.equal())
        self.pushButton_Clear.clicked.connect(lambda:self.clear())
        print(str)
    def addNumber(self,number):
        self.lineEdit.clear()
        self.result +=number
        self.lineEdit.setText(self.result)
    def equal(self):
        self.numberResult = eval(self.result)
        self.lineEdit.setText(str(self.numberResult))
        self.result = str(self.numberResult)
    def clear(self):
        self.lineEdit.clear()
        self.result = '0'
    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)

if __name__ == '__main__':
    app = QApplication([])#sys.argv
    window = MyWindow()
    window.show()
    app.exec()