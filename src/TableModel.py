from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd
from decimal import Decimal
from src.functions import *


class NormalTableModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            if not functions.is_number(value):
                functions.showDialog(
                    'error', 'امکان وارد کردن حروف وجود ندارد.')
            elif float(value) > 1:
                functions.showDialog('error', 'احتمال باید بین 0 و 1 باشد.')
            elif index.column() == 0:
                self._data.iloc[index.row(), index.column()] = Decimal(value)

                for i in range(0, len(self._data)):
                    if i == 0 and self._data.iloc[i, 0] != 0:
                        self._data.iloc[i, 1] = self._data.iloc[i, 0]

                    elif self._data.iloc[i, 0] != 0:
                        self._data.iloc[i, 1] = self._data.iloc[i,
                                                                0] + self._data.iloc[i-1, 1]
                return True
        return False

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return list(range(1, len(self._data)+1))[section]
        return None

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        elif index.column() == 1:
            return Qt.ItemIsSelectable
        


class RandomTableModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return list(range(1, len(self._data)+1))[section]
        return None

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        elif index.column() == 1:
            return Qt.ItemIsSelectable