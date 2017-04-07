# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(779, 504)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Find = QtGui.QPushButton(self.centralwidget)
        self.Find.setGeometry(QtCore.QRect(470, 300, 291, 61))
        self.Find.setObjectName(_fromUtf8("Find"))
        self.NameText = QtGui.QTextEdit(self.centralwidget)
        self.NameText.setGeometry(QtCore.QRect(20, 300, 221, 21))
        self.NameText.setObjectName(_fromUtf8("NameText"))
        self.FamilyText = QtGui.QTextEdit(self.centralwidget)
        self.FamilyText.setGeometry(QtCore.QRect(20, 260, 221, 21))
        self.FamilyText.setObjectName(_fromUtf8("FamilyText"))
        self.Name2Text = QtGui.QTextEdit(self.centralwidget)
        self.Name2Text.setGeometry(QtCore.QRect(20, 340, 221, 21))
        self.Name2Text.setObjectName(_fromUtf8("Name2Text"))
        self.Default = QtGui.QPushButton(self.centralwidget)
        self.Default.setGeometry(QtCore.QRect(470, 380, 291, 61))
        self.Default.setObjectName(_fromUtf8("Default"))
        self.textEdit_4 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(260, 260, 191, 21))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(260, 300, 191, 21))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(260, 340, 191, 21))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 0, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 250, 52, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 290, 52, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 330, 52, 14))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 250, 52, 14))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 290, 52, 14))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 330, 101, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.ResultTable = QtGui.QTableWidget(self.centralwidget)
        self.ResultTable.setGeometry(QtCore.QRect(20, 20, 741, 211))
        self.ResultTable.setObjectName(_fromUtf8("ResultTable"))
        self.ResultTable.setColumnCount(0)
        self.ResultTable.setRowCount(0)
        self.textEdit_7 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(470, 260, 291, 21))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 250, 52, 14))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.SettingsButton = QtGui.QToolButton(self.centralwidget)
        self.SettingsButton.setGeometry(QtCore.QRect(20, 380, 431, 61))
        self.SettingsButton.setObjectName(_fromUtf8("SettingsButton"))
        self.Find.raise_()
        self.NameText.raise_()
        self.Name2Text.raise_()
        self.Default.raise_()
        self.textEdit_4.raise_()
        self.textEdit_5.raise_()
        self.textEdit_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.ResultTable.raise_()
        self.textEdit_7.raise_()
        self.label_8.raise_()
        self.FamilyText.raise_()
        self.SettingsButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSettings_2 = QtGui.QAction(MainWindow)
        self.actionSettings_2.setObjectName(_fromUtf8("actionSettings_2"))
        self.actionClose_2 = QtGui.QAction(MainWindow)
        self.actionClose_2.setObjectName(_fromUtf8("actionClose_2"))
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Find.setText(_translate("MainWindow", "Find", None))
        self.NameText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.FamilyText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Name2Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Default.setText(_translate("MainWindow", "Default Table", None))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Result Table", None))
        self.label_2.setText(_translate("MainWindow", "Family", None))
        self.label_3.setText(_translate("MainWindow", "Name", None))
        self.label_4.setText(_translate("MainWindow", "Name2", None))
        self.label_5.setText(_translate("MainWindow", "Passport", None))
        self.label_6.setText(_translate("MainWindow", "Police", None))
        self.label_7.setText(_translate("MainWindow", "Gender", None))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "Birthday", None))
        self.SettingsButton.setText(_translate("MainWindow", "Settings", None))
        self.menuAbout.setTitle(_translate("MainWindow", "about", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))
        self.actionSettings.setText(_translate("MainWindow", "settings", None))
        self.actionSettings_2.setText(_translate("MainWindow", "settings", None))
        self.actionClose_2.setText(_translate("MainWindow", "close", None))

