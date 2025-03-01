# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_HkuUserManagerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserManagerForm(object):
    def setupUi(self, UserManagerForm):
        UserManagerForm.setObjectName("UserManagerForm")
        UserManagerForm.resize(642, 400)
        self.formLayout = QtWidgets.QFormLayout(UserManagerForm)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_user_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.add_user_pushButton.setObjectName("add_user_pushButton")
        self.horizontalLayout.addWidget(self.add_user_pushButton)
        self.remove_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.horizontalLayout.addWidget(self.remove_pushButton)
        self.reset_password_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.reset_password_pushButton.setObjectName("reset_password_pushButton")
        self.horizontalLayout.addWidget(self.reset_password_pushButton)
        self.refresh_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.users_tableView = QtWidgets.QTableView(UserManagerForm)
        self.users_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.users_tableView.setAlternatingRowColors(False)
        self.users_tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.users_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.users_tableView.setSortingEnabled(True)
        self.users_tableView.setObjectName("users_tableView")
        self.users_tableView.horizontalHeader().setDefaultSectionSize(140)
        self.users_tableView.horizontalHeader().setMinimumSectionSize(5)
        self.users_tableView.horizontalHeader().setSortIndicatorShown(True)
        self.users_tableView.horizontalHeader().setStretchLastSection(True)
        self.users_tableView.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.users_tableView)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout)

        self.retranslateUi(UserManagerForm)
        QtCore.QMetaObject.connectSlotsByName(UserManagerForm)

    def retranslateUi(self, UserManagerForm):
        _translate = QtCore.QCoreApplication.translate
        UserManagerForm.setWindowTitle(_translate("UserManagerForm", "Form"))
        self.add_user_pushButton.setText(_translate("UserManagerForm", "Add"))
        self.remove_pushButton.setText(_translate("UserManagerForm", "Remove"))
        self.reset_password_pushButton.setText(_translate("UserManagerForm", "Reset password"))
        self.refresh_pushButton.setText(_translate("UserManagerForm", "Refresh"))
