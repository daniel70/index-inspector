# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowfyjFym.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QHeaderView, QMainWindow, QSizePolicy, QStatusBar,
    QTableView, QToolBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 600)
        icon = QIcon()
        icon.addFile(u":/program/art/toolbar/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        icon1 = QIcon()
        icon1.addFile(u":/toolbar/art/feather/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConnect.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon2 = QIcon()
        icon2.addFile(u":/toolbar/art/feather/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chkMale = QCheckBox(self.groupBox)
        self.chkMale.setObjectName(u"chkMale")
        self.chkMale.setChecked(True)

        self.horizontalLayout.addWidget(self.chkMale)

        self.chkFemale = QCheckBox(self.groupBox)
        self.chkFemale.setObjectName(u"chkFemale")
        self.chkFemale.setChecked(True)

        self.horizontalLayout.addWidget(self.chkFemale)


        self.verticalLayout.addWidget(self.groupBox)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Index Inspector", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.actionConnect.setToolTip(QCoreApplication.translate("MainWindow", u"Connect to a database", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.actionRefresh.setToolTip(QCoreApplication.translate("MainWindow", u"Reload data", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.chkMale.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.chkFemale.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

