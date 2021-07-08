from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import qtmodern.styles
import qtmodern.windows
from src.MyWindow import MyWindow
from src.bcolors import bcolors


def window():
    print(f'{bcolors.OKBLUE}Program is Start...{bcolors.RESET}')
    app = QApplication(sys.argv)
    window = MyWindow()

    app.setStyle("Fusion")
    # qtmodern.styles.dark(app)
    # editedWindow = qtmodern.windows.ModernWindow(window)

    window.show()
    sys.exit(app.exec_())

window()
