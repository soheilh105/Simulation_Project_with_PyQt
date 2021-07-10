from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class ResultWindow(QDialog):
    def __init__(self, sumData, p, q, path, endTime):
        # super(ResultWindow, self).__init__()
        super().__init__()
        self.initUI()
        self.showResults(sumData, p, q, path, endTime)

    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('New Window')
        self.setGeometry(350, 350, 700, 550)
        self.setFixedWidth(550)
        self.setFixedHeight(500)
        self.setWindowTitle("Soheil Hasnai | Results")
        self.setStyleSheet("font-size: 10pt; font-family: 'Vazir';")

    def showResults(self, sumData, p, q, savePath, simuEndTime):
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        layout.message = QtWidgets.QLabel(f'محاسبات با موفقیت انجام شد، فایل محاسبات تمام مراحل شبیه سازی (با فرمت csv) در مسیر زیر ذخیره شده است.')
        layout.message.setWordWrap(True)
        layout.message.setStyleSheet("font-weight: bold;")
        layout.addWidget(layout.message)
        layout.path = QtWidgets.QLabel(savePath)
        layout.path.setWordWrap(True)
        layout.path.setStyleSheet("font-weight: bold;")
        layout.addWidget(layout.path)
        titles = ['متوسط مدت انتظار', 'احتمال انتظار در سیستم برای خدمت دهی', 'احتمال بیکاری خدمت دهنده', 'متوسط مدت خدمت دهی','متوسط مدت زمان بین دو ورود', 'متوسط مدت انتظار برای افراد در صف', 'متوسط مدت ماندن مشتری در سیستم', 'امید ریاضی مدت خدمت دهی']
        results = [0]*8

        results[0]=sumData[4]/p
        results[1]=q/p
        results[2]=sumData[7]/simuEndTime
        results[3]=sumData[2]/p
        results[4]=sumData[0]/(p-1)
        if q==0:
            results[5]='بدون جواب (مخرج صفر)'
        else:
            results[5]=sumData[4]/q
        results[6]=sumData[6]/p
        results[7]=sumData[0]/p


        # Add widgets to the layout
        for i in range(8):
            layout.addWidget(QtWidgets.QLabel(titles[i]+' = '+str(results[i])))

        # Set the layout on the application's window
        self.setLayout(layout)
