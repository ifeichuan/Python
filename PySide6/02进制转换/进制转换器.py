from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QFont
from UI_ui import Ui_Form

class Mywindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lenghtVar = {'米':100,'厘米':1,'千米':10000,'分米':10}
        self.weightVar={'克':1,'千克':1000,'斤':500}
        font = QFont()
        font.setPixelSize(200)
        font.setFamily("")
        self.label_1.setFont(font)
        self.TypeDict = {'长度':self.lenghtVar,'质量':self.weightVar}
        self.comboBox_3.addItems(self.TypeDict.keys())
        self.comboBox_1.addItems(self.lenghtVar.keys())
        self.comboBox_2.addItems(self.lenghtVar.keys())
        self.bind()

    def bind(self):
        self.comboBox_3.currentTextChanged.connect(self.typeChanged)
        self.pushButton.clicked.connect(self.calculate)
    
    def calculate(self):
        value = self.lineEdit_2.text()
        if value == '':
            return 
        currentType = self.comboBox_1.currentText()
        transType = self.comboBox_2.currentText()
        datatype = self.comboBox_3.currentText()
        standardization = float(value) * self.TypeDict[datatype][currentType]
        result = standardization/self.TypeDict[datatype][transType]
        self.label_2.setText(f'{value} {currentType} = ')
        self.label_1.setText(f"{result} {transType}")
        self.lineEdit_2.setText(str(result))
    
    def typeChanged(self,text):
        self.comboBox_1.clear()
        self.comboBox_2.clear()
        self.comboBox_2.addItems(self.TypeDict[text].keys())
        self.comboBox_1.addItems(self.TypeDict[text].keys())

        
    
if __name__ == '__main__':
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()