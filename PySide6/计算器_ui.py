# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '计算器.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(218, 339)
        icon = QIcon(QIcon.fromTheme(u"address-book-new"))
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.pushButton_5 = QPushButton(Form)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6c5f\u897f\u62d9\u69773.0"])
        font.setPointSize(18)
        self.pushButton_5.setFont(font)

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_minus = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_minus)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)
        self.pushButton_minus.setFont(font)

        self.gridLayout.addWidget(self.pushButton_minus, 2, 3, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFont(font)

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font)

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font)

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_mult = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_mult)
        self.pushButton_mult.setObjectName(u"pushButton_mult")
        sizePolicy.setHeightForWidth(self.pushButton_mult.sizePolicy().hasHeightForWidth())
        self.pushButton_mult.setSizePolicy(sizePolicy)
        self.pushButton_mult.setFont(font)

        self.gridLayout.addWidget(self.pushButton_mult, 1, 3, 1, 1)

        self.pushButton_delete = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_delete)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setFont(font)

        self.gridLayout.addWidget(self.pushButton_delete, 0, 1, 1, 1)

        self.pushButton_add = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_add)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setFont(font)

        self.gridLayout.addWidget(self.pushButton_add, 3, 3, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setFont(font)

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_div = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_div)
        self.pushButton_div.setObjectName(u"pushButton_div")
        sizePolicy.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy)
        self.pushButton_div.setFont(font)

        self.gridLayout.addWidget(self.pushButton_div, 0, 3, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font)

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFont(font)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_equal = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_equal)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        sizePolicy.setHeightForWidth(self.pushButton_equal.sizePolicy().hasHeightForWidth())
        self.pushButton_equal.setSizePolicy(sizePolicy)
        self.pushButton_equal.setFont(font)

        self.gridLayout.addWidget(self.pushButton_equal, 5, 3, 1, 1)

        self.pushButton_yu = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_yu)
        self.pushButton_yu.setObjectName(u"pushButton_yu")
        sizePolicy.setHeightForWidth(self.pushButton_yu.sizePolicy().hasHeightForWidth())
        self.pushButton_yu.setSizePolicy(sizePolicy)
        self.pushButton_yu.setFont(font)

        self.gridLayout.addWidget(self.pushButton_yu, 0, 2, 1, 1)

        self.pushButton_Clear = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_Clear)
        self.pushButton_Clear.setObjectName(u"pushButton_Clear")
        sizePolicy.setHeightForWidth(self.pushButton_Clear.sizePolicy().hasHeightForWidth())
        self.pushButton_Clear.setSizePolicy(sizePolicy)
        self.pushButton_Clear.setFont(font)

        self.gridLayout.addWidget(self.pushButton_Clear, 0, 0, 1, 1)

        self.pushButton_dot = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_dot)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        sizePolicy.setHeightForWidth(self.pushButton_dot.sizePolicy().hasHeightForWidth())
        self.pushButton_dot.setSizePolicy(sizePolicy)
        self.pushButton_dot.setFont(font)

        self.gridLayout.addWidget(self.pushButton_dot, 5, 2, 1, 1)

        self.pushButton_10 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setFont(font)

        self.gridLayout.addWidget(self.pushButton_10, 5, 0, 1, 2)

        self.pushButton_6 = QPushButton(Form)
        self.buttonGroup.addButton(self.pushButton_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setFont(font)

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 100))
        font1 = QFont()
        font1.setPointSize(48)
        self.lineEdit.setFont(font1)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("Form", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_minus.setText(QCoreApplication.translate("Form", u"-", None))
#if QT_CONFIG(shortcut)
        self.pushButton_minus.setShortcut(QCoreApplication.translate("Form", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
#if QT_CONFIG(shortcut)
        self.pushButton_8.setShortcut(QCoreApplication.translate("Form", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("Form", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Form", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("Form", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("Form", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_mult.setText(QCoreApplication.translate("Form", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_mult.setShortcut(QCoreApplication.translate("Form", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_delete.setText(QCoreApplication.translate("Form", u"\u2190", None))
#if QT_CONFIG(shortcut)
        self.pushButton_delete.setShortcut(QCoreApplication.translate("Form", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
#if QT_CONFIG(shortcut)
        self.pushButton_add.setShortcut(QCoreApplication.translate("Form", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
#if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("Form", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_div.setShortcut(QCoreApplication.translate("Form", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("Form", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("Form", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_equal.setText(QCoreApplication.translate("Form", u"=", None))
#if QT_CONFIG(shortcut)
        self.pushButton_equal.setShortcut(QCoreApplication.translate("Form", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_yu.setText(QCoreApplication.translate("Form", u"%", None))
#if QT_CONFIG(shortcut)
        self.pushButton_yu.setShortcut(QCoreApplication.translate("Form", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Clear.setText(QCoreApplication.translate("Form", u"C", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Clear.setShortcut(QCoreApplication.translate("Form", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
#if QT_CONFIG(shortcut)
        self.pushButton_dot.setShortcut(QCoreApplication.translate("Form", u".", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_10.setShortcut(QCoreApplication.translate("Form", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("Form", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"1+1=", None))
    # retranslateUi

