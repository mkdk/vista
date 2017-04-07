# encoding:utf-8
import sys

from PyQt4.QtGui import *
from PyQt4.QtSql import *

from v1 import Ui_MainWindow


class StartApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(StartApp, self).__init__(parent)
        self.setupUi(self)
        self.db = self.db_connect()

        self.Default.clicked.connect(self.default_values)

    def db_connect(self):
        """settings db from file"""
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("localhost")
        db.setDatabaseName("pyqt")
        db.setUserName("root")
        db.setPassword("root")
        ok = db.open()

        if ok:
            print u'db succes connect'
            return db
        else:
            print u'error while connecting to db'

    def default_values(self):
        """query to db without filter"""
        table = self.ResultTable
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(['Name', 'Birthday', 'Gender', 'SNILS', 'Passport', "Policy"])
        query = QSqlQuery(self.db)
        query.exec_("""SELECT firstName, patrName, lastName, birthDate, sex, SNILS, ClientDocument.serial, ClientDocument.number, ClientPolicy.serial, ClientPolicy.number from Client JOIN ClientDocument ON Client.id=ClientDocument.client_id JOIN ClientPolicy ON Client.id=ClientPolicy.client_id""")
        a = query.size()
        table.setRowCount(a)
        for i in range(a):
            query.next()
            name = query.value(0).toPyObject() + ' ' + query.value(1).toPyObject() + ' ' + query.value(2).toPyObject()
            birthday = query.value(3).toPyObject().toPyDate()
            gender = query.value(4).toPyObject()
            if gender==1:
                gender = 'M'
            else:
                gender = 'W'
            snils = query.value(5).toPyObject()
            passport = query.value(6).toPyObject() + ':' + query.value(7).toPyObject()
            policy = query.value(8).toPyObject() + ':' + query.value(9).toPyObject()
            # print unicode(name), unicode(birthday), unicode(gender), unicode(snils), unicode(passport), unicode(policy)
            table.setItem(i,0, QTableWidgetItem(unicode(name)))
            table.setItem(i,1, QTableWidgetItem(unicode(birthday)))
            table.setItem(i,2, QTableWidgetItem(unicode(gender)))
            table.setItem(i,3, QTableWidgetItem(unicode(snils)))
            table.setItem(i,4, QTableWidgetItem(unicode(passport)))
            table.setItem(i,5, QTableWidgetItem(unicode(policy)))


def main():
    app = QApplication(sys.argv)
    form = StartApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()