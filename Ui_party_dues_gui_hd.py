# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\workspace\cuebpartydues\party_dues_gui_hd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(931, 640)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("party.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setEnabled(False)
        self.calculateButton.setGeometry(QtCore.QRect(770, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.calculateButton.setFont(font)
        self.calculateButton.setCheckable(False)
        self.calculateButton.setChecked(False)
        self.calculateButton.setAutoDefault(False)
        self.calculateButton.setObjectName("calculateButton")
        self.aboutLabel = QtWidgets.QLabel(self.centralwidget)
        self.aboutLabel.setGeometry(QtCore.QRect(290, 600, 351, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.aboutLabel.setFont(font)
        self.aboutLabel.setObjectName("aboutLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 70, 621, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setGeometry(QtCore.QRect(770, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.importButton.setFont(font)
        self.importButton.setObjectName("importButton")
        self.filepathLabel = QtWidgets.QLabel(self.centralwidget)
        self.filepathLabel.setGeometry(QtCore.QRect(30, 60, 91, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.filepathLabel.setFont(font)
        self.filepathLabel.setObjectName("filepathLabel")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(330, 10, 261, 49))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.welcomeLabel.setScaledContents(False)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.GTBox = QtWidgets.QGroupBox(self.centralwidget)
        self.GTBox.setGeometry(QtCore.QRect(10, 190, 911, 421))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.GTBox.setFont(font)
        self.GTBox.setAlignment(QtCore.Qt.AlignCenter)
        self.GTBox.setFlat(True)
        self.GTBox.setCheckable(False)
        self.GTBox.setObjectName("GTBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.GTBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 891, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 5, 10, 10)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.TeachingList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.TeachingList.setEnabled(False)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.TeachingList.setFont(font)
        self.TeachingList.setObjectName("TeachingList")
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TeachingList.addItem(item)
        self.gridLayout.addWidget(self.TeachingList, 1, 1, 1, 1)
        self.OtherSpecialtyList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.OtherSpecialtyList.setEnabled(False)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.OtherSpecialtyList.setFont(font)
        self.OtherSpecialtyList.setObjectName("OtherSpecialtyList")
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.OtherSpecialtyList.addItem(item)
        self.gridLayout.addWidget(self.OtherSpecialtyList, 1, 4, 1, 1)
        self.OtherSpecialtyPosition = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.OtherSpecialtyPosition.setEnabled(False)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.OtherSpecialtyPosition.setFont(font)
        self.OtherSpecialtyPosition.setObjectName("OtherSpecialtyPosition")
        self.gridLayout.addWidget(self.OtherSpecialtyPosition, 0, 4, 1, 1)
        self.TeachingPosition = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.TeachingPosition.setEnabled(False)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.TeachingPosition.setFont(font)
        self.TeachingPosition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TeachingPosition.setAutoFillBackground(False)
        self.TeachingPosition.setCheckable(True)
        self.TeachingPosition.setChecked(True)
        self.TeachingPosition.setObjectName("TeachingPosition")
        self.gridLayout.addWidget(self.TeachingPosition, 0, 1, 1, 1)
        self.workerList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.workerList.setEnabled(False)
        self.workerList.setObjectName("workerList")
        item = QtWidgets.QListWidgetItem()
        self.workerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.workerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.workerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.workerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.workerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.workerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.workerList.addItem(item)
        self.gridLayout.addWidget(self.workerList, 1, 5, 1, 1)
        self.workerPosition = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.workerPosition.setEnabled(False)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.workerPosition.setFont(font)
        self.workerPosition.setCheckable(True)
        self.workerPosition.setObjectName("workerPosition")
        self.gridLayout.addWidget(self.workerPosition, 0, 5, 1, 1)
        self.ManagementList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.ManagementList.setEnabled(False)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ManagementList.setFont(font)
        self.ManagementList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ManagementList.setProperty("isWrapping", False)
        self.ManagementList.setObjectName("ManagementList")
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        item.setFont(font)
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ManagementList.addItem(item)
        self.gridLayout.addWidget(self.ManagementList, 1, 2, 1, 1)
        self.ManagementPosition = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.ManagementPosition.setEnabled(False)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ManagementPosition.setFont(font)
        self.ManagementPosition.setCheckable(True)
        self.ManagementPosition.setChecked(False)
        self.ManagementPosition.setObjectName("ManagementPosition")
        self.gridLayout.addWidget(self.ManagementPosition, 0, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 120, 631, 54))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AutoGT = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.AutoGT.setFont(font)
        self.AutoGT.setChecked(True)
        self.AutoGT.setObjectName("AutoGT")
        self.horizontalLayout.addWidget(self.AutoGT)
        self.ManualGT = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ManualGT.setFont(font)
        self.ManualGT.setToolTipDuration(-5)
        self.ManualGT.setObjectName("ManualGT")
        self.horizontalLayout.addWidget(self.ManualGT)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionset = QtWidgets.QAction(MainWindow)
        self.actionset.setEnabled(True)
        self.actionset.setObjectName("actionset")

        self.retranslateUi(MainWindow)
        self.TeachingList.setCurrentRow(9)
        self.OtherSpecialtyList.setCurrentRow(10)
        self.workerList.setCurrentRow(6)
        self.ManagementList.setCurrentRow(15)
        self.ManualGT.clicked['bool'].connect(self.ManagementPosition.setEnabled)
        self.AutoGT.clicked['bool'].connect(self.GTBox.setDisabled)
        self.ManualGT.clicked['bool'].connect(self.TeachingPosition.setEnabled)
        self.ManualGT.clicked['bool'].connect(self.OtherSpecialtyPosition.setEnabled)
        self.OtherSpecialtyPosition.clicked['bool'].connect(self.OtherSpecialtyList.setEnabled)
        self.TeachingPosition.clicked['bool'].connect(self.TeachingList.setEnabled)
        self.OtherSpecialtyPosition.clicked['bool'].connect(self.ManagementList.setDisabled)
        self.OtherSpecialtyPosition.clicked['bool'].connect(self.TeachingList.setDisabled)
        self.TeachingPosition.clicked['bool'].connect(self.ManagementList.setDisabled)
        self.TeachingPosition.clicked['bool'].connect(self.OtherSpecialtyList.setDisabled)
        self.ManagementPosition.clicked['bool'].connect(self.ManagementList.setEnabled)
        self.ManagementPosition.clicked['bool'].connect(self.TeachingList.setDisabled)
        self.ManagementPosition.clicked['bool'].connect(self.OtherSpecialtyList.setDisabled)
        self.ManualGT.clicked['bool'].connect(self.GTBox.setEnabled)
        self.ManualGT.clicked['bool'].connect(self.TeachingPosition.click)
        self.ManualGT.clicked['bool'].connect(self.workerPosition.setEnabled)
        self.workerPosition.clicked['bool'].connect(self.workerList.setEnabled)
        self.workerPosition.clicked['bool'].connect(self.OtherSpecialtyList.setDisabled)
        self.workerPosition.clicked['bool'].connect(self.TeachingList.setDisabled)
        self.workerPosition.clicked['bool'].connect(self.ManagementList.setDisabled)
        self.ManagementPosition.clicked['bool'].connect(self.workerList.setDisabled)
        self.TeachingPosition.clicked['bool'].connect(self.workerList.setDisabled)
        self.OtherSpecialtyPosition.clicked['bool'].connect(self.workerList.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CUEB教职工党费计算器"))
        self.calculateButton.setText(_translate("MainWindow", "生成缴费表"))
        self.aboutLabel.setText(_translate("MainWindow", "作者：许博祥   单位：工商管理学院   邮箱：xbx@cueb.edu.cn "))
        self.importButton.setText(_translate("MainWindow", "导入工资文件"))
        self.filepathLabel.setText(_translate("MainWindow", "工资文件路径："))
        self.welcomeLabel.setText(_translate("MainWindow", "欢迎使用CUEB教职工党费计算器！"))
        self.GTBox.setTitle(_translate("MainWindow", "手动选择岗贴标准"))
        __sortingEnabled = self.TeachingList.isSortingEnabled()
        self.TeachingList.setSortingEnabled(False)
        item = self.TeachingList.item(0)
        item.setText(_translate("MainWindow", "教授一级"))
        item = self.TeachingList.item(1)
        item.setText(_translate("MainWindow", "教授二级"))
        item = self.TeachingList.item(2)
        item.setText(_translate("MainWindow", "教授三级"))
        item = self.TeachingList.item(3)
        item.setText(_translate("MainWindow", "教授四级"))
        item = self.TeachingList.item(4)
        item.setText(_translate("MainWindow", "副教授一级"))
        item = self.TeachingList.item(5)
        item.setText(_translate("MainWindow", "副教授二级"))
        item = self.TeachingList.item(6)
        item.setText(_translate("MainWindow", "副教授三级"))
        item = self.TeachingList.item(7)
        item.setText(_translate("MainWindow", "讲师一级"))
        item = self.TeachingList.item(8)
        item.setText(_translate("MainWindow", "讲师二级"))
        item = self.TeachingList.item(9)
        item.setText(_translate("MainWindow", "讲师三级"))
        item = self.TeachingList.item(10)
        item.setText(_translate("MainWindow", "助教一级"))
        item = self.TeachingList.item(11)
        item.setText(_translate("MainWindow", "助教二级"))
        self.TeachingList.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.OtherSpecialtyList.isSortingEnabled()
        self.OtherSpecialtyList.setSortingEnabled(False)
        item = self.OtherSpecialtyList.item(0)
        item.setText(_translate("MainWindow", "其他专业技术三级"))
        item = self.OtherSpecialtyList.item(1)
        item.setText(_translate("MainWindow", "其他专业技术四级"))
        item = self.OtherSpecialtyList.item(2)
        item.setText(_translate("MainWindow", "其他专业技术五级"))
        item = self.OtherSpecialtyList.item(3)
        item.setText(_translate("MainWindow", "其他专业技术六级"))
        item = self.OtherSpecialtyList.item(4)
        item.setText(_translate("MainWindow", "其他专业技术七级"))
        item = self.OtherSpecialtyList.item(5)
        item.setText(_translate("MainWindow", "其他专业技术八级"))
        item = self.OtherSpecialtyList.item(6)
        item.setText(_translate("MainWindow", "其他专业技术九级"))
        item = self.OtherSpecialtyList.item(7)
        item.setText(_translate("MainWindow", "其他专业技术十级"))
        item = self.OtherSpecialtyList.item(8)
        item.setText(_translate("MainWindow", "其他专业技术十一级"))
        item = self.OtherSpecialtyList.item(9)
        item.setText(_translate("MainWindow", "其他专业技术十二级"))
        item = self.OtherSpecialtyList.item(10)
        item.setText(_translate("MainWindow", "其他专业技术十三级"))
        self.OtherSpecialtyList.setSortingEnabled(__sortingEnabled)
        self.OtherSpecialtyPosition.setText(_translate("MainWindow", "其他专业技术岗位"))
        self.TeachingPosition.setText(_translate("MainWindow", "教学岗位"))
        __sortingEnabled = self.workerList.isSortingEnabled()
        self.workerList.setSortingEnabled(False)
        item = self.workerList.item(0)
        item.setText(_translate("MainWindow", "技师"))
        item = self.workerList.item(1)
        item.setText(_translate("MainWindow", "高级工，工作年限30年（含）以上"))
        item = self.workerList.item(2)
        item.setText(_translate("MainWindow", "高级工，工作年限20年（含）以上"))
        item = self.workerList.item(3)
        item.setText(_translate("MainWindow", "高级工，工作年限20年以下；\n"
"中级工，工作年限30年（含）以上"))
        item = self.workerList.item(4)
        item.setText(_translate("MainWindow", "中级工，工作年限20年（含）以上"))
        item = self.workerList.item(5)
        item.setText(_translate("MainWindow", "中级工工作年限20年以下；\n"
"初级工（普工），工作年限30年\n"
"（含）以上"))
        item = self.workerList.item(6)
        item.setText(_translate("MainWindow", "初级工（普工）"))
        self.workerList.setSortingEnabled(__sortingEnabled)
        self.workerPosition.setText(_translate("MainWindow", "工勤岗位"))
        __sortingEnabled = self.ManagementList.isSortingEnabled()
        self.ManagementList.setSortingEnabled(False)
        item = self.ManagementList.item(0)
        item.setText(_translate("MainWindow", "正校级"))
        item = self.ManagementList.item(1)
        item.setText(_translate("MainWindow", "副校级"))
        item = self.ManagementList.item(2)
        item.setText(_translate("MainWindow", "党委常委/校长助理"))
        item = self.ManagementList.item(3)
        item.setText(_translate("MainWindow", "任正处级12年（含）以上"))
        item = self.ManagementList.item(4)
        item.setText(_translate("MainWindow", "任正处级6年（含）以上"))
        item = self.ManagementList.item(5)
        item.setText(_translate("MainWindow", "任正处级6年以下"))
        item = self.ManagementList.item(6)
        item.setText(_translate("MainWindow", "任副处级12年（含）以上"))
        item = self.ManagementList.item(7)
        item.setText(_translate("MainWindow", "任副处级6年（含）以上"))
        item = self.ManagementList.item(8)
        item.setText(_translate("MainWindow", "任副处级6年以下"))
        item = self.ManagementList.item(9)
        item.setText(_translate("MainWindow", "正科级，工作年限25年（含）以上"))
        item = self.ManagementList.item(10)
        item.setText(_translate("MainWindow", "正科级，工作年限10年（含）以上"))
        item = self.ManagementList.item(11)
        item.setText(_translate("MainWindow", "副科级，工作年限25年（含）以上；\n"
"正科级，工作年限10年以下"))
        item = self.ManagementList.item(12)
        item.setText(_translate("MainWindow", "副科级，工作年限10年（含）以上"))
        item = self.ManagementList.item(13)
        item.setText(_translate("MainWindow", "科员，工作年限25年（含）以上；\n"
"副科级，工作年限10年以下"))
        item = self.ManagementList.item(14)
        item.setText(_translate("MainWindow", "科员，工作年限10年（含）以上"))
        item = self.ManagementList.item(15)
        item.setText(_translate("MainWindow", "科员，工作年限10年以下"))
        item = self.ManagementList.item(16)
        item.setText(_translate("MainWindow", "办事员"))
        self.ManagementList.setSortingEnabled(__sortingEnabled)
        self.ManagementPosition.setText(_translate("MainWindow", "党政管理岗位"))
        self.AutoGT.setText(_translate("MainWindow", "读取工资文件内的岗贴数字自动计算党费\n"
"（主要适用于【非教学岗位】。教学岗位的\n"
"工资文件一般无岗贴栏目，请不要选择此项）"))
        self.ManualGT.setText(_translate("MainWindow", "手动选择岗贴标准后计算党费\n"
"(主要适用于【教学岗位】。如果非教学岗位的工资\n"
"文件内的岗贴栏目数字不准确，也可选择此项)"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#aa0000;\">特别提示：</span>无论计算<span style=\" font-weight:600; text-decoration: underline; color:#aa0000;\">第几季度</span>的党费，</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入的工资文件<span style=\" font-weight:600; text-decoration: underline; color:#aa0000;\">必须从【1月】开始</span>，</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">否则会<span style=\" font-weight:600; text-decoration: underline; color:#aa0000;\">计算出错</span>或者<span style=\" font-weight:600; text-decoration: underline; color:#aa0000;\">生成缴费表失败</span>！</p></body></html>"))
        self.actionImport.setText(_translate("MainWindow", "导入工资文件"))
        self.actionset.setText(_translate("MainWindow", "岗贴自定义设置"))

