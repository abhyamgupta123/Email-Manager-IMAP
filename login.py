# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_email(object):
    def setupUi(self, email):
        email.setObjectName("email")
        email.resize(818, 601)
        email.setWhatsThis("")
        self.centralwidget = QtWidgets.QWidget(email)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(234, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.warning_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.warning_label.sizePolicy().hasHeightForWidth())
        self.warning_label.setSizePolicy(sizePolicy)
        self.warning_label.setMinimumSize(QtCore.QSize(300, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.warning_label.setFont(font)
        self.warning_label.setStyleSheet("color: rgb(170, 0, 0)")
        self.warning_label.setText("")
        self.warning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_label.setObjectName("warning_label")
        self.gridLayout_2.addWidget(self.warning_label, 1, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(233, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 4, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 0, 1, 1)
        self.signin_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signin_frame.sizePolicy().hasHeightForWidth())
        self.signin_frame.setSizePolicy(sizePolicy)
        self.signin_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.signin_frame.setObjectName("signin_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.signin_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_server = QtWidgets.QLabel(self.signin_frame)
        self.label_server.setObjectName("label_server")
        self.horizontalLayout_3.addWidget(self.label_server)
        self.server_name = QtWidgets.QLineEdit(self.signin_frame)
        self.server_name.setObjectName("server_name")
        self.horizontalLayout_3.addWidget(self.server_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.email_label = QtWidgets.QLabel(self.signin_frame)
        self.email_label.setObjectName("email_label")
        self.horizontalLayout.addWidget(self.email_label)
        self.Email_edit = QtWidgets.QLineEdit(self.signin_frame)
        self.Email_edit.setObjectName("Email_edit")
        self.horizontalLayout.addWidget(self.Email_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pass_label = QtWidgets.QLabel(self.signin_frame)
        self.pass_label.setObjectName("pass_label")
        self.horizontalLayout_2.addWidget(self.pass_label)
        self.Pass_edit = QtWidgets.QLineEdit(self.signin_frame)
        self.Pass_edit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Pass_edit.setText("")
        self.Pass_edit.setObjectName("Pass_edit")
        self.horizontalLayout_2.addWidget(self.Pass_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 4)
        spacerItem5 = QtWidgets.QSpacerItem(3, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        self.signin_btn = QtWidgets.QPushButton(self.signin_frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.signin_btn.setFont(font)
        self.signin_btn.setObjectName("signin_btn")
        self.gridLayout.addWidget(self.signin_btn, 3, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 3, 1, 1)
        self.gridLayout_2.addWidget(self.signin_frame, 3, 1, 2, 3)
        spacerItem8 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 180, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 5, 2, 1, 1)
        self.signin_frame.raise_()
        self.warning_label.raise_()
        email.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(email)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        email.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(email)
        self.statusbar.setObjectName("statusbar")
        email.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(email)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLogout = QtWidgets.QAction(email)
        self.actionLogout.setObjectName("actionLogout")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionLogout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(email)
        QtCore.QMetaObject.connectSlotsByName(email)

        # custom
        self.Pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, email):
        _translate = QtCore.QCoreApplication.translate
        email.setWindowTitle(_translate("email", "Welcome - Login"))
        self.label_server.setText(_translate("email", "Server       :"))
        self.email_label.setText(_translate("email", "Email ID    :"))
        self.pass_label.setText(_translate("email", "Password :"))
        self.signin_btn.setText(_translate("email", "Signin"))
        self.signin_btn.setShortcut(_translate("email", "Return"))
        self.menuFile.setTitle(_translate("email", "File"))
        self.actionQuit.setText(_translate("email", "Quit"))
        self.actionQuit.setShortcut(_translate("email", "Ctrl+W"))
        self.actionLogout.setText(_translate("email", "Logout"))
        self.actionLogout.setShortcut(_translate("email", "Ctrl+Shift+L"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     email = QtWidgets.QMainWindow()
#     ui = Ui_email()
#     ui.setupUi(email)
#     email.show()
#     sys.exit(app.exec_())
