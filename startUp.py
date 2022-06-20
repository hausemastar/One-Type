from tkinter.tix import Tree
from PyQt5 import QtCore, QtGui, QtWidgets
from HandleData import PassData
from Preview import Ui_PreviewWindow
from Editor import Ui_EditorWindow
from ChangePasswordWindow import Ui_ChangePassword
import sys

class Ui_StartUPwindow(object):
    def setupUi(self, StartUPwindow):
        StartUPwindow.setObjectName("StartUPwindow")
        StartUPwindow.setFixedSize(782, 720)
        self.centralwidget = QtWidgets.QWidget(StartUPwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.itemConteiner = QtWidgets.QListWidget(self.centralwidget)
        self.itemConteiner.setGeometry(QtCore.QRect(0, 100, 731, 601))
        self.itemConteiner.setStyleSheet("padding-left:5px; background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.itemConteiner.setFont(font)
        self.itemConteiner.setObjectName("itemConteiner")
        # password entry
        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(0, 60, 731, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(1, 1, 731, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("background-color: rgb(255, 255, 255);"
"border-bottom: 1px solid black;")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setWordWrap(True)
        self.statusLabel.setObjectName("statusLabel")
        StartUPwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StartUPwindow)
        self.statusbar.setObjectName("statusbar")
        StartUPwindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(StartUPwindow)
        self.toolBar.setStyleSheet("margin-top:5px;")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setObjectName("toolBar")
        StartUPwindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        
        self.actionopenEditor = QtWidgets.QAction(StartUPwindow)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(".\\icons/icons/editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopenEditor.setIcon(self.icon)
        self.actionopenEditor.setObjectName("actionopenEditor")

        self.actionExit = QtWidgets.QAction(StartUPwindow)
        self.icon1 = QtGui.QIcon()
        self.actionExit.setObjectName("actionExit")
        
        self.actionRefresh = QtWidgets.QAction(StartUPwindow)
        self.icon3 = QtGui.QIcon()
        self.actionRefresh.setObjectName("actionRefresh")

        self.actionDrak_mood = QtWidgets.QAction(StartUPwindow)
        self.icon4 = QtGui.QIcon()
        self.actionDrak_mood.setObjectName("actionDrak_mood")

        self.actionchangPassword = QtWidgets.QAction(StartUPwindow)
        self.icon5 = QtGui.QIcon()
        self.actionchangPassword.setObjectName("actionchangPassword")

        
        self.toolBar.addAction(self.actionopenEditor)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDrak_mood)
        self.toolBar.addAction(self.actionchangPassword)
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionExit)

        # opening seleted items
        self.itemConteiner.itemDoubleClicked.connect(self.openItem) # mouse Double click
        self.itemConteiner.itemActivated.connect(self.openItem) # enter key pressed
        self.password_lineEdit.returnPressed.connect(self.varifyPassword)
        

        # add manually
        self.dataClass = PassData()
        self.data = self.dataClass.getData()
        self.isPassed = False
        # self.displayItems()
        self.settingUpTheme()
        # self.centralwidget.focusInEvent(self.refresh_item())

        # tool bar key binding
        self.actionopenEditor.triggered.connect(self.openEditor)
        self.actionExit.triggered.connect(self.exit_app)
        self.actionRefresh.triggered.connect(self.refresh_item)
        self.actionDrak_mood.triggered.connect(self.toggleMood)
        self.actionchangPassword.triggered.connect(self.OpenChangePasswordWindow)

        self.retranslateUi(StartUPwindow)
        QtCore.QMetaObject.connectSlotsByName(StartUPwindow)


    def varifyPassword(self):
        entered_password = self.password_lineEdit.text()
        if self.data["password"] == entered_password:
            self.password_lineEdit.setText("")
            self.statusbar.showMessage("Showing Items")
            self.isPassed = True

            self.displayItems()
        else:
            self.statusbar.showMessage("Wrong Password")

    def displayItems(self):
        self.data = self.dataClass.refreshData()
        # print(self.data)
        for i in self.data["file_data"]:
            # print(self.data["file_data"][i]["title"])
            self.itemConteiner.addItem(self.data["file_data"][i]["title"])

    def openItem(self):
        clickedItemTitle = self.itemConteiner.item(self.itemConteiner.currentRow()).text()
        dataList = self.dataClass.FindDataFormTitle(clickedItemTitle)
        # print(dataList)
        self.statusbar.showMessage(f"Opening '{dataList[0]}'")
        self.openPreview(dataList[0],dataList[1])
    
    def settingUpTheme(self):
        mood = self.data["mood"]
        if mood == "dark":
            # updateing the status bar
            self.statusbar.showMessage("Switch to DarkMood")
            # changing the icon to dark
            self.icon.addPixmap(QtGui.QPixmap(".\\icons/icons/editor_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionopenEditor.setIcon(self.icon)
            
            self.icon1.addPixmap(QtGui.QPixmap(".\\icons/icons/exit_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionExit.setIcon(self.icon1)

            self.icon3.addPixmap(QtGui.QPixmap(".\\icons/icons/refresh_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionRefresh.setIcon(self.icon3)

            self.icon4.addPixmap(QtGui.QPixmap(".\\icons/icons/monitor_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionDrak_mood.setIcon(self.icon4)

            self.icon5.addPixmap(QtGui.QPixmap(".\\icons/icons/key_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionchangPassword.setIcon(self.icon5)

            # changing the color to dark
            self.itemConteiner.setStyleSheet("background-color:black;color:white")
            self.statusLabel.setStyleSheet("background-color:black;color:white;border-bottom: 1px solid white;border-right: 1px solid white")
            self.toolBar.setStyleSheet("background-color:black;")
            self.password_lineEdit.setStyleSheet("padding-left:12px;background-color:black;color:white")
            self.statusbar.setStyleSheet("background-color:black;color:white;border-top:1px solid white;")
            

        else:
            self.statusbar.showMessage("Switch to LightMood")
            # changing the icon to dark
            self.icon.addPixmap(QtGui.QPixmap(".\\icons/icons/editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionopenEditor.setIcon(self.icon)
            
            self.icon1.addPixmap(QtGui.QPixmap(".\\icons/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionExit.setIcon(self.icon1)

            self.icon3.addPixmap(QtGui.QPixmap(".\\icons/icons/refresh (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionRefresh.setIcon(self.icon3)

            self.icon4.addPixmap(QtGui.QPixmap(".\\icons/icons/monitor-levels.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionDrak_mood.setIcon(self.icon4)

            self.icon5.addPixmap(QtGui.QPixmap(".\\icons/icons/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionchangPassword.setIcon(self.icon5)

            # changing the color to dark
            self.itemConteiner.setStyleSheet("background-color:white;color:black")
            self.statusLabel.setStyleSheet("background-color:white; color:black;border-bottom:none;border-right:none")
            self.toolBar.setStyleSheet("background-color:white;")
            self.password_lineEdit.setStyleSheet("padding-left:12px;background-color:white;color:black")
            self.statusbar.setStyleSheet("background-color:white;color:black;border-top:none;")


    def retranslateUi(self, StartUPwindow):
        _translate = QtCore.QCoreApplication.translate
        StartUPwindow.setWindowTitle(_translate("StartUPwindow", "One type"))
        __sortingEnabled = self.itemConteiner.isSortingEnabled()
        self.itemConteiner.setSortingEnabled(False)
        self.itemConteiner.setSortingEnabled(__sortingEnabled)
        self.statusLabel.setText(_translate("StartUPwindow", "One type application"))
        self.password_lineEdit.setPlaceholderText(_translate("StartUPwindow", "PASSWORD"))
        self.toolBar.setWindowTitle(_translate("StartUPwindow", "toolBar"))
        self.actionopenEditor.setText(_translate("StartUPwindow", "openEditor"))
        self.actionopenEditor.setToolTip(_translate("StartUPwindow", "Open Editor"))
        self.actionopenEditor.setShortcut(_translate("StartUPwindow", "Ctrl+E"))
        self.actionExit.setText(_translate("StartUPwindow", "Exit"))
        self.actionExit.setToolTip(_translate("StartUPwindow", "Exit the app"))
        self.actionRefresh.setToolTip(_translate("StartUPwindow", "Refresh items"))
        self.actionRefresh.setShortcut(_translate("StartUPwindow", "Ctrl+R"))
        self.actionchangPassword.setToolTip(_translate("StartUPwindow", "Reset Password"))

    def openPreview(self,title,decr):
        self.Preview_window = QtWidgets.QMainWindow()
        self.Preview_window_ui = Ui_PreviewWindow()
        self.Preview_window_ui.setupUi(self.Preview_window)
        self.Preview_window_ui.title.setText(title)
        self.Preview_window_ui.plainTextEdit.setPlainText(decr)
        self.Preview_window.show()

    # Tool bar fuctions
    def openEditor(self):
        self.Editor_window = QtWidgets.QMainWindow()
        self.Editor_window_ui = Ui_EditorWindow()
        self.Editor_window_ui.setupUi(self.Editor_window)
        self.Editor_window.show()

    def OpenChangePasswordWindow(self):
        self.ChangePassword_window = QtWidgets.QMainWindow()
        self.ChangePassword_window_ui = Ui_ChangePassword()
        self.ChangePassword_window_ui.setupUi(self.ChangePassword_window)
        self.ChangePassword_window.show()
    
    def exit_app(self):
        sys.exit()

    def refresh_item(self):
        if self.isPassed:
            self.statusbar.showMessage("Refreshing item list")
            print("refreshing window")
            self.itemConteiner.clear()
            self.displayItems()


    def toggleMood(self):
        if self.data["mood"] == "dark":
            self.data["mood"] = "light"
            self.settingUpTheme()
            self.dataClass.updateMoodData(self.data)
            

        else:
            self.data["mood"] = "dark"
            self.settingUpTheme()
            self.dataClass.updateMoodData(self.data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartUPwindow = QtWidgets.QMainWindow()
    ui = Ui_StartUPwindow()
    ui.setupUi(StartUPwindow)
    StartUPwindow.show()
    sys.exit(app.exec_())
