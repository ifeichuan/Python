from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton('按钮',self)
        btn.setGeometry(100,100,200,200)
        btn.setToolTip("明治!")
        btn.setText("1+1=2\ne3")
        label = QLabel('# `我`是一个标签',self)
        label.setGeometry(100,120,200,190)
        label.setFont("江西拙楷3.0")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setTextFormat(Qt.TextFormat.MarkdownText)
        line = QLineEdit()
        line.setGeometry(50,50,50,50)
        line.setPlaceholderText("请输入")

if __name__ == '__main__':
    app = QApplication([])#sys.argv
    window = MyWindow()
    window.show()
    app.exec()