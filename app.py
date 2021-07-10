from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from src.mainWindow import MainWindow


def window():
    print('Program is Start...')
    app = QApplication(sys.argv)
    
    dir_ = QtCore.QDir("fonts")
    _id = [
            QtGui.QFontDatabase.addApplicationFont('fonts/Vazir.ttf'),
            QtGui.QFontDatabase.addApplicationFont('fonts/Vazir-Bold.ttf'),
        ]
    
    window = MainWindow()
    app.setStyle("Fusion")
    window.show()
    sys.exit(app.exec_())


window()
