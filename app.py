import os
import sys
from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QMainWindow, QLayout
from ui.ui_ConnectToServer import Ui_ConnectToServer
from ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def connect_clicked(self):
        self.dlg_connect.show()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dlg_connect = ConnectToServer(self)
        self.ui.actionConnect.triggered.connect(self.connect_clicked)


class ConnectToServer(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_ConnectToServer()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Connect")
        self.ui.cmbAuthentication.currentTextChanged.connect(self.authentication_changed)
        # self.ui.cmbAuthentication.setCurrentText("Windows Authentication")
        self.ui.txtUserName.setText(self.get_username())

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    SystemExit(app.exec())
