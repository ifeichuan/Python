# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1038, 864)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 381, 231))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"\u6c5f\u897f\u62d9\u69773.0"])
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(111,111,111)")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_1 = QLabel(self.layoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u6c5f\u897f\u62d9\u69773.0"])
        font1.setPointSize = 28
        font1.setBold(True)
        self.label_1.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.comboBox_3 = QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(300, 16777215))
        self.comboBox_3.setFont(font)

        self.verticalLayout.addWidget(self.comboBox_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.lineEdit_1 = QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMaximumSize(QSize(300, 40))

        self.gridLayout.addWidget(self.lineEdit_1, 0, 0, 1, 1)

        self.comboBox_1 = QComboBox(self.layoutWidget)
        self.comboBox_1.setObjectName(u"comboBox_1")

        self.gridLayout.addWidget(self.comboBox_1, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.comboBox_2.setCurrentText("")
    # retranslateUi

