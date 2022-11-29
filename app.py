import operator
import os
import sys
from dataclasses import dataclass, fields
from time import sleep
from typing import Union, Any

import PySide6
import pyodbc

from PySide6 import QtCore
from PySide6.QtCore import QAbstractTableModel, SIGNAL, QSortFilterProxyModel
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QMainWindow, QLayout, QMessageBox
from ui.ui_ConnectToServer import Ui_ConnectToServer
from ui.ui_MainWindow import Ui_MainWindow
# to reload the resource file run: pyside6-rcc.exe .\resources.qrc -o resources_rc.py


#test class
@dataclass()
class Child:
    def __getitem__(self, item):
        """
        QT model/views need data objects that are subscriptable, like string, list, dict
        The properties of dataclasses are not, however, we can make them behave like one.
        The easiest way is by hardcoding the values, it can also be done programmatically, like so:

        myfields = {i: fld.name for i, fld in enumerate(fields(self.__class__))}
        return self.__getattribute__(myfields[item])

        However:
        Explicit is better than implicit.
        Simple is better than complex.
        so I put it here, as the first function, so it won't be overlooked when new fields are added to this class.
        """
        match item:
            case 0:
                return self.name
            case 1:
                return self.age
            case 2:
                return self.sex
            case _:
                raise IndexError()

    name: str
    age: int
    sex: str


class FilteredDuplicateIndexes(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)


class DuplicateIndexes(QAbstractTableModel):
    def __init__(self, parent):
        super().__init__(parent)
        self.header = ["name", "age", "sex"]
        self.rows = [
            Child("Sofie", 20, "F"),
            Child("Rindert", 18, "M"),
            Child("Geerten", 16, "M"),
        ]

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.rows)

    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.header)

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.rows[index.row()][index.column()]

    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[section]
        return None

    def sort(self, column: int, order: PySide6.QtCore.Qt.SortOrder = ...) -> None:
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        reverse = order == Qt.DescendingOrder
        self.rows = sorted(self.rows, key=operator.itemgetter(column), reverse=reverse)
        self.emit(SIGNAL("layoutChanged()"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionConnect.triggered.connect(self.connect_clicked)
        duplicate_indexes = DuplicateIndexes(self)
        self.ui.tableView.setModel(duplicate_indexes)
        self.ui.tableView.setSortingEnabled(True)

    @QtCore.Slot()
    def connect_clicked(self):
        dlg_connect = ConnectToServer(self)
        result = dlg_connect.exec()
        if result == QDialog.Accepted:
            print("he was accepted")
            conn: pyodbc.Connection = dlg_connect.conn
            conn.execute("SELECT @@VERSION")

        else:
            print("he was rejected")


class ConnectToServer(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_ConnectToServer()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Connect")
        self.ui.cmbAuthentication.currentTextChanged.connect(self.authentication_changed)
        # self.ui.cmbAuthentication.setCurrentText("Windows Authentication")
        self.ui.txtUserName.setText(self.get_username())

        self.conn = None  # holds the connection object

    @staticmethod
    def get_username() -> str:
        domain = os.environ.get("USERDOMAIN", "")
        username = os.environ.get("USERNAME", "")
        return domain + "\\" + username if domain else username

    def authentication_changed(self, txt):
        self.ui.txtPassword.setText("")
        if txt in ["SQL Server Authentication", "Azure Active Directory - Password"]:
            self.ui.lblUserName.setEnabled(True)
            self.ui.lblPassword.setEnabled(True)
            self.ui.txtUserName.setEnabled(True)
            self.ui.txtPassword.setEnabled(True)
            self.ui.txtUserName.setText("")
        else:
            self.ui.lblUserName.setEnabled(False)
            self.ui.lblPassword.setEnabled(False)
            self.ui.txtUserName.setEnabled(False)
            self.ui.txtPassword.setEnabled(False)
            self.ui.txtUserName.setText(self.get_username())

    def accept(self) -> None:
        print("it feels nice to be accepted")
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setDefault(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        # start the animation
        params = {"APP": "Index-Inspector"}

        working_drivers = [
            "ODBC Driver 19 for SQL Server",
            "ODBC Driver 17 for SQL Server",
            "ODBC Driver 13 for SQL Server",
            "SQL Server Native Client 11.0",
        ]
        driver = None
        for current in working_drivers:
            if current in pyodbc.drivers():
                driver = current
                break
        if driver is None:
            QMessageBox.critical(self, "Connection Error", "Could not find a valid ODBC driver.")
            return super().reject()

        params["Driver"] = f"{{{driver}}}"
        params['Server'] = self.ui.cmbServerName.currentText().strip() + "," + self.ui.txtPort.text().strip()
        params['Database'] = self.ui.txtDatabase.text().strip()
        if self.ui.cmbAuthentication.currentText() == "Windows Authentication":
            params["Trusted_Connection"] = "yes"
        elif self.ui.cmbAuthentication.currentText() == "SQL Server Authentication":
            params["UID"] = self.ui.txtUserName.text().strip()
            params["PWD"] = self.ui.txtPassword.text().strip()

        connection_string = ";".join(f"{key}={value}" for key, value in params.items())
        print(connection_string)
        try:
            self.conn = pyodbc.connect(connection_string)
        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Connection Error", ex.args[1])
            return
        finally:
            # stop the animation
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

        super().accept()

    def reject(self) -> None:
        print("it does not feel nice to be rejected")
        super().reject()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    SystemExit(app.exec())
