# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\xbx\Desktop\pack\party_dues_gui_hd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(581, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("communist.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setEnabled(False)
        self.calculateButton.setGeometry(QtCore.QRect(210, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.calculateButton.setFont(font)
        self.calculateButton.setCheckable(False)
        self.calculateButton.setChecked(False)
        self.calculateButton.setAutoDefault(False)
        self.calculateButton.setObjectName("calculateButton")
        self.aboutLabel = QtWidgets.QLabel(self.centralwidget)
        self.aboutLabel.setGeometry(QtCore.QRect(130, 180, 331, 39))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.aboutLabel.setFont(font)
        self.aboutLabel.setObjectName("aboutLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 70, 319, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setGeometry(QtCore.QRect(460, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.importButton.setFont(font)
        self.importButton.setObjectName("importButton")
        self.filepathLabel = QtWidgets.QLabel(self.centralwidget)
        self.filepathLabel.setGeometry(QtCore.QRect(20, 60, 91, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.filepathLabel.setFont(font)
        self.filepathLabel.setObjectName("filepathLabel")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(160, 10, 241, 49))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.welcomeLabel.setScaledContents(False)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionset = QtWidgets.QAction(MainWindow)
        self.actionset.setEnabled(True)
        self.actionset.setObjectName("actionset")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CUEB教师党费计算器"))
        self.calculateButton.setText(_translate("MainWindow", "生成缴费表"))
        self.aboutLabel.setText(_translate("MainWindow", "作者：许博祥 单位：工商管理学院 邮箱：xbx@cueb.edu.cn"))
        self.importButton.setText(_translate("MainWindow", "导入工资文件"))
        self.filepathLabel.setText(_translate("MainWindow", "工资文件路径："))
        self.welcomeLabel.setText(_translate("MainWindow", "欢迎使用CUEB教师党费计算器！"))
        self.actionImport.setText(_translate("MainWindow", "导入工资文件"))
        self.actionset.setText(_translate("MainWindow", "岗贴自定义设置"))

