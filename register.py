# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import sqlite3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RegisterWindow(object):
    def insert(self):
        conn=sqlite3.connect('drug.db')
        a=str(self.lineEdit.text())
        b=str(self.lineEdit_2.text())
        c=str(self.lineEdit_3.text())
        d=str(self.lineEdit_4.text())
        conn.execute("INSERT INTO drugs (Name,MFD,ED,Quantity) VALUES (?,?,?,?)",(a,b,c,d))
        conn.commit()
        QMessageBox.information(QWidget(),"Information",'Succesfully Saved')

    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()


    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName(_fromUtf8("RegisterWindow"))
        RegisterWindow.resize(466, 374)
        self.centralwidget = QtGui.QWidget(RegisterWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 171, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 120, 171, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 180, 171, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 280, 75, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.insert)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 280, 75, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_2.clicked.connect(self.clear)

        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 230, 171, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "RegisterWindow", None))
        self.label.setText(_translate("RegisterWindow", "REGISTER DRUG", None))
        self.label_2.setText(_translate("RegisterWindow", "DRUG NAME:", None))
        self.label_3.setText(_translate("RegisterWindow", "MANUFACTURED DATE:", None))
        self.label_4.setText(_translate("RegisterWindow", "EXPIRED DATE:", None))
        self.pushButton.setText(_translate("RegisterWindow", "SAVE", None))
        self.pushButton_2.setText(_translate("RegisterWindow", "CLEAR", None))
        self.label_5.setText(_translate("RegisterWindow", "QUANTITY:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RegisterWindow = QtGui.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())

