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
        MainWindow.resize(786, 553)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Find = QtGui.QPushButton(self.centralwidget)
        self.Find.setGeometry(QtCore.QRect(20, 430, 431, 61))
        self.Find.setObjectName(_fromUtf8("Find"))
        self.NameText = QtGui.QTextEdit(self.centralwidget)
        self.NameText.setGeometry(QtCore.QRect(20, 360, 221, 21))
        self.NameText.setObjectName(_fromUtf8("NameText"))
        self.FamilyText = QtGui.QTextEdit(self.centralwidget)
        self.FamilyText.setGeometry(QtCore.QRect(20, 320, 221, 21))
        self.FamilyText.setObjectName(_fromUtf8("FamilyText"))
        self.Name2Text = QtGui.QTextEdit(self.centralwidget)
        self.Name2Text.setGeometry(QtCore.QRect(20, 400, 221, 21))
        self.Name2Text.setObjectName(_fromUtf8("Name2Text"))
        self.numberPassEdit = QtGui.QTextEdit(self.centralwidget)
        self.numberPassEdit.setGeometry(QtCore.QRect(340, 320, 111, 21))
        self.numberPassEdit.setObjectName(_fromUtf8("numberPassEdit"))
        self.numberPoliceEdit = QtGui.QTextEdit(self.centralwidget)
        self.numberPoliceEdit.setGeometry(QtCore.QRect(340, 360, 111, 21))
        self.numberPoliceEdit.setObjectName(_fromUtf8("numberPoliceEdit"))
        self.sexEdit = QtGui.QTextEdit(self.centralwidget)
        self.sexEdit.setGeometry(QtCore.QRect(260, 400, 191, 21))
        self.sexEdit.setObjectName(_fromUtf8("sexEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 310, 52, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 350, 52, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 390, 52, 14))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 310, 52, 14))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 350, 52, 14))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 390, 101, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.ResultTable = QtGui.QTableWidget(self.centralwidget)
        self.ResultTable.setGeometry(QtCore.QRect(20, 40, 741, 261))
        self.ResultTable.setObjectName(_fromUtf8("ResultTable"))
        self.ResultTable.setColumnCount(0)
        self.ResultTable.setRowCount(0)
        self.birthdayEdit = QtGui.QTextEdit(self.centralwidget)
        self.birthdayEdit.setGeometry(QtCore.QRect(470, 320, 291, 21))
        self.birthdayEdit.setObjectName(_fromUtf8("birthdayEdit"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 310, 52, 14))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.SettingsButton = QtGui.QToolButton(self.centralwidget)
        self.SettingsButton.setGeometry(QtCore.QRect(470, 400, 291, 21))
        self.SettingsButton.setObjectName(_fromUtf8("SettingsButton"))
        self.serialPassEdit = QtGui.QTextEdit(self.centralwidget)
        self.serialPassEdit.setGeometry(QtCore.QRect(260, 320, 71, 21))
        self.serialPassEdit.setObjectName(_fromUtf8("serialPassEdit"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 310, 52, 14))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(340, 310, 52, 14))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.serialPoliceEdit = QtGui.QTextEdit(self.centralwidget)
        self.serialPoliceEdit.setGeometry(QtCore.QRect(260, 360, 71, 21))
        self.serialPoliceEdit.setObjectName(_fromUtf8("serialPoliceEdit"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(260, 350, 52, 14))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(340, 350, 52, 14))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.Default = QtGui.QPushButton(self.centralwidget)
        self.Default.setGeometry(QtCore.QRect(470, 430, 291, 61))
        self.Default.setObjectName(_fromUtf8("Default"))
        self.regularEdit = QtGui.QTextEdit(self.centralwidget)
        self.regularEdit.setGeometry(QtCore.QRect(470, 360, 291, 21))
        self.regularEdit.setObjectName(_fromUtf8("regularEdit"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(550, 350, 131, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(580, 510, 181, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.Find.raise_()
        self.NameText.raise_()
        self.Name2Text.raise_()
        self.numberPassEdit.raise_()
        self.numberPoliceEdit.raise_()
        self.sexEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.ResultTable.raise_()
        self.birthdayEdit.raise_()
        self.label_8.raise_()
        self.FamilyText.raise_()
        self.SettingsButton.raise_()
        self.serialPassEdit.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.serialPoliceEdit.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.Default.raise_()
        self.regularEdit.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSettings_2 = QtGui.QAction(MainWindow)
        self.actionSettings_2.setObjectName(_fromUtf8("actionSettings_2"))
        self.actionClose_2 = QtGui.QAction(MainWindow)
        self.actionClose_2.setObjectName(_fromUtf8("actionClose_2"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Find.setText(_translate("MainWindow", "Find", None))
        self.NameText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.NameText.setProperty("field", _translate("MainWindow", "firstName", None))
        self.FamilyText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.FamilyText.setProperty("field", _translate("MainWindow", "lastName", None))
        self.Name2Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Name2Text.setProperty("field", _translate("MainWindow", "patrName", None))
        self.numberPassEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.numberPassEdit.setProperty("field", _translate("MainWindow", "ClientDocument.number", None))
        self.numberPoliceEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.numberPoliceEdit.setProperty("field", _translate("MainWindow", "ClientPolicy.number", None))
        self.sexEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1-Man or 2-Woman</p></body></html>", None))
        self.sexEdit.setProperty("field", _translate("MainWindow", "sex", None))
        self.label.setText(_translate("MainWindow", "Result Table", None))
        self.label_2.setText(_translate("MainWindow", "Family", None))
        self.label_3.setText(_translate("MainWindow", "Name", None))
        self.label_4.setText(_translate("MainWindow", "Name2", None))
        self.label_5.setText(_translate("MainWindow", "Passport", None))
        self.label_6.setText(_translate("MainWindow", "Police", None))
        self.label_7.setText(_translate("MainWindow", "Gender", None))
        self.birthdayEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1990-05-05</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.birthdayEdit.setProperty("field", _translate("MainWindow", "birthDate", None))
        self.label_8.setText(_translate("MainWindow", "Birthday", None))
        self.SettingsButton.setText(_translate("MainWindow", "Settings", None))
        self.serialPassEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.serialPassEdit.setProperty("field", _translate("MainWindow", "ClientDocument.serial", None))
        self.label_9.setText(_translate("MainWindow", "Serial", None))
        self.label_10.setText(_translate("MainWindow", "Number", None))
        self.serialPoliceEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.serialPoliceEdit.setProperty("field", _translate("MainWindow", "ClientPolicy.serial", None))
        self.label_11.setText(_translate("MainWindow", "Serial", None))
        self.label_12.setText(_translate("MainWindow", "Number", None))
        self.Default.setText(_translate("MainWindow", "Default", None))
        self.regularEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.regularEdit.setProperty("field", _translate("MainWindow", "regular expression", None))
        self.label_13.setText(_translate("MainWindow", "Regular expression", None))
        self.label_14.setText(_translate("MainWindow", "Author: eugen_k69@yahoo.com", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))
        self.actionSettings.setText(_translate("MainWindow", "settings", None))
        self.actionSettings_2.setText(_translate("MainWindow", "settings", None))
        self.actionClose_2.setText(_translate("MainWindow", "close", None))

