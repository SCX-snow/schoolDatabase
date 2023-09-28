# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
                               QSizePolicy, QStatusBar, QWidget, QComboBox, QAbstractItemView)

from qfluentwidgets import (DoubleSpinBox, PushButton, ComboBox, TableView)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TableView = TableView(self.centralwidget)
        self.TableView.setObjectName(u"TableView")
        self.TableView.setGeometry(QRect(30, 20, 740, 290))
        self.TableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 340, 41, 21))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 340, 41, 21))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 340, 41, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 340, 71, 21))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 340, 101, 21))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(660, 340, 71, 21))
        self.label_6.setFont(font)
        self.commit = PushButton(self.centralwidget)
        self.commit.setObjectName(u"commit")
        self.commit.setGeometry(QRect(820, 400, 102, 32))
        self.peacetimescore = DoubleSpinBox(self.centralwidget)
        self.peacetimescore.setObjectName(u"peacetimescore")
        self.peacetimescore.setGeometry(QRect(290, 370, 133, 33))
        self.peacetimescore.setDecimals(1)
        self.peacetimescore.setMaximum(100.000000000000000)
        self.bigworkscore = DoubleSpinBox(self.centralwidget)
        self.bigworkscore.setObjectName(u"bigworkscore")
        self.bigworkscore.setGeometry(QRect(460, 370, 133, 33))
        self.bigworkscore.setDecimals(1)
        self.examscore = DoubleSpinBox(self.centralwidget)
        self.examscore.setObjectName(u"examscore")
        self.examscore.setGeometry(QRect(630, 370, 133, 33))
        self.examscore.setDecimals(1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(840, 340, 54, 21))
        self.name = QLabel(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 380, 61, 21))
        self.name.setFont(font)
        self.id =  ComboBox(self.centralwidget)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(93, 380, 81, 30))
        self.class_2 = QLabel(self.centralwidget)
        self.class_2.setObjectName(u"class_2")
        self.class_2.setGeometry(QRect(190, 380, 81, 21))
        self.class_2.setFont(font)
        self.aimscore = QLabel(self.centralwidget)
        self.aimscore.setObjectName(u"aimscore")
        self.aimscore.setGeometry(QRect(833, 366, 61, 20))
        self.ComboBox = ComboBox(self.centralwidget)
        self.ComboBox.setObjectName(u"ComboBox")
        self.ComboBox.setGeometry(QRect(800, 40, 113, 33))
        self.fileout = PushButton(self.centralwidget)
        self.fileout.setObjectName(u"fileout")
        self.fileout.setGeometry(QRect(800, 190, 111, 32))
        self.table = PushButton(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(800, 140, 111, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u65f6\u6210\u7ee9", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5927\u4f5c\u4e1a\u6210\u7ee9", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8003\u8bd5\u6210\u7ee9", None))
        self.commit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8ba1\u6210\u7ee9", None))
        self.name.setText("")
        self.class_2.setText("")
        self.aimscore.setText("")
        self.ComboBox.setProperty("text_", QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bfe\u7a0b", None))
        self.fileout.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5bfc\u51fa", None))
        self.table.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d", None))
    # retranslateUi
