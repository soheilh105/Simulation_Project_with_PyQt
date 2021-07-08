from src.functions import *
from src.bcolors import bcolors
import pandas as pd
import numpy as np


class simulation():
    def mainCalculation(serviceData, customerData, p, s):
        resultData = np.zeros((p, 10))
        serverEndTime = [0]*s
        index = 0 # To store the number of the server that does the work
        value = 0 # To save when the server can do it (Service start time)

        for i in range(p):
            resultData[i][0] = i+1
            resultData[i][1] = customerData[i][1]
            resultData[i][2] = resultData[i-1][2]+resultData[i][1]
            resultData[i][3] = serviceData[i][1]

            index,value = simulation.defineServer(serverEndTime, resultData[i][2])
            resultData[i][4] = value
            resultData[i][5] = resultData[i][4]-resultData[i][2]
            resultData[i][6] = resultData[i][3]+resultData[i][4]
            resultData[i][7] = resultData[i][6]-resultData[i][2]
            resultData[i][8] = resultData[i][4]-serverEndTime[index]
            resultData[i][9] = index + 1
            serverEndTime[index] = resultData[i][6]

            print(f"{bcolors.OKGREEN}Customer {i+1} ... DONE{bcolors.RESET}")

        resultColumns = ['مشتری', 'مدت از آخرین ورود', 'زمان ورود', 'مدت خدمت دهی', 'زمان شروع خدمت',
                         'مدت ماندن مشتری در صف', 'زمان پایان خدمت', 'مدت ماندن مشتری در سیستم', 'مدت بیکاری خدمت دهنده', 'شماره خدمت دهنده']
        resultDataFrame = pd.DataFrame(resultData, columns=resultColumns)
        functions.toCsv(resultDataFrame)

    def defineServer(serverData, customerLoginTime):
        queue = False
        for index, value in enumerate(serverData):
            if (customerLoginTime >= value):
                return index,customerLoginTime
                break
            elif (index == len(serverData)-1):
                queue = True
        if queue:
            return serverData.index(min(serverData)),min(serverData)
