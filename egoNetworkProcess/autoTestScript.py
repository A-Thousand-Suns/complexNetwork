import threading
import resultAnalysis.resultTest

def testFunc(networkFile, communityFile, resultFile, testResultFile):
    c = resultAnalysis.resultTest.test(networkFile, communityFile, resultFile, testResultFile)
    c.run()

if __name__ == '__main__':
    samplePath = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\sampleNetwork\network_'
    resultPath = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\processResult\network_'
    storePath = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\testResult\network_'
    fileList = ['1', '2', '3', '4', '5', '6', '8', '9']
    for i in fileList:
        t = threading.Thread(target=testFunc, args=(samplePath+i+r'\network.dat', samplePath+i+'\community.dat',
                                                    resultPath+i+'.dat', storePath+i+'.dat'))
        t.run()

    for i in fileList:
        with open(storePath+i+r'.dat', 'r+') as file:
            old = file.read()
            configFile = open(samplePath+i+r'\config.dat', 'r')
            configContent = configFile.read()
            file.seek(0)
            file.write(configContent + '\n')
            #file.write('\n')
            file.write(old)
            configFile.close()
