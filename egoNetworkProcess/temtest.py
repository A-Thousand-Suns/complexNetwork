import networkx as nx
import copy
import random
import os
import re
import matplotlib.pyplot as plt

def showGraphTest():
    path = r'G:\研究生阶段文档\导师任务\egoNetworkProcess3_24\network.dat'
    G = nx.read_edgelist(path)
    nx.draw_networkx(G)
    plt.show()

def findKey(dic,value):
    return list(dic.keys())[list(dic.values()).index(value)]

def randomWalk(G, sourceNode, k):
    tempG = copy.deepcopy(G)
    linkList = []
    path = [sourceNode]
    for i in range(k):
        neighborList = list(G.neighbors(path[i]))
        print(path[i])
        print(neighborList)
        neighborSelected = random.choice(neighborList)
        path.append(neighborSelected)
        print('-----------------------')

    for i in range(path.__len__() - 1):
        linkList.append((path[i], path[i+1]))
    print(path)
    print(linkList)
    temG = nx.Graph()
    temG.remove_node()
    temG.add_edges_from(linkList)
    nx.draw_networkx(temG)
    plt.show()
    print('-----------------------')

def egoGraphTest(G, sourceNode):
    temG = nx.ego_graph(G, sourceNode, 1)
    nx.draw_networkx(temG)
    plt.show()

def typeTest():
    path = r'E:\编程文件\Python\complexNetwork\test.gexf'
    name, type = os.path.splitext(path)
    print(type)
    G = nx.Graph()
    G.number_of_nodes()

def numOfNdoesTest():
    path = r'G:\研究生阶段文档\Complex Network Datasets\Complex Network Datasets\For Community\football\football.gml'
    G = nx.read_gml(path)
    print(G.number_of_nodes())

def readfileTest():
    path = r'E:\benchmark\benchmark\benchmark\Debug\community.dat'
    #path =r'G:\研究生阶段文档\Complex Network Datasets\Complex Network Datasets\For Community\football\football.gml'
    moduleDic = {}
    with open(path, 'r') as file:
        for i in file.readlines():
            temStr = i.replace('\n', '')
            str = temStr.split('\t')
            nodeId = str[0]
            moduleId = int(str[1])
            moduleDic[nodeId] = moduleId
    print(moduleDic)
    G = nx.Graph()
    return moduleDic

def egoNetworkModuleTest():
    answerDit = {}
    moduleDic = readfileTest()
    path = r'E:\benchmark\benchmark\benchmark\Debug\network.dat'
    G = nx.read_edgelist(path)
    for i in G.nodes:
        G.nodes[i]['moduleId'] = moduleDic[i]

    for i in G.nodes:
        neighbors = list(G.neighbors(i))
        answerDit[i] = neighbors
        for j in neighbors:
            if(G.nodes[j]['moduleId'] != G.nodes[i]['moduleId']):
                answerDit[i].remove(j)
    #print(answerDit)
    return answerDit

def readResultTest():
    sum = 0
    resultDic = {}
    neighborList = []
    path =  r'E:\编程文件\Python\complexNetwork\egoNetworkProcess3_24\result.dat'
    with open(path, 'r') as file:
        for i in file.readlines():
            sum = sum +1
            temStr = i.replace('\n', '')
            str = temStr.split('\t')
            for j in str[1].split():
                neighborList.append(j)
            #print(str[0], neighborList)
            resultDic[str[0]] = neighborList
            neighborList = []
    #print(resultDic)
    return resultDic

def accuracyTest():
    answerDic = egoNetworkModuleTest()
    resultDic = readResultTest()
    print(answerDic['589'])
    print(resultDic['589'])
    for i in answerDic:
        answerSum = answerDic[i].__len__()
        resultSum = resultDic[i].__len__()

        rightNum = 0
        for j in answerDic[i]:
            if (j in resultDic[i]):
                 rightNum = rightNum + 1
        rightPercent = "%.2f%%" % ((rightNum/answerSum)*100)
        #print(i, rightPercent)
        rightPercent = 0

def getPathTest():
    path = 'E:\编程文件\Python\complexNetwork\egoNetworkProcess_323.py'
    pattern = r"(.+)\\"
    result = re.findall(pattern, path)
    print(type(result))

def readComFileTest():
    path = r'E:\benchmark\benchmark\benchmark\Debug\community.dat'
    list =[]
    with open(path, 'r', encoding='utf-8') as file:
        for i in file.readlines():
            str = i.replace('\n', '')
            str = str.strip()
            str = str.split('\t')
            for i in str[1].split(' '):
                list.append(i)
            print(str[0], list)
            list = []

def listEqualTest():
    listA = [1, 2, 3]
    listB = [2, 3, 4]
    print((set(listA) & set(listB)).__len__())


def fileOpenTest():
    path = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\sampleNetwork\network_1\community.dat'
    with open(path, 'r') as file:
        for i in file.readlines():
            print(i)

def readResultTest():
    neighborList = []
    resultDic = {}
    resultPath = r'E:\编程文件\python\complexNetwork\egoNetworkProcess\processResult\network_1.dat'
    with open(resultPath, 'r') as file:
        for i in file.readlines():
            temStr = i.replace('\n', '')
            temStr = temStr.strip()
            str = temStr.split('\t')
            print(str)
            print(str.__len__() == 1)
            if (str.__len__() == 1):
                print(temStr)
                resultDic[temStr] = neighborList
                neighborList = []
                continue



            for j in str[1].split():
                neighborList.append(j)

            resultDic[str[0]] = neighborList
            neighborList = []
        print(resultDic)

def dicRemoveTest():
    a = {1:[2, 3, 4]}
    for i in a:
        print(i)


if __name__ == '__main__':
    readResultTest()
    pass

