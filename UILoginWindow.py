# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
                               QStatusBar, QWidget, QLineEdit)

from qfluentwidgets import (LineEdit, PushButton)


class UI_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(544, 240)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.teacherid = LineEdit(self.centralwidget)
        self.teacherid.setObjectName(u"teacherid")
        self.teacherid.setGeometry(QRect(170, 60, 321, 33))
        self.password = LineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(170, 110, 321, 33))
        self.password.setEchoMode(LineEdit.Password)
        self.PushButton = PushButton(self.centralwidget)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(220, 160, 102, 32))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 60, 71, 31))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 110, 54, 31))
        self.label_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PushButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6559\u5e08\u7f16\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
    # retranslateUi
