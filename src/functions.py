import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
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

    def createProbTable(self, tabs, m, n, p):
        tabs.removeTab(2)
        tabs.removeTab(1)
        tabs.addTab(self.getTables(m, n, p), "جدول احتمالات")
        tabs.setCurrentIndex(1)

    def createRandom(self, tabs, m, n, p):
        if self.df_1.iloc[m-1, 1] != 1 or self.df_2.iloc[n-1, 1] != 1:
            functions.showDialog('Error', 'مجموع احتمالات باید برابر 1 باشد')
        else:
            tabs.removeTab(2)
            self.button.setEnabled(True)
            tabs.addTab(self.getRandomTable(m, n, p), "اعداد رندوم")
            tabs.setCurrentIndex(2)
            print('Random numbers were generated...')

    def createRandomList(list, listLength, pbar, num):
        for i in range(listLength):
            rn = round(random.random(), 3)
            list.append([rn, 0])
            print(f"RandomNumber {i} id created")
            if num == 1:
                pbar.setValue((i/listLength)*50)
            else:
                pbar.setValue(50+(i/listLength)*50)
        if num == 1:
            pbar.setValue(50)
        else:
            pbar.setValue(100)

    def toCsv(data):
        # result = pd.concat([data1, data2, data3, data4], axis=1)
        path = os.path.abspath(os.getcwd()) + "/result.csv"
        data.to_csv(path, index=False, encoding='utf-8-sig')
        print(f'result.csv file created ......... {path}')
        return path

    def is_number(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def setWarrningLabel(self):
        if self.tabs.currentIndex() == 0:
            self.warrningLabel.setText(
                'ابتدا اطلاعات زیر را کامل کرده و سپس بر روی «تایید اطلاعات» کلیک کنید. درصورت تغییر دادن دوباره اطلاعات، دوباره بر روی «تایید اطلاعات» کلیک کنید.')
            self.warrningLabel.setWordWrap(True)
            self.warrningLabel.setStyleSheet("font-weight: bold;")
        elif self.tabs.currentIndex() == 1:
            self.warrningLabel.setText(
                'در این مرحله ستون اول جداول زیر را با اعداد موردنظر کامل کرده و سپس بر روی «تولید اعداد» کلیک کنید.')
            self.warrningLabel.setWordWrap(True)
            self.warrningLabel.setStyleSheet("font-weight: bold;")
        elif self.tabs.currentIndex() == 2:
            self.warrningLabel.setWordWrap(True)
            self.warrningLabel.setStyleSheet("font-weight: bold;")
            self.warrningLabel.setText(
                'در این مرحله جداول اعداد رندوم و زمان بین ورودها و زمان خدمت دهی به دست آمده، برای انجام محاسبات نهایی بر روی «محاسبه» کلیک کنید.')
