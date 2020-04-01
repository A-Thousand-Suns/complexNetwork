import process.egoNetworkProcess
import networkx as nx
import threading

def processFunc(sampleFile, k, processResultFile):
    G = nx.read_edgelist(sampleFile)
    c = process.egoNetworkProcess.egoNetworkProcess(G, k, processResultFile)
    c.run()

if __name__ == '__main__':
    k = 2
    sampleNetworkPath = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\sampleNetwork\network_'
    processResultPath = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\processResult\network_'
    fileList = ['1', '2', '3', '4', '5', '6', '8', '9']
    for i in fileList:
        t = threading.Thread(target=processFunc, args=(sampleNetworkPath+i+r'\network.dat', k, processResultPath+i+'.dat'))
        t.run()