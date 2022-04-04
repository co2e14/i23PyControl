# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addgisaxsbs.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 1212)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidgetgisaxsbs = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidgetgisaxsbs.setGeometry(QtCore.QRect(20, 810, 631, 80))
        self.horizontalLayoutWidgetgisaxsbs.setObjectName("horizontalLayoutWidgetgisaxsbs")
        self.gisaxshbox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetgisaxsbs)
        self.gisaxshbox.setContentsMargins(0, 0, 0, 0)
        self.gisaxshbox.setObjectName("gisaxshbox")
        self.gisaxs_bs_x_lab = QtWidgets.QLabel(self.horizontalLayoutWidgetgisaxsbs)
        self.gisaxs_bs_x_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gisaxs_bs_x_lab.setObjectName("gisaxs_bs_x_lab")
        self.gisaxshbox.addWidget(self.gisaxs_bs_x_lab)
        self.set_gisaxs_x = QtWidgets.QLineEdit(self.horizontalLayoutWidgetgisaxsbs)
        self.set_gisaxs_x.setText("")
        self.set_gisaxs_x.setObjectName("set_gisaxs_x")
        self.gisaxshbox.addWidget(self.set_gisaxs_x)
        self.gisaxs_bs_x_rbv = QtWidgets.QLabel(self.horizontalLayoutWidgetgisaxsbs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gisaxs_bs_x_rbv.sizePolicy().hasHeightForWidth())
        self.gisaxs_bs_x_rbv.setSizePolicy(sizePolicy)
        self.gisaxs_bs_x_rbv.setObjectName("gisaxs_bs_x_rbv")
        self.gisaxshbox.addWidget(self.gisaxs_bs_x_rbv)
        self.set_gisaxs_y = QtWidgets.QLineEdit(self.horizontalLayoutWidgetgisaxsbs)
        self.set_gisaxs_x.setText("")
        self.set_gisaxs_y.setObjectName("set_gisaxs_y")
        self.gisaxshbox.addWidget(self.set_gisaxs_y)
        self.gisaxs_bs_y_lab = QtWidgets.QLabel(self.horizontalLayoutWidgetgisaxsbs)
        self.gisaxs_bs_y_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gisaxs_bs_y_lab.setObjectName("gisaxs_bs_y_lab")
        self.gisaxshbox.addWidget(self.gisaxs_bs_y_lab)
        self.gisaxs_bs_y_rbv = QtWidgets.QLabel(self.horizontalLayoutWidgetgisaxsbs)
        self.gisaxs_bs_y_rbv.setObjectName("gisaxs_bs_y_rbv")
        self.gisaxshbox.addWidget(self.gisaxs_bs_y_rbv)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gisaxs_bs_x_lab.setText(_translate("MainWindow", "GISAXS BS X"))
        self.gisaxs_bs_x_rbv.setText(_translate("MainWindow", "x is"))
        self.gisaxs_bs_y_lab.setText(_translate("MainWindow", "GISAXS BS Y"))
        self.gisaxs_bs_y_rbv.setText(_translate("MainWindow", "y is"))
