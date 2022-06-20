from startUp import Ui_StartUPwindow
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    StartUPwindow = QtWidgets.QMainWindow()
    ui = Ui_StartUPwindow()
    ui.setupUi(StartUPwindow)
    StartUPwindow.show()
    sys.exit(app.exec_())
