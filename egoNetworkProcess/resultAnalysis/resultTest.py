import threading

import networkx as nx


class test:
    def __init__(self, networkPath, modulePath, resultPath, storePath):
        self.networkPath = networkPath
        self.modulePath = modulePath
        self.resultPath = resultPath
        self.storePath = storePath

    def readModuleFile(self):
        moduleDic = {}
        moduleId = []
        with open(self.modulePath, 'r') as file:
            for i in file.readlines():
                temStr = i.replace('\n', '')
                temStr = temStr.strip()
                str = temStr.split('\t')
                nodeId = str[0]
                for j in str[1].split(' '):
                    moduleId.append(j)
                moduleDic[nodeId] = moduleId
                moduleId = []

        print(moduleDic)
        return moduleDic

    def getAnswerDic(self):
        answerDic = {}
        moduleDic = self.readModuleFile()
        G = nx.read_edgelist(self.networkPath)

        for i in G.nodes:
            G.nodes[i]['moduleId'] = moduleDic[i]

        for i in G.nodes:
            neighbors = list(G.neighbors(i))
            answerDic[i] = neighbors

            for j in neighbors:
                if ((set(G.nodes[j]['moduleId']) & set(G.nodes[i]['moduleId'])).__len__() == 0):
                    answerDic[i].remove(j)
        print(answerDic)
        return answerDic

    def getResultDic(self):
        sum = 0
        resultDic = {}
        neighborList = []

        with open(self.resultPath, 'r') as file:
            for i in file.readlines():
                sum = sum + 1
                temStr = i.replace('\n', '')
                temStr = temStr.strip()
                str = temStr.split('\t')

                for j in str[1].split():
                    neighborList.append(j)
                resultDic[str[0]] = neighborList
                neighborList = []

        return resultDic

    def getAccuracy(self):
        answerDic = self.getAnswerDic()
        resultDic = self.getResultDic()
        answerSumForAll = 0
        resultSumForAll = 0
        rightNumForAll = 0

        with open(self.storePath, 'w+') as file:
            file.truncate()
            file.write('Node' + '\t' + 'P' + '\t' + 'R' + '\n')

        for i in answerDic:
            answerSumForNode = answerDic[i].__len__()
            answerSumForAll = answerSumForAll + answerSumForNode
            resultSumForNode = resultDic[i].__len__()
            resultSumForAll = resultSumForAll + resultSumForNode
            rightNumForNode = 0

            for j in answerDic[i]:
                if (j in resultDic[i]):
                     rightNumForNode = rightNumForNode + 1
            rightNumForAll = rightNumForAll + rightNumForNode
            accuracyP = "%.2f%%" % ((rightNumForNode/answerSumForNode)*100)

            if (resultSumForNode == 0 ):
                accuracyR = 0
            else:
                accuracyR = "%.2f%%" % ((rightNumForNode/resultSumForNode)*100)
            print(str(i) + '\t' + str(accuracyP) + '\t' + str(accuracyR) + '\n')
            with open(self.storePath, 'a') as file:
                file.write(str(i) + '\t' + str(accuracyP) + '\t' + str(accuracyR) + '\n')
            accuracyP = 0
            accuracyR = 0

        accuracyPAll = "%.2f%%" % ((rightNumForAll/resultSumForAll)*100)
        accuracyRAll = "%.2f%%" % ((rightNumForAll/answerSumForAll)*100)

        with open(self.storePath, 'r+') as file:
            old =file.read()
            file.seek(0)
            file.write('P:' + str(accuracyPAll) + '\t' + 'R:' + str(accuracyRAll) + '\n')
            file.write('----------------------------\n')
            file.write(old)

    def run(self):
        tGetAnswerDic = threading.Thread(target=self.getAnswerDic)
        tGetResultDic = threading.Thread(target=self.getResultDic)
        tGetAccuracy = threading.Thread(target=self.getAccuracy, args=(tGetAnswerDic.run(), tGetResultDic.run(),))
        tGetAccuracy.run()




