# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_mod.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 50, 241, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_host = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_host.setObjectName("label_host")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_host)
        self.lineEdit_host = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_host)
        self.lineEdit_port = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_port)
        self.label_port = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_port.setObjectName("label_port")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_port)
        self.pushButton_OK = QtWidgets.QPushButton(Dialog)
        self.pushButton_OK.setGeometry(QtCore.QRect(74, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_OK.setFont(font)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(220, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label_host.setText(_translate("Dialog", "Device IP"))
        self.lineEdit_host.setText(_translate("Dialog", "192.168.0.113"))
        self.lineEdit_port.setText(_translate("Dialog", "8266"))
        self.label_port.setText(_translate("Dialog", "Device port"))
        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))