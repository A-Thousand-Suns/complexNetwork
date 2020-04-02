import argparse
import resultTest

def parse_args():
    parse = argparse.ArgumentParser(description='Run resultAnalysis function')
    parse.add_argument('--network', required=True, help='input the network file')
    parse.add_argument('--community', required=True, help='input the module file')
    parse.add_argument('--result', required=True, help='input the result file')
    parse.add_argument('--output', default='accuracy.dat', help='input accuracy file')
    return parse.parse_args()

def main():
    c = resultTest.test(args.network, args.community, args.result, args.output)
    c.run()

if __name__ == '__main__':
    args = parse_args()
    main()
    print('done')
