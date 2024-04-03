from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.btn1 = QPushButton("按钮1")
        self.btn1.clicked.connect(self.btn_clicked)
        self.label1 = QLabel("标签1")
        self.label1.setText("标签1被修改了")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineedit1 = QLineEdit()
        self.lineedit1.setPlaceholderText("请输入:")
        font1 = QFont()
        font1.setBold(True)
        font1.setFamilies("奶油")
        self.lineedit1.setFont(font1)
        
        self.lineedit1.setEchoMode(QLineEdit.EchoMode.Password)
        #布局
        layout.addWidget(self.label1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.btn1)
        self.setLayout(layout)

    def btn_clicked(self):
        print("按钮btn1被点击")

if __name__ == '__main__':
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()