from config import *
from dss import *
from random import random


def main():
    init()
    print('Terminals: {}'.format(TERMINALS))
    print('\tP\t|\tM=1000\t|\tM=10000')
    print('-'*50)
    for chance in P:
        print('\t'+format(chance, '.2f'), end='\t|\t')
        for m in M:
            r = 0
            for _ in range(m):
                for edge in EDGES:
                    if random() <= chance:
                        merge(edge)
                if connectivityCheck():
                    r += 1
                init_parents()
            print(format(r/m, '.4f'), end='\t|\t')
            if m == 10000:
                print()



def fix_vertices_index(array):
    for i in range(len(array)):
        array[i] -= 1


def init():
    init_parents()
    fix_vertices_index(TERMINALS)
    for edge in EDGES:
        fix_vertices_index(edge)


if __name__ == "__main__":
    main()
