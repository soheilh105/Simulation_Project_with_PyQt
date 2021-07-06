from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd
from decimal import Decimal
import os
import random


class functions():
    def showDialog(title, text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

    def calculate_1(var_1, var_2, var_3, var_4):
        if(var_1 == 0 or var_2 == 0 or var_3 == 0 or var_4 == 0):
            functions.showDialog(
                "Error", "مقدارهای وارد شده باید مخالف 0 باشند")
        else:
            return 'sucsuss'

    def createTable(self, tabs, m, n, p):
        tabs.removeTab(2)
        tabs.removeTab(1)
        tabs.addTab(self.getTables(m, n, p), "جدول ها")
        tabs.setCurrentIndex(1)

    def createRandom(self, tabs, m, n, p):
        tabs.removeTab(2)
        self.button.setEnabled(True)
        tabs.addTab(self.getRandomTable(m, n, p), "اعداد رندوم")
        tabs.setCurrentIndex(2)

    def toCsv(data1, data2, data3, data4):
        result = pd.concat([data1, data2, data3, data4], axis=1)
        path = os.path.abspath(os.getcwd()) + "/file.csv"
        result.to_csv(path, index=False, encoding='utf-8-sig')

    def is_number(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def createRandomList(list, listLength):
        for i in range(listLength):
            rn = round(random.random(), 3)
            list.append([rn, 0])

    def setWarrningLabel(self):
        if self.tabs.currentIndex() == 0:
            print('0')
            self.warrningLabel.setText(
                'ابتدا اطلاعات زیر را کامل کرده و سپس بر روی «تایید اطلاعات» کلیک کنید. درصورتی که اطلاعات را تغییر دادی دوباره بر روی «تایید اطلاعات» کلیک کنید.')
            self.warrningLabel.setWordWrap(True)
            self.warrningLabel.setStyleSheet("font-weight: bold;")
        elif self.tabs.currentIndex() == 1:
            print('1')
            self.warrningLabel.setText(
                'در این مرحله ستون اول جداول زیر را با اعداد موردنظر کامل کرده و سپس بر روی «تولید اعداد» کلیک کنید.')
            self.warrningLabel.setWordWrap(True)
            self.warrningLabel.setStyleSheet("font-weight: bold;")
        elif self.tabs.currentIndex() == 2:
            print('2')
            self.warrningLabel.setWordWrap(True)
            self.warrningLabel.setStyleSheet("font-weight: bold;")
            self.warrningLabel.setText(
                'در این مرحله جداول اعداد رندوم و اعداد زمان بین ورود ها و زمان خدمت دهی به دست آمده برای انجام محاسبات بر روی «محاسبه» کلیک کنید.')
