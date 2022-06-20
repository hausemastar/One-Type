from PyQt5 import QtCore, QtGui, QtWidgets
from HandleData import HandelData,PassData
from Preview import Ui_PreviewWindow
import sys
from saveFileDialog import Ui_Dialog
from pyautogui import hotkey

class Ui_EditorWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1150, 897)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1151, 865))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleBox = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.TitleBox.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.TitleBox.setFont(font)
        self.TitleBox.setMouseTracking(True)
        self.TitleBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TitleBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TitleBox.setMaxLength(80)
        self.TitleBox.setFrame(False)
        self.TitleBox.setClearButtonEnabled(True)
        self.TitleBox.setObjectName("TitleBox")
        self.verticalLayout.addWidget(self.TitleBox)
        self.decrBox = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.decrBox.setFont(font)
        self.decrBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.decrBox.setObjectName("decrBox")
        self.verticalLayout.addWidget(self.decrBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.allowedAreas()
        self.toolBar.setEnabled(True)
        self.toolBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(25, 25))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.icon = QtGui.QIcon()
        self.actionSave.setObjectName("actionSave")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.icon1 = QtGui.QIcon()
        self.actioncopy.setObjectName("actioncopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setCheckable(False)
        self.icon2 = QtGui.QIcon()
        self.actionPaste.setObjectName("actionPaste")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.icon3 = QtGui.QIcon()
        self.actionexit.setObjectName("actionexit")
        self.actionDrak_mood = QtWidgets.QAction(MainWindow)
        self.icon4 = QtGui.QIcon()
        self.actionDrak_mood.setObjectName("actionDrak_mood")

        self.actionPreview = QtWidgets.QAction(MainWindow)
        self.icon5 = QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap(".\\icons/icons/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreview.setIcon(self.icon5)
        self.actionPreview.setObjectName("actionPreview")

        self.toolBar.addAction(self.actionexit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDrak_mood)
        self.toolBar.addAction(self.actionPreview)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actioncopy)
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Add manually#################################################################
        self.toolBar.setStyleSheet("background-color : white")
        self.isSaved = False
        self.dataPassing = PassData()
        self.allTitle = self.dataPassing.getAllTitle()


        # handel change events
        self.decrBox.textChanged.connect(self.handelDecrChange)
        self.TitleBox.textChanged.connect(self.getValiedTitle)

        # tool bar events
        # exit Button
        self.actionexit.triggered.connect(self.exit_app)
        self.actionDrak_mood.triggered.connect(self.toggleDarkMood)
        self.actioncopy.triggered.connect(self.copy_text)
        self.actionPaste.triggered.connect(self.paste_text)
        self.actionSave.triggered.connect(self.handelSave)
        self.actionPreview.triggered.connect(self.openPreview)

        # Tool ber label
        self.toolberLable = QtWidgets.QLabel(self.toolBar)
        self.toolberLable.setText("Not save ")
        self.toolberLable.setAlignment(QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toolberLable.setFont(font)
        self.toolberLable.setGeometry(QtCore.QRect(0, 0, 400, 39))
        self.toolberLable.setStyleSheet("border-top:1px solid white;")
        self.previousText = self.decrBox.toPlainText()

        # self.darkMood = True
        self.settingUpTheme()

    def settingUpTheme(self):
        if self.dataPassing.data["mood"] == "dark":
            self.darkMood = True
        
        else:
            self.darkMood = False
        
        self.toggleDarkMood()


    # Hendel titlebox change events
    def getValiedTitle(self):
        if self.dataPassing.checkeValidTitle(self.TitleBox.text()) == True:
            self.updateToolber("Valid title.")
            self.decrBox.setEnabled(True)
        
        else:
            self.updateToolber("Invalid title.Title already exist")
            self.decrBox.setEnabled(False)




    # function for update toolbarlabel
    def updateToolber(self,newMassage):
        self.toolberLable.setText(newMassage)
        
    # Handel decrBox change event 
    def handelDecrChange(self):
        if self.TitleBox.isReadOnly():
            hotkey("ctrl","end")
            if len(self.decrBox.toPlainText()) < len(self.previousText):
                self.decrBox.setPlainText(self.previousText)
                # self.decrBox.moveCursor(QtWidgets.qC)
                hotkey("ctrl","end")
            # pass
        # self.previousText = self.decrBox.toPlainText()
        self.updateToolber("Unsave*")


    # funtions for tools bar buttons
    def showDialogbox(self):
        self.dialog_window = QtWidgets.QDialog()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self.dialog_window)

        self.dialog_ui.buttonBox.accepted.connect(lambda:self.setSaveValue(True))
        self.dialog_ui.buttonBox.rejected.connect(lambda:self.setSaveValue(False))
        self.dialog_window.show()

    def setSaveValue(self,value):
        self.isSaved = value
        if value == True:
            QtCore.QCoreApplication.instance().quit()


    def exit_app(self):
        if self.TitleBox.text() == "":
            QtCore.QCoreApplication.instance().quit()
            return
        if self.isSaved == False:
            self.showDialogbox()

        if self.isSaved == True:
            QtCore.QCoreApplication.instance().quit()
        else:
            pass


        
        pass
        
        # sys.exit()
    
        # dark mood
    def toggleDarkMood(self):
        if self.darkMood:
            self.decrBox.setStyleSheet("background-color: black;" "color: white; padding-left:10px")
            self.TitleBox.setStyleSheet("background-color: black;" "color: white; ")
            self.toolBar.setStyleSheet("background-color: black;")
            self.toolberLable.setStyleSheet("color:white; border-top:1px solid white;")
            # changing the icon to dark
            # save icon
            self.icon.addPixmap(QtGui.QPixmap(".\\icons/icons/save_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionSave.setIcon(self.icon)
            # copy icon
            self.icon1.addPixmap(QtGui.QPixmap(".\\icons/icons/copy_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actioncopy.setIcon(self.icon1)
            # paste icon
            self.icon2.addPixmap(QtGui.QPixmap(".\\icons/icons/paste_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPaste.setIcon(self.icon2)
            # exit icon
            self.icon3.addPixmap(QtGui.QPixmap(".\\icons/icons/exit_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionexit.setIcon(self.icon3)
            # dark moood icon
            self.icon4.addPixmap(QtGui.QPixmap(".\\icons/icons/monitor_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionDrak_mood.setIcon(self.icon4)
            self.actionDrak_mood.setToolTip("Enable Light Mood")

            # preview icon
            self.icon5.addPixmap(QtGui.QPixmap(".\\icons/icons/preview_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPreview.setIcon(self.icon5)

        else:
            self.decrBox.setStyleSheet("color: black;" "background-color: white; padding-left:10px")
            self.TitleBox.setStyleSheet("color: black;" "background-color: white;")
            self.toolBar.setStyleSheet("background: white;")
            self.toolberLable.setStyleSheet("color:black; border-top:1px solid white;")

            # changing the icon to light
            # save icon
            self.icon.addPixmap(QtGui.QPixmap(".\\icons/icons/save (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionSave.setIcon(self.icon)
            # copy icon
            self.icon1.addPixmap(QtGui.QPixmap(".\\icons/icons/copy (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actioncopy.setIcon(self.icon1)
            # paste icon
            self.icon2.addPixmap(QtGui.QPixmap(".\\icons/icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPaste.setIcon(self.icon2)
            # exit icon
            self.icon3.addPixmap(QtGui.QPixmap(".\\icons/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionexit.setIcon(self.icon3)
            # dark moood icon
            self.icon4.addPixmap(QtGui.QPixmap(".\\icons/icons/monitor-levels.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionDrak_mood.setIcon(self.icon4)
            self.actionDrak_mood.setToolTip("Enable Dark Mood")
            # preview icon
            self.icon5.addPixmap(QtGui.QPixmap(".\\icons/icons/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPreview.setIcon(self.icon5)
            
        self.darkMood = not self.darkMood

        # copy button
    def copy_text(self):
        if self.centralwidget.focusWidget().objectName() == self.TitleBox.objectName():
            self.TitleBox.copy()

        elif self.centralwidget.focusWidget().objectName() == self.decrBox.objectName():
            self.decrBox.copy()

        # paste button
    def paste_text(self):
        if self.centralwidget.focusWidget().objectName() == self.TitleBox.objectName():
            self.TitleBox.paste()

        elif self.centralwidget.focusWidget().objectName() == self.decrBox.objectName():
            self.decrBox.paste()
    
    def handelSave(self):
        if self.TitleBox.text() == "":
            self.updateToolber("Enter a Title")

        # print(self.TitleBox.text().isspace())
        if self.TitleBox.text() != "":

            self.TitleBox.setReadOnly(True)
        
            dataHandler = HandelData()
            # print(dataHandler.checkeTitle(self.TitleBox.text()))
            if dataHandler.checkeTitle(self.TitleBox.text()) == False:

                dataHandler.updateData([self.TitleBox.text(),self.decrBox.toPlainText()])
                dataHandler.storeData()
                self.isSaved = True
                self.updateToolber("Saved")
                self.previousText = self.decrBox.toPlainText()

            elif dataHandler.checkeTitle(self.TitleBox.text()) == True:
                dataHandler.saveData([self.TitleBox.text(),self.decrBox.toPlainText()])
                dataHandler.storeData()
                self.isSaved = True
                self.updateToolber("Saved")
                self.previousText = self.decrBox.toPlainText()
                # pass
            


    
    # Setting up PreviewWindow 
    def openPreview(self):
        self.preview_window = QtWidgets.QMainWindow()
        self.preview_ui = Ui_PreviewWindow()
        self.preview_ui.setupUi(self.preview_window)
        self.preview_ui.toolBar.deleteLater()
        self.preview_ui.title.setText(self.TitleBox.text())
        self.preview_ui.plainTextEdit.setPlainText(self.decrBox.toPlainText())
        self.preview_window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "One type -Editor"))
        self.TitleBox.setPlaceholderText(_translate("MainWindow", "Title....."))
        self.decrBox.setPlaceholderText(_translate("MainWindow", "Description....."))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save the file"))
        self.actionSave.setShortcut(_translate("StartUPwindow", "Ctrl+S"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actioncopy.setToolTip(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setToolTip(_translate("MainWindow", "Paste from clipboard"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionexit.setToolTip(_translate("MainWindow", "Exit the app"))
        self.actionDrak_mood.setText(_translate("MainWindow", "Drak mood"))
        self.actionDrak_mood.setToolTip(_translate("MainWindow", "Enable dark mood"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_EditorWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
