import threading
import resultAnalysis.resultTest

def testFunc(networkFile, communityFile, resultFile, testResultFile):
    c = resultAnalysis.resultTest.test(networkFile, communityFile, resultFile, testResultFile)
    c.run()

if __name__ == '__main__':
    samplePath = r'E:\编程文件\python\egoNetworkProcess\sampleNetwork/network_'
    resultPath = r'E:\编程文件\python\egoNetworkProcess\processResult/network_'
    storePath = r'E:\编程文件\python\egoNetworkProcess\testResult/network_'
    fileList = ['1', '2', '3', '4', '5', '6', '8', '9']
    for i in fileList:
        t = threading.Thread(target=testFunc, args=(samplePath+i+r'\network.dat', samplePath+i+'\community.dat',
                                                    resultPath+i+'.dat', storePath+i+'.dat'))
        t.run()