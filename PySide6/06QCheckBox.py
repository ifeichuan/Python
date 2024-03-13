from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QCheckBox,QSwitch


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        cb = QCheckBox("是否选中")
        cb.stateChanged.connect(self.showstate)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)

    def showstate(self,state):
        print(state)

if __name__ == '__main__':
    app = QApplication([])#sys.argv
    window = MyWindow()
    window.show()
    app.exec()