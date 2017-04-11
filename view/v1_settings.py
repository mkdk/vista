# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(291, 300)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.hostNameEdit = QtGui.QLineEdit(Dialog)
        self.hostNameEdit.setGeometry(QtCore.QRect(50, 30, 191, 20))
        self.hostNameEdit.setObjectName(_fromUtf8("hostNameEdit"))
        self.DatabaseNameEdit = QtGui.QLineEdit(Dialog)
        self.DatabaseNameEdit.setGeometry(QtCore.QRect(50, 80, 191, 20))
        self.DatabaseNameEdit.setObjectName(_fromUtf8("DatabaseNameEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.PasswordEdit = QtGui.QLineEdit(Dialog)
        self.PasswordEdit.setGeometry(QtCore.QRect(50, 180, 191, 20))
        self.PasswordEdit.setObjectName(_fromUtf8("PasswordEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 160, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.UserNameEdit = QtGui.QLineEdit(Dialog)
        self.UserNameEdit.setGeometry(QtCore.QRect(50, 130, 191, 20))
        self.UserNameEdit.setObjectName(_fromUtf8("UserNameEdit"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 110, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.SaveButton = QtGui.QPushButton(Dialog)
        self.SaveButton.setGeometry(QtCore.QRect(70, 220, 141, 61))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Hostname", None))
        self.label_2.setText(_translate("Dialog", "Database", None))
        self.label_3.setText(_translate("Dialog", "Password", None))
        self.label_4.setText(_translate("Dialog", "User", None))
        self.SaveButton.setText(_translate("Dialog", "Save", None))

