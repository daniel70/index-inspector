# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConnectToServerUJzOhD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ConnectToServer(object):
    def setupUi(self, ConnectToServer):
        if not ConnectToServer.objectName():
            ConnectToServer.setObjectName(u"ConnectToServer")
        ConnectToServer.resize(405, 265)
        ConnectToServer.setModal(True)
        self.verticalLayout = QVBoxLayout(ConnectToServer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(18, -1, 18, -1)
        self.lblHeader = QLabel(ConnectToServer)
        self.lblHeader.setObjectName(u"lblHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHeader.sizePolicy().hasHeightForWidth())
        self.lblHeader.setSizePolicy(sizePolicy)
        self.lblHeader.setMinimumSize(QSize(0, 0))
        self.lblHeader.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.lblHeader.setFont(font)
        self.lblHeader.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblHeader)

        self.frmServer = QFormLayout()
        self.frmServer.setObjectName(u"frmServer")
        self.frmServer.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frmServer.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.frmServer.setHorizontalSpacing(30)
        self.frmServer.setContentsMargins(-1, 10, -1, -1)
        self.lblServerName = QLabel(ConnectToServer)
        self.lblServerName.setObjectName(u"lblServerName")

        self.frmServer.setWidget(0, QFormLayout.LabelRole, self.lblServerName)

        self.lblAuthentication = QLabel(ConnectToServer)
        self.lblAuthentication.setObjectName(u"lblAuthentication")

        self.frmServer.setWidget(3, QFormLayout.LabelRole, self.lblAuthentication)

        self.cmbAuthentication = QComboBox(ConnectToServer)
        self.cmbAuthentication.addItem("")
        self.cmbAuthentication.addItem("")
        self.cmbAuthentication.addItem("")
        self.cmbAuthentication.addItem("")
        self.cmbAuthentication.addItem("")
        self.cmbAuthentication.setObjectName(u"cmbAuthentication")
        self.cmbAuthentication.setEditable(False)

        self.frmServer.setWidget(3, QFormLayout.FieldRole, self.cmbAuthentication)

        self.cmbServerName = QComboBox(ConnectToServer)
        self.cmbServerName.setObjectName(u"cmbServerName")
        self.cmbServerName.setEditable(True)

        self.frmServer.setWidget(0, QFormLayout.FieldRole, self.cmbServerName)

        self.lblPort = QLabel(ConnectToServer)
        self.lblPort.setObjectName(u"lblPort")

        self.frmServer.setWidget(2, QFormLayout.LabelRole, self.lblPort)

        self.txtPort = QLineEdit(ConnectToServer)
        self.txtPort.setObjectName(u"txtPort")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txtPort.sizePolicy().hasHeightForWidth())
        self.txtPort.setSizePolicy(sizePolicy1)
        self.txtPort.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.frmServer.setWidget(2, QFormLayout.FieldRole, self.txtPort)

        self.lblDatabase = QLabel(ConnectToServer)
        self.lblDatabase.setObjectName(u"lblDatabase")

        self.frmServer.setWidget(1, QFormLayout.LabelRole, self.lblDatabase)

        self.txtDatabase = QLineEdit(ConnectToServer)
        self.txtDatabase.setObjectName(u"txtDatabase")

        self.frmServer.setWidget(1, QFormLayout.FieldRole, self.txtDatabase)


        self.verticalLayout.addLayout(self.frmServer)

        self.frmUser = QFormLayout()
        self.frmUser.setObjectName(u"frmUser")
        self.frmUser.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frmUser.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frmUser.setHorizontalSpacing(50)
        self.frmUser.setContentsMargins(30, -1, -1, -1)
        self.lblUserName = QLabel(ConnectToServer)
        self.lblUserName.setObjectName(u"lblUserName")
        self.lblUserName.setEnabled(False)

        self.frmUser.setWidget(0, QFormLayout.LabelRole, self.lblUserName)

        self.lblPassword = QLabel(ConnectToServer)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setEnabled(False)

        self.frmUser.setWidget(1, QFormLayout.LabelRole, self.lblPassword)

        self.txtPassword = QLineEdit(ConnectToServer)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEnabled(False)
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.frmUser.setWidget(1, QFormLayout.FieldRole, self.txtPassword)

        self.txtUserName = QLineEdit(ConnectToServer)
        self.txtUserName.setObjectName(u"txtUserName")
        self.txtUserName.setEnabled(False)

        self.frmUser.setWidget(0, QFormLayout.FieldRole, self.txtUserName)


        self.verticalLayout.addLayout(self.frmUser)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ConnectToServer)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ConnectToServer)
        self.buttonBox.accepted.connect(ConnectToServer.accept)
        self.buttonBox.rejected.connect(ConnectToServer.reject)

        QMetaObject.connectSlotsByName(ConnectToServer)
    # setupUi

    def retranslateUi(self, ConnectToServer):
        ConnectToServer.setWindowTitle(QCoreApplication.translate("ConnectToServer", u"Connect to Server", None))
        self.lblHeader.setText(QCoreApplication.translate("ConnectToServer", u"Index Inspector", None))
        self.lblServerName.setText(QCoreApplication.translate("ConnectToServer", u"Server name:", None))
        self.lblAuthentication.setText(QCoreApplication.translate("ConnectToServer", u"Authentication:", None))
        self.cmbAuthentication.setItemText(0, QCoreApplication.translate("ConnectToServer", u"Windows Authentication", None))
        self.cmbAuthentication.setItemText(1, QCoreApplication.translate("ConnectToServer", u"SQL Server Authentication", None))
        self.cmbAuthentication.setItemText(2, QCoreApplication.translate("ConnectToServer", u"Azure Active Directory - Universal with MFA", None))
        self.cmbAuthentication.setItemText(3, QCoreApplication.translate("ConnectToServer", u"Azure Active Directory - Password", None))
        self.cmbAuthentication.setItemText(4, QCoreApplication.translate("ConnectToServer", u"Azure Active Directory - Integrated", None))

        self.lblPort.setText(QCoreApplication.translate("ConnectToServer", u"Port:", None))
        self.txtPort.setText(QCoreApplication.translate("ConnectToServer", u"1433", None))
        self.lblDatabase.setText(QCoreApplication.translate("ConnectToServer", u"Database:", None))
        self.lblUserName.setText(QCoreApplication.translate("ConnectToServer", u"User name:", None))
        self.lblPassword.setText(QCoreApplication.translate("ConnectToServer", u"Password:", None))
    # retranslateUi

