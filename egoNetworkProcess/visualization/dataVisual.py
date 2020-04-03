import numpy as np
import matplotlib.pyplot as plt

def importData():
    path = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\testResult\network_'
    fileList = ['1', '2', '3', '4', '5', '6', '8', '9']
    lable = []
    temData = []
    dataP = []
    dataR = []
    for i in fileList:
        flag = 0
        with open(path+i+'.dat', 'r') as file:
            while flag < 3:
                content = file.readline()
                if (flag == 0):
                    lable.append(content)

                if (flag == 2):
                    temData.append(content)

                flag = flag + 1

        print(lable)
        print(temData)

if __name__ =='__main__':
    importData()

