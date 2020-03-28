import networkx as nx
import threading
import infomap

class egoNetworkProcess:
    def __init__(self, G, k, storePath):
        self.G = G
        self.k = k  #k-step neighbor
        self.storePath = storePath
        self.writeNetworkLock = threading.Lock()
        self.writeModuleLock = threading.Lock()
        self.writeResultLock = threading.Lock()

    def createEgoNetwork(self, sourceNode): #create the egonetwork of the source node
        tempG = nx.ego_graph(self.G, sourceNode, self.k)
        self.egoNetwork = tempG
        return tempG

    def findKey(self, dic, value):
        return list(dic.keys())[list(dic.values()).index(value)]

    def runInfo(self, temG):  #run infomap argorithm on the egonetwork
        nodesId = [i for i in range(1, temG.number_of_nodes() + 1)]
        nodesName = list(temG.nodes)
        nodesDic = dict(zip(nodesId, nodesName))
        print(nodesDic)
        linksList = []

        for i in list(temG.edges):
            singleLink = (self.findKey(nodesDic, i[0]), (self.findKey(nodesDic, i[1])))
            linksList.append(singleLink)

        linksTup = tuple(linksList)
        print(linksTup)
        im = infomap.Infomap()
        im.add_links(linksTup)
        im.run()
        moduleResult = im.get_modules()
        print(moduleResult)
        return moduleResult, nodesDic

    def getResult(self, sourceNode):
        result = []
        temG = self.createEgoNetwork(sourceNode)
        moduleResult, nodesDic = self.runInfo(temG)

        for i in list(temG.nodes):
            temG.nodes[i]['moduleId'] = moduleResult[self.findKey(nodesDic, i)]

        sourceNodeNeighbor = list(self.G.neighbors(sourceNode))

        for i in sourceNodeNeighbor:
            if (temG.nodes[i]['moduleId'] == temG.nodes[sourceNode]['moduleId']):
                result.append(i)

        self.writeResultLock.acquire()
        with open(self.storePath, 'a') as file:
            file.write(str(sourceNode) + '\t')
            for i in result:
                file.write(str(i) + ' ')
            file.write('\n')
        self.writeResultLock.release()

        # self.writeNetworkLock.acquire()
        # with open('network.dat', 'a') as file:
        #     for i in temG.edges:
        #         file.write(str(i[0]) + ' ' + str(i[1]) + '\n')
        # self.writeNetworkLock.release()
        #
        # self.writeModuleLock.acquire()
        # with open('module.dat', 'a') as file:
        #     for i in temG.nodes:
        #         file.write(str(i) + ' ' + str(temG.nodes[i]['moduleId']) + '\n')
        #     file.write('--------------------------\n')
        # self.writeModuleLock.release()

    def run(self):
        # for i in ['network.dat', 'module.dat', 'result.dat']:
        #     with open(i, 'w+') as file:
        #         file.truncate()
        with open(self.storePath, 'w+') as file:
            file.truncate()

        for i in self.G.nodes:
            thread = threading.Thread(target=self.getResult, args=(i,))
            thread.run()










