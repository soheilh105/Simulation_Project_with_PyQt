from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import numpy as np
import pandas as pd
import random
from threading import Thread

from src.functions import *
from src.TableModel import *
from src.simulation import simulation
from src.ResultWindow import ResultWindow


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 700, 550)
        self.setFixedWidth(750)
        self.setFixedHeight(600)
        self.setWindowTitle("Soheil Hasnai | simulation project")
        self.setStyleSheet("font-size: 11pt; font-family: 'Vazir';")

        # Create a top-level layout
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        self.warrningLabel = QtWidgets.QLabel()
        self.warrningLabel.setWordWrap(True)
        self.warrningLabel.setStyleSheet("font-weight: bold;")

        # Create the tab widget
        self.tabs = QTabWidget()
        self.tabs.currentChanged.connect(
            lambda: functions.setWarrningLabel(self))
        self.tabs.addTab(self.getBaseInfo(), "اطلاعات اصلی")

        # Create progress-bar
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)

        # create calculate button
        self.button = QtWidgets.QPushButton(self)
        self.button.setText('محاسبه')
        self.button.setFont(QtGui.QFont('Vazir', 11,))
        self.button.setEnabled(False)
        self.button.clicked.connect(lambda: self.mainCalculation(
            self.randomData_1, self.randomData_2, self.numOfCustomersTextbox.value(), self.numOfServersTextbox.value(), self.pbar))

        mainLayout.addWidget(self.warrningLabel)
        mainLayout.addWidget(self.tabs)
        mainLayout.addWidget(self.pbar)
        mainLayout.addWidget(self.button)

# ------------------------------------------------------------------
    def getBaseInfo(self):
        getBaseInfo = QWidget()
        layout = QVBoxLayout()

        # Number of rows of service function
        layout.serviceTextbox = QtWidgets.QSpinBox(self)
        layout.serviceTextbox.setRange(1, 100)
        layout.serviceTextbox.setValue(5)

        # Number of rows of customer login function
        layout.customerTextbox = QtWidgets.QSpinBox(self)
        layout.customerTextbox.setRange(1, 100)
        layout.customerTextbox.setValue(5)

        # Number of servers
        self.numOfServersTextbox = QtWidgets.QSpinBox(self)
        self.numOfServersTextbox.setRange(1, 9999999)
        self.numOfServersTextbox.setValue(3)

        # Number of customers
        self.numOfCustomersTextbox = QtWidgets.QSpinBox(self)
        self.numOfCustomersTextbox.setRange(1, 2147483647)
        self.numOfCustomersTextbox.setValue(400)

        # create labels
        layout.label_1 = QtWidgets.QLabel("تعداد سطرهای تابع زمان خدمت دهی")
        layout.label_2 = QtWidgets.QLabel('تعداد سطرهای تابع مدت بین دو ورود')
        layout.label_3 = QtWidgets.QLabel("تعداد خدمت دهندگان")
        layout.label_4 = QtWidgets.QLabel("تعداد مشتریان")
        layout.label_1.adjustSize()
        layout.label_2.adjustSize()
        layout.label_3.adjustSize()
        layout.label_4.adjustSize()

        # create calculate button
        self.tbtn = QtWidgets.QPushButton(self)
        self.tbtn.setText('تایید اطلاعات')
        self.tbtn.setFont(QtGui.QFont('Vazir', 11))
        self.tbtn.clicked.connect(lambda: functions.createProbTable(
            self, self.tabs, layout.serviceTextbox.value(), layout.customerTextbox.value(), self.numOfCustomersTextbox.value()))

        # Create a QGridLayout instance
        GridLayout = QGridLayout()
        GridLayout.setSpacing(10)

        # Add widgets to the layout
        GridLayout.addWidget(layout.serviceTextbox, 0, 0)
        GridLayout.addWidget(layout.customerTextbox, 1, 0)
        GridLayout.addWidget(self.numOfServersTextbox, 2, 0)
        GridLayout.addWidget(self.numOfCustomersTextbox, 3, 0)

        GridLayout.addWidget(layout.label_1, 0, 1, 1, 3)
        GridLayout.addWidget(layout.label_2, 1, 1, 1, 3)
        GridLayout.addWidget(layout.label_3, 2, 1, 1, 3)
        GridLayout.addWidget(layout.label_4, 3, 1, 1, 3)

        GridLayout.addWidget(self.tbtn, 4, 1, 1, 2)

        # Set the layout on the application's window
        getBaseInfo.setLayout(GridLayout)

        return getBaseInfo

# ------------------------------------------------------------------
    def getTables(self, m, n, p):
        getTables = QWidget()
        layout2 = QGridLayout()

        # Arrays to store probabilities and convert them to data-frames
        self.data_1 = [[0]*2]*m
        self.data_2 = [[0]*2]*n
        self.df_1 = pd.DataFrame(self.data_1, columns=[
                                 'احتمال', 'احتمال تجمعی'])
        self.df_2 = pd.DataFrame(self.data_2, columns=[
                                 'احتمال', 'احتمال تجمعی'])

        self.table_1 = QTableView()
        self.table_2 = QTableView()
        header_1 = self.table_1.horizontalHeader()
        header_1.setSectionResizeMode(QHeaderView.Stretch)
        header_2 = self.table_2.horizontalHeader()
        header_2.setSectionResizeMode(QHeaderView.Stretch)

        # Build a Object from a NormalTableModel class
        self.model_1 = NormalTableModel(self.df_1)
        self.table_1.setModel(self.model_1)
        self.model_2 = NormalTableModel(self.df_2)
        self.table_2.setModel(self.model_2)

        self.rbtn = QtWidgets.QPushButton(self)
        self.rbtn.setText('تولید اعداد')
        self.rbtn.setFont(QtGui.QFont('Vazir', 11))

        self.rbtn.clicked.connect(lambda: functions.createRandom(self, self.tabs, m, n, p))

        self.label_1 = QtWidgets.QLabel('جدول احتمالات خدمت دهی')
        self.label_2 = QtWidgets.QLabel('جدول احتمالات مدت بین دو ورود')
        self.label_1.setStyleSheet('color:#999;')
        self.label_2.setStyleSheet('color:#999;')
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        layout2.addWidget(self.label_1, 0, 0, 1, 3)
        layout2.addWidget(self.label_2, 0, 3, 1, 3)
        layout2.addWidget(self.table_1, 1, 0, 1, 3)
        layout2.addWidget(self.table_2, 1, 3, 1, 3)
        layout2.addWidget(self.rbtn, 2, 2, 1, 2)
        getTables.setLayout(layout2)
        return getTables

# ------------------------------------------------------------------
    def getRandomTable(self, m, n, p):
        getRandomTable = QWidget()
        layout3 = QGridLayout()

        # Arrays to store customer arrival times and service times and convert them to data-frames
        self.randomData_1 = []
        self.randomData_2 = []
        Thread(target=functions.createRandomList(self.randomData_1, p, self.pbar, 1)).start()
        Thread(target=functions.createRandomList(self.randomData_2, p, self.pbar, 2)).start()

        # Calculate time from random numbers and probability tables
        for i in range(p):
            for j in range(m):
                if float(self.randomData_1[i][0]) <= float(self.df_1.iat[j, 1]):
                    self.randomData_1[i][1] = j+1
                    break

        for i in range(p):
            if i == 0:
                self.randomData_2[i][0] = 0
                self.randomData_2[i][1] = 0
            else:
                for j in range(n):
                    if float(self.randomData_2[i][0]) <= float(self.df_2.iat[j, 1]):
                        self.randomData_2[i][1] = j+1
                        break

        self.randomDf_1 = pd.DataFrame(self.randomData_1, columns=[
            'عدد رندوم', 'مدت خدمت دهی'])
        self.randomDf_2 = pd.DataFrame(self.randomData_2, columns=[
            'عدد رندوم', 'مدت بین دو ورود'])

        self.randomTable_1 = QTableView()
        self.randomTable_2 = QTableView()
        header_1 = self.randomTable_1.horizontalHeader()
        header_1.setSectionResizeMode(QHeaderView.Stretch)
        header_2 = self.randomTable_2.horizontalHeader()
        header_2.setSectionResizeMode(QHeaderView.Stretch)

        # Build a Object from a RandomTableModel class
        self.randomModel_1 = RandomTableModel(self.randomDf_1)
        self.randomTable_1.setModel(self.randomModel_1)
        self.randomModel_2 = RandomTableModel(self.randomDf_2)
        self.randomTable_2.setModel(self.randomModel_2)

        self.label_3 = QtWidgets.QLabel('جدول مدت خدمت دهی')
        self.label_4 = QtWidgets.QLabel('جدول مدت بین دو ورود')
        self.label_3.setStyleSheet('color:#999;')
        self.label_4.setStyleSheet('color:#999;')
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)

        layout3.addWidget(self.label_3, 0, 0, 1, 3)
        layout3.addWidget(self.label_4, 0, 3, 1, 3)
        layout3.addWidget(self.randomTable_1, 1, 0, 1, 3)
        layout3.addWidget(self.randomTable_2, 1, 3, 1, 3)
        # layout3.addWidget(self.rbtn, 2, 2, 1, 2)
        getRandomTable.setLayout(layout3)
        return getRandomTable

    def mainCalculation(self, data1, data2, data3, data4, progressbar):
        result, numQueue, path, simuEndTime = simulation.mainCalculation(
            self, data1, data2, data3, data4, progressbar)
        resultDialog = ResultWindow(result, data3, numQueue, path, simuEndTime)
        resultDialog.show()
        resultDialog.exec_()
