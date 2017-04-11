# encoding:utf-8
import json
import os
import sys

from PyQt4.QtCore import pyqtSlot, QString
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from view.v1 import Ui_MainWindow
from view.v1_settings import Ui_Dialog

reload(sys)
sys.setdefaultencoding('utf-8')

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class SettingsWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Settings')

        self.load_data()
        self.SaveButton.clicked.connect(self.save_data)

    def load_data(self):
        with open(os.path.join(ROOT_PATH, 'settings.json'), 'r') as settings:
            data = json.load(settings)
            self.hostNameEdit.setText(data['hostname'])
            self.DatabaseNameEdit.setText(data['database'])
            self.UserNameEdit.setText(data['user'])
            self.PasswordEdit.setText(data['password'])

    def save_data(self):
        hostname = self.hostNameEdit.text()
        database = self.DatabaseNameEdit.text()
        user = self.UserNameEdit.text()
        password = self.PasswordEdit.text()
        if hostname and database and user and password:
            with open(os.path.join(ROOT_PATH, 'settings.json'), 'w') as settings:
                data = {
                    'hostname': str(hostname),
                    'database': str(database),
                    'user': str(user),
                    'password': str(password)
                }
                json.dump(data, settings)


class StartApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(StartApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Test task for \"Vista\"")
        self.db = self.db_connect()
        self.settings_dialog = SettingsWindow()
        self.default_values()

        self.SettingsButton.clicked.connect(self.set_settings)
        self.Find.clicked.connect(self.custom_search)
        self.Default.clicked.connect(self.default_values)

    @pyqtSlot()
    def set_settings(self):
        self.settings_dialog.show()

    def db_connect(self):
        """settings db from file"""
        with open(os.path.join(ROOT_PATH, 'settings.json'), 'r') as settings:
            data = json.load(settings)
            db = QSqlDatabase.addDatabase("QMYSQL")
            db.setHostName(data["hostname"])
            db.setDatabaseName(data["database"])
            db.setUserName(data["user"])
            db.setPassword(data["password"])
            ok = db.open()

            if ok:
                print 'db succes connect'
                return db
            else:
                print 'error while connecting to db'

    def values_into_result_table(self, query, table):
        a = query.size()
        table.setRowCount(a)
        for i in range(a):
            query.next()
            name = (query.value(0).toPyObject() + ' ' + query.value(1).toPyObject() + ' ' + query.value(2).toPyObject())
            birthday = query.value(3).toPyObject().toPyDate()
            gender = query.value(4).toPyObject()
            if gender == 1:
                gender = 'Man'
            else:
                gender = 'Woman'
            snils = query.value(5).toPyObject()
            passport = query.value(6).toPyObject() + ':' + query.value(7).toPyObject()
            policy = query.value(8).toPyObject() + ':' + query.value(9).toPyObject()
            table.setItem(i, 0, QTableWidgetItem(unicode(name)))
            table.setItem(i, 1, QTableWidgetItem(unicode(birthday)))
            table.setItem(i, 2, QTableWidgetItem(unicode(gender)))
            table.setItem(i, 3, QTableWidgetItem(unicode(snils)))
            table.setItem(i, 4, QTableWidgetItem(unicode(passport)))
            table.setItem(i, 5, QTableWidgetItem(unicode(policy)))

    def default_values(self):
        """query to db without filter"""
        table = self.ResultTable
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(['Name', 'Birthday', 'Gender', 'SNILS', 'Passport', "Policy"])
        query = QSqlQuery(self.db)
        query.exec_("""SELECT firstName, patrName, lastName, birthDate, sex, SNILS,
                        ClientDocument.serial, ClientDocument.number, ClientPolicy.serial,
                        ClientPolicy.number from Client JOIN ClientDocument ON
                        Client.id=ClientDocument.client_id JOIN ClientPolicy ON
                        Client.id=ClientPolicy.client_id""")
        # show table
        self.values_into_result_table(query, table)

    def parse_arguments(self):
        """parsing parametrs for filter"""
        data = {}
        arguments = [self.NameText, self.Name2Text, self.FamilyText,
                     self.serialPassEdit, self.numberPassEdit, self.serialPoliceEdit,
                     self.numberPoliceEdit, self.sexEdit, self.birthdayEdit, self.regularEdit]

        for argument in arguments:
            v = str(argument.toPlainText())
            v = v.replace('\n', '')
            k = str(argument.property('field').toPyObject())
            data[k] = v
        return data

    def custom_search(self):
        """query to db with filter"""
        q = """ SELECT firstName, patrName, lastName, birthDate, sex, SNILS, ClientDocument.serial, ClientDocument.number, ClientPolicy.serial, ClientPolicy.number from Client JOIN ClientDocument ON Client.id=ClientDocument.client_id JOIN ClientPolicy ON Client.id=ClientPolicy.client_id WHERE """
        q_regular = """ SELECT firstName, patrName, lastName, birthDate, sex, SNILS, ClientDocument.serial,
        ClientDocument.number, ClientPolicy.serial, ClientPolicy.number from Client JOIN
        ClientDocument ON Client.id=ClientDocument.client_id JOIN ClientPolicy
        ON Client.id=ClientPolicy.client_id WHERE firstName Like \"%{arg}%\" OR patrName Like \"%{arg}%\"
        OR lastName Like \"%{arg}%\" OR sex Like \"%{arg}%\"
        OR ClientDocument.serial Like \"%{arg}%\" OR ClientDocument.number Like \"%{arg}%\" OR
        ClientPolicy.serial Like \"%{arg}%\" OR ClientPolicy.number Like \"%{arg}%\" """.replace('\n', '')
        table = self.ResultTable
        table.setRowCount(0)
        table.setColumnCount(0)
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(['Name', 'Birthday', 'Gender', 'SNILS', 'Passport', 'Policy'])

        data = self.parse_arguments()
        first = True
        for k in data.iterkeys():
            if k == 'regular expression' and len(data[k]) != 0:
                q = q_regular.format(arg=data[k])
                break
            else:
                if len(data[k].strip()) != 0:
                    if first:
                        q += ' %s="%s"' % (k, data[k])
                        first = False
                    else:
                        q += ' and %s="%s"' % (k, data[k])
        query = QSqlQuery(self.db)
        q = QString(unicode(q))
        print '+' * 10, q
        query.exec_(q)
        # show table
        self.values_into_result_table(query, table)


def main():
    app = QApplication(sys.argv)
    form = StartApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
