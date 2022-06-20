from PyQt5 import QtCore, QtGui, QtWidgets
from HandleData import PassData

class Ui_ChangePassword(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 90, 501, 177))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(26)
        self.formLayout.setObjectName("formLayout")
        self.old_password_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.old_password_label.setFont(font)
        self.old_password_label.setObjectName("old_password_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.old_password_label)
        self.old_passwod_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.old_passwod_entry.setFont(font)
        self.old_passwod_entry.setObjectName("old_passwod_entry")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.old_passwod_entry)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.new_password_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.new_password_label.setFont(font)
        self.new_password_label.setObjectName("new_password_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.new_password_label)
        self.new_passwod_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.new_passwod_entry.setFont(font)
        self.new_passwod_entry.setObjectName("new_passwod_entry")
        self.old_passwod_entry.textChanged.connect(self.checkOldPassword)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.new_passwod_entry)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.new_password_label_repeat = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.new_password_label_repeat.setFont(font)
        self.new_password_label_repeat.setObjectName("new_password_label_repeat")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.new_password_label_repeat)
        self.new_passwod_entry_repeat = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.new_passwod_entry_repeat.setFont(font)
        self.new_passwod_entry_repeat.setObjectName("new_passwod_entry_repeat")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.new_passwod_entry_repeat)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(60, 290, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.submit.setEnabled(False)
        self.submit.clicked.connect(self.resetPassword)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dataClass = PassData()
        self.data = self.dataClass.getData()



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def resetPassword(self):
        if self.new_passwod_entry.text() == self.new_passwod_entry_repeat.text():

            if self.old_passwod_entry.text() == self.data["password"]:
                self.data["password"] = self.new_passwod_entry.text()
                self.dataClass.updatePassWord(self.data)
                self.statusbar.showMessage("Password change succeesful")

        else:
            self.statusbar.showMessage("Two Password don't match!!")


    def checkOldPassword(self):
        if self.old_passwod_entry.text() == self.data["password"]:
            self.statusbar.showMessage("Old Password Match")
            self.submit.setEnabled(True)

        else:
            self.statusbar.showMessage("Old Password not Match")
            self.submit.setEnabled(False)
            

        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Change Password"))
        self.old_password_label.setText(_translate("MainWindow", "Old Password:"))
        self.new_password_label.setText(_translate("MainWindow", "New Passeord:"))
        self.new_password_label_repeat.setText(_translate("MainWindow", "New Password:"))
        self.label_4.setText(_translate("MainWindow", "Change Password"))
        self.submit.setText(_translate("MainWindow", "Reset Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ChangePassword()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
