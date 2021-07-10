from src.functions import *
import pandas as pd
import numpy as np


class simulation():
    def mainCalculation(self, serviceData, customerData, p, s):
        resultArray = np.zeros((p, 10))
        serversEndTime = [0]*s # To store when each servers is working until then
        index = 0  # To store the number of the server that does the work
        value = 0  # To save when the server can do it (Service start time)
        sumResult = [0]*8 
        numQueue = 0 # To save the number of people in the queue 

        for i in range(p):
            resultArray[i][0] = i+1
            resultArray[i][1] = customerData[i][1]
            resultArray[i][2] = resultArray[i-1][2]+resultArray[i][1]
            resultArray[i][3] = serviceData[i][1]

            index, value = simulation.defineServer(
                serversEndTime, resultArray[i][2])
            resultArray[i][4] = value
            resultArray[i][5] = resultArray[i][4]-resultArray[i][2]
            resultArray[i][6] = resultArray[i][3]+resultArray[i][4]
            resultArray[i][7] = resultArray[i][6]-resultArray[i][2]
            resultArray[i][8] = resultArray[i][4]-serversEndTime[index]
            resultArray[i][9] = index + 1
            serversEndTime[index] = resultArray[i][6]

            # To calculate the sum of each column
            for index in range(len(sumResult)):
                sumResult[index] += resultArray[i][index+1]
            print(f"Customer {i+1} ... DONE")

            # Add the total line
            # sumResult = ['مجموع'] + sumResult
            # print(sumResult)
            # np.vstack(resultArray, sumResult.insert(0, 'مجموع'))


        # To get the number of people in the queue
        for i in range(p):
            if resultArray[i][5] != 0:
                numQueue+=1

        resultColumns = ['مشتری', 'مدت از آخرین ورود', 'زمان ورود', 'مدت خدمت دهی', 'زمان شروع خدمت', 'مدت ماندن مشتری در صف', 'زمان پایان خدمت', 'مدت ماندن مشتری در سیستم', 'مدت بیکاری خدمت دهنده', 'شماره خدمت دهنده']
        resultDataFrame = pd.DataFrame(resultArray, columns=resultColumns)
        # toCsv function also export csv file, return path of saving file
        path = functions.toCsv(resultDataFrame)
        simulationEndTime = resultArray[p-1][6]
        
        for i in range(s):
            if serversEndTime[i] != simulationEndTime:
                sumResult[7] += (simulationEndTime-serversEndTime[i])
        
        return sumResult, numQueue, path, simulationEndTime

    def defineServer(serverData, customerLoginTime):
        queue = False
        for index, value in enumerate(serverData):
            if (customerLoginTime >= value):
                return index, customerLoginTime
                break
            elif (index == len(serverData)-1):
                queue = True
        if queue:
            return serverData.index(min(serverData)), min(serverData)
