# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainhome.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_right = QtWidgets.QFrame(self.centralwidget)
        self.frame_right.setGeometry(QtCore.QRect(210, 20, 531, 361))
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.frame_left = QtWidgets.QFrame(self.centralwidget)
        self.frame_left.setGeometry(QtCore.QRect(20, 20, 171, 361))
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.pushButton_one = QtWidgets.QPushButton(self.frame_left)
        self.pushButton_one.setGeometry(QtCore.QRect(40, 80, 80, 22))
        self.pushButton_one.setObjectName("pushButton_one")
        self.pushButton_two = QtWidgets.QPushButton(self.frame_left)
        self.pushButton_two.setGeometry(QtCore.QRect(40, 160, 80, 22))
        self.pushButton_two.setObjectName("pushButton_two")
        self.pushButton_three = QtWidgets.QPushButton(self.frame_left)
        self.pushButton_three.setGeometry(QtCore.QRect(40, 250, 80, 22))
        self.pushButton_three.setObjectName("pushButton_three")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_one.setText(_translate("MainWindow", "one"))
        self.pushButton_two.setText(_translate("MainWindow", "two"))
        self.pushButton_three.setText(_translate("MainWindow", "three"))
