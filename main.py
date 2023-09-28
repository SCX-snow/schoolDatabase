#
# Created by slcomplex on 2023/6/21.
#
import sys

import pymysql
import xlwings
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication
from qfluentwidgets import MessageDialog
from qframelesswindow import FramelessMainWindow, StandardTitleBar

from UILoginWindow import UI_LoginWindow
from UIMainWindow import Ui_MainWindow


class LoginWindow(FramelessMainWindow, UI_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.raise_()
        self.PushButton.clicked.connect(self.login)
        self.teacherid.returnPressed.connect(self.login)
        self.password.returnPressed.connect(self.login)

    def login(self):
        global teacherId, password
        teacherId = self.teacherid.text()
        password = self.password.text()
        try:
            db = pymysql.connect(host='192.168.158.134',
                                 user=teacherId,
                                 password=password,
                                 database='big_job',
                                 charset='utf8')
            cursor = db.cursor()
            cursor.execute("SELECT VERSION()")
            db.commit()
            db.close()
            self.close()
            ww.show()
            ww.activateWindow()
            ww.startF()
        except pymysql.Error:
            f = MessageDialog('登录失败', '登录失败,请检查', self)
            f.exec()


class MainWindow(FramelessMainWindow, Ui_MainWindow):
    def __init__(self):
        self.model = QStandardItemModel()
        global teacherId, password
        super().__init__()
        self.setupUi(self)
        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.raise_()
        self.fileout.setEnabled(False)
        self.TableView.setSortingEnabled(True)
        self.table.clicked.connect(self.tabelShow)
        self.id.currentIndexChanged.connect(self.edit)
        self.commit.clicked.connect(self.submit)
        self.fileout.clicked.connect(self.fileoutB)
        self.peacetimescore.valueChanged.connect(self.scoreChange)
        self.bigworkscore.valueChanged.connect(self.scoreChange)
        self.examscore.valueChanged.connect(self.scoreChange)

    def startF(self):
        try:
            db = pymysql.connect(host='192.168.158.134',
                                 user=teacherId,
                                 password=password,
                                 database='big_job',
                                 charset='utf8')
            cursor = db.cursor()
            sql = "SELECT Course_id FROM Course WHERE Teacher_id = %s" % teacherId
            cursor.execute(sql)
            data = cursor.fetchall()
            db.close()
            for i in range(len(data)):
                self.ComboBox.addItem(str(data[i][0]))
            self.ComboBox.setCurrentIndex(0)
        except pymysql.Error:
            f = MessageDialog('错误', '致命错误,程序退出', self)
            f.exec()
            self.close()

    def tabelShow(self):
        try:
            db = pymysql.connect(host='192.168.158.134',
                                 user=teacherId,
                                 password=password,
                                 database='big_job',
                                 charset='utf8')
            cursor = db.cursor()
            sql = "SELECT Student.Student_name,Studen_Course.Student_id,Student.Class_id," \
                  "Studen_Course.Achievement_peacetime,Studen_Course.Achievement_bighomework," \
                  "Studen_Course.Achievement_exam FROM Studen_Course INNER JOIN Student ON " \
                  "Student.Student_id=Studen_Course.Student_id WHERE Course_id = %s" % (
                      self.ComboBox.currentText())
            cursor.execute(sql)
            data = cursor.fetchall()
            db.close()
            self.model.setHorizontalHeaderLabels(
                ['姓名', '学号', '班级', '平时成绩', '大作业成绩', '考试成绩', '总成绩'])
            for i in range(len(data)):
                for j in range(6):
                    k = QStandardItem(str(data[i][j]))
                    self.model.setItem(i, j, k)
                k = QStandardItem(str(data[i][3] * 0.4 + data[i][4] * 0.1 + data[i][5] * 0.5))
                self.model.setItem(i, 6, k)
            self.TableView.setModel(self.model)
            self.id.clear()
            for i in range(len(data)):
                self.id.addItem(str(data[i][1]))
            self.id.setCurrentIndex(0)
            self.edit()
            self.fileout.setEnabled(True)
            self.TableView.selectionModel().currentChanged.connect(self.tableC)
            self.TableView.sortByColumn(1, Qt.AscendingOrder)
        except pymysql.Error:
            f = MessageDialog('错误', '致命错误,程序退出', self)
            f.exec()
            self.close()

    def edit(self):
        for i in range(self.model.rowCount()):
            if self.model.data(self.model.index(i, 1)) == self.id.currentText():
                self.TableView.setCurrentIndex(self.model.index(i, 0))
                self.name.setText(self.model.data(self.model.index(i, 0)))
                self.class_2.setText(self.model.data(self.model.index(i, 2)))
                self.peacetimescore.setValue(float(self.model.data(self.model.index(i, 3))))
                self.bigworkscore.setValue(float(self.model.data(self.model.index(i, 4))))
                self.examscore.setValue(float(self.model.data(self.model.index(i, 5))))
                self.aimscore.setText(str((float(self.model.data(self.model.index(i, 3)))) * 0.4 + (
                        float(self.model.data(self.model.index(i, 4))) * 0.1 + (float(self.model.data(self.model.index(i, 5)))) * 0.5)))

    def submit(self):
        try:
            db = pymysql.connect(host='192.168.158.134',
                                 user=teacherId,
                                 password=password,
                                 database='big_job',
                                 charset='utf8')
            cursor = db.cursor()
            sql = "UPDATE Studen_Course SET Achievement_peacetime = %d ,Achievement_bighomework = %d ,Achievement_exam = %d WHERE Student_id = %s" % (
                self.peacetimescore.value(), self.bigworkscore.value(), self.examscore.value(), self.id.currentText())
            cursor.execute(sql)
            db.commit()
            db.close()
        except pymysql.Error:
            f = MessageDialog('错误', '致命错误,程序退出', self)
            f.exec()
            self.close()
        self.model.setItem(self.TableView.currentIndex().row(), 3, QStandardItem(self.peacetimescore.text()))
        self.model.setItem(self.TableView.currentIndex().row(), 4, QStandardItem(self.bigworkscore.text()))
        self.model.setItem(self.TableView.currentIndex().row(), 5, QStandardItem(self.examscore.text()))
        self.model.setItem(self.TableView.currentIndex().row(), 6, QStandardItem(self.aimscore.text()))

    def scoreChange(self):
        self.aimscore.setText('%.1f' % (
                self.peacetimescore.value() * 0.4 + self.bigworkscore.value() * 0.1 + self.examscore.value() * 0.5))

    def tableC(self):
        self.id.setCurrentText(self.model.index(self.TableView.currentIndex().row(), 1).data())
        self.edit()

    def fileoutB(self):
        xApp = xlwings.App(visible=False, add_book=False)
        wb = xApp.books.add()
        sheet = wb.sheets.add()
        sheet[0, 0].value = '%s班成绩单.xlsx' % (self.ComboBox.text())
        sheet.range((1, 1), (1, self.model.columnCount())).api.Merge()
        sheet[0, 0].api.HorizontalAlignment = -4108
        for i in range(self.model.columnCount()):
            sheet[1, i].value = self.model.headerData(i, Qt.Horizontal)
        for i in range(self.model.rowCount()):
            for j in range(self.model.columnCount()):
                sheet[2 + i, j].value = self.model.index(i, j).data()
        wb.save('%s班成绩单.xlsx' % (self.ComboBox.text()))
        wb.close()
        xApp.quit()
        f = MessageDialog('成功', '导出成功', self)
        f.exec()


if __name__ == '__main__':
    teacherId = str()
    password = str()
    app = QApplication(sys.argv)
    w = LoginWindow()
    ww = MainWindow()
    w.show()
    app.exec()
