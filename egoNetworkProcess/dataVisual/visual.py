import numpy as np
from matplotlib import pyplot as plt

def importData():
    path = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\testResult\network_'
    fileList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
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
                    lable.append(content[23:-1])

                if (flag == 2):
                    temData.append(content)

                flag = flag + 1
    for i in temData:
        dataP.append(float(i.replace('\n', '').split('\t')[0].replace('%','')))
        dataR.append(float(i.replace('\n', '').split('\t')[1].replace('%','')))

    print(lable)
    print(dataP)
    print(dataR)
    plt.xticks(range(len(lable)), lable, rotation=45)
    x = range(len(lable))
    y = np.array(dataR)
    plt.bar(x, y)
    plt.show()

if __name__ =='__main__':
    importData()

