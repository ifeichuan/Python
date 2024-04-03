from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QMessageBox


class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,200)

        self.btn = QPushButton("按钮")
        self.btn.clicked.connect(self.btn_clicked)
        self.setWindowTitle("Qmessage")
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.btn)
        self.setLayout(self.mainlayout)

    def btn_clicked(self):
        # QMessageBox.about(self,"你好","你好世界") 普通
        # QMessageBox.aboutQt(self,"你好") Qt自带介绍
        # QMessageBox.critical(self,"你好","你好") 警告
        # QMessageBox.information(self,"你好","你好") 信息
        # QMessageBox.warning(self,"你好","年后")
        replay = QMessageBox.question(self,"111","222",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        return replay
    
if __name__ == '__main__':
    app = QApplication([])
    window = myWindow()
    window.show()
    app.exec()