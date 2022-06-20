from pyautogui import press
from PyQt5 import QtCore, QtGui, QtWidgets
from HandleData import HandelData,PassData

class Ui_PreviewWindow(object):
    def setupUi(self, PreviewWindow):
        PreviewWindow.setObjectName("PreviewWindow")
        PreviewWindow.setFixedSize(1150, 897)
        self.centralwidget = QtWidgets.QWidget(PreviewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1150, 897))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.title.setEnabled(True)
        self.title.setMinimumSize(QtCore.QSize(0, 0))
        self.title.setSizeIncrement(QtCore.QSize(0, 0))
        self.title.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet("border-bottom: 1px solid black;\n"
"border-top: 10px solid white;")
        self.title.setMaxLength(80)
        self.title.setFrame(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setReadOnly(False)
        self.title.setObjectName("title")
        self.title.setReadOnly(True)
        self.verticalLayout.addWidget(self.title)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("border-left:8px solid white;\n"
"border-top:12px solid white;\n"
"\n"
"")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.plainTextEdit.textChanged.connect(self.handelDecrChange)
        PreviewWindow.setCentralWidget(self.centralwidget)

        # Tool ber section

        self.toolBar = QtWidgets.QToolBar(PreviewWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.BottomToolBarArea)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setStyleSheet("background-color:white;")
        PreviewWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.actionEditFile = QtWidgets.QAction(PreviewWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditFile.setIcon(icon)
        self.actionEditFile.setObjectName("actionEditFile")
        self.toolBar.addAction(self.actionEditFile)

        # Tool ber event handel
        self.actionEditFile.triggered.connect(self.ediFile)
        self.previousText = self.plainTextEdit.toPlainText()

        self.data = PassData().getData()
        self.settingUpTheme()
        self.retranslateUi(PreviewWindow)
        QtCore.QMetaObject.connectSlotsByName(PreviewWindow)

    def settingUpTheme(self):
        if self.data["mood"] == "dark":
            self.title.setStyleSheet("background-color:black;color:white;")
            self.plainTextEdit.setStyleSheet("background-color:black;color:white;")
            self.toolBar.setStyleSheet("background-color:black;color:white;")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(".\\icons/icons/pencil_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionEditFile.setIcon(icon)
        else:
            self.title.setStyleSheet("background-color:white;color:black;")
            self.plainTextEdit.setStyleSheet("background-color:white;color:black;")
            self.toolBar.setStyleSheet("background-color:white;color:black;")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(".\\icons/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionEditFile.setIcon(icon)


    # fumctions for tool bar
    # Handel description box text changed event
    def handelDecrChange(self):
        # press("end")
        if len(self.plainTextEdit.toPlainText()) < len(self.previousText):
            self.plainTextEdit.setPlainText(self.previousText)
            # self.decrBox.moveCursor(QtWidgets.qC)
            press("end")
        # pass
        self.previousText = self.plainTextEdit.toPlainText()


    def ediFile(self):

        if self.plainTextEdit.isReadOnly():
            self.plainTextEdit.setReadOnly(False)

            icon = QtGui.QIcon()
            if self.data["mood"] == "dark":
                icon.addPixmap(QtGui.QPixmap(".\\icons/icons/save_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else:
                icon.addPixmap(QtGui.QPixmap(".\\icons/icons/save (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.actionEditFile.setIcon(icon)
            self.actionEditFile.setToolTip("Save Changes")
            
            
        else:
            DataHandler = HandelData()
            DataHandler.updateData([self.title.text(),self.plainTextEdit.toPlainText()])
            DataHandler.storeData()
            icon = QtGui.QIcon()
            if self.data["mood"] == "dark":
                icon.addPixmap(QtGui.QPixmap(".\\icons/icons/pencil_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else:
                icon.addPixmap(QtGui.QPixmap(".\\icons/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.actionEditFile.setIcon(icon)
            self.plainTextEdit.setReadOnly(True)
            self.actionEditFile.setToolTip("Edit Page")





    def retranslateUi(self, PreviewWindow):
        _translate = QtCore.QCoreApplication.translate
        PreviewWindow.setWindowTitle(_translate("PreviewWindow", "One type -Preview"))
        self.actionEditFile.setToolTip(_translate("PreviewWindow", "Edit Page"))

        # self.plainTextEdit.setPlainText("This is a descrpition......")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PreviewWindow = QtWidgets.QMainWindow()
    ui = Ui_PreviewWindow()
    ui.setupUi(PreviewWindow)
    PreviewWindow.show()
    sys.exit(app.exec_())
