import egoNetworkProcess
import argparse
import networkx as nx
import os

def parse_args():
    parser = argparse.ArgumentParser(description='Run process function')

    parser.add_argument('--input', nargs='?', required=True,
                        help=r'input the graph path' )

    parser.add_argument('--k', default=2, choices=[2, 3], type=int,
                        help=r'input k-step')

    parser.add_argument('--output', default='result.dat', help=r'the path to store the result')

    return parser.parse_args()

def importGraph():
    #path =r'G:\研究生阶段文档\Complex Network Datasets\Complex Network Datasets\For Community\football\football.gml'
    path = args.input
    G = nx.Graph()
    name, type = os.path.splitext(path)
    if ((type == '.txt') or (type == '.dat')):
        G = nx.read_edgelist(path)
    if (type == '.gml'):
        G = nx.read_gml(path)
    return G

def main():
    G =importGraph()
    egoNetworkProcessC = egoNetworkProcess.egoNetworkProcess(G, args.k, args.output)
    egoNetworkProcessC.run()
    return

if __name__ == '__main__':
    args = parse_args()
    main()
    print('done')