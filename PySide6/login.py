from PySide6.QtWidgets import QWidget,QApplication,QFileIconProvider
from 登录_ui import Ui_Form

class Mywindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginFuc)
        
    def loginFuc(self):
        # 拿到账号
        account = self.lineEdit.text()
        # 拿到密码
        password = self.lineEdit_2.text()
        if account == "admin" and password == "admin":
            print("登录成功")
        else:
            print("登录失败")

if __name__ == "__main__":
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()