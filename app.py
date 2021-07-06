from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import qtmodern.styles
import qtmodern.windows
from src.MyWindow import MyWindow


def window():
    print('Program is Start...')
    app = QApplication(sys.argv)
    window = MyWindow()

    app.setStyle("Fusion")
    # qtmodern.styles.dark(app)
    # editedWindow = qtmodern.windows.ModernWindow(window)

    window.show()
    sys.exit(app.exec_())

window()
