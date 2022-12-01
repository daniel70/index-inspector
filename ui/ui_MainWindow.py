# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowrsyyLZ.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QToolBar, QVBoxLayout,
    QWidget)
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
        self.actionFilter = QAction(MainWindow)
        self.actionFilter.setObjectName(u"actionFilter")
        self.actionFilter.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/toolbar/art/feather/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFilter.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filterLayout = QVBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.filterWidget = QWidget(self.centralwidget)
        self.filterWidget.setObjectName(u"filterWidget")
        self.verticalLayout_2 = QVBoxLayout(self.filterWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.filterWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lblName = QLabel(self.groupBox)
        self.lblName.setObjectName(u"lblName")

        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setInputMask(u"d000000000")
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)

        self.txtName = QLineEdit(self.groupBox)
        self.txtName.setObjectName(u"txtName")
        self.txtName.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txtName, 0, 1, 1, 4)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chkMale = QCheckBox(self.groupBox_2)
        self.chkMale.setObjectName(u"chkMale")
        self.chkMale.setChecked(True)

        self.horizontalLayout.addWidget(self.chkMale)

        self.chkFemale = QCheckBox(self.groupBox_2)
        self.chkFemale.setObjectName(u"chkFemale")
        self.chkFemale.setChecked(True)

        self.horizontalLayout.addWidget(self.chkFemale)


        self.gridLayout.addWidget(self.groupBox_2, 2, 3, 1, 2)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.filterLayout.addWidget(self.filterWidget)


        self.verticalLayout.addLayout(self.filterLayout)

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
#if QT_CONFIG(shortcut)
        self.lblName.setBuddy(self.txtName)
#endif // QT_CONFIG(shortcut)

        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionFilter)

        self.retranslateUi(MainWindow)
        self.actionFilter.toggled.connect(self.filterWidget.setVisible)

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
        self.actionFilter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
#if QT_CONFIG(tooltip)
        self.actionFilter.setToolTip(QCoreApplication.translate("MainWindow", u"Filter the data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionFilter.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Filters:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"more", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"less", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"than", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.lblName.setText(QCoreApplication.translate("MainWindow", u"&Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Age is ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"years.", None))
        self.txtName.setProperty("filterAttribute", QCoreApplication.translate("MainWindow", u"name", None))
        self.groupBox_2.setTitle("")
        self.chkMale.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.chkMale.setProperty("filterValue", QCoreApplication.translate("MainWindow", u"M", None))
        self.chkMale.setProperty("filterAttribute", QCoreApplication.translate("MainWindow", u"sex", None))
        self.chkFemale.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.chkFemale.setProperty("filterValue", QCoreApplication.translate("MainWindow", u"F", None))
        self.chkFemale.setProperty("filterAttribute", QCoreApplication.translate("MainWindow", u"sex", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

