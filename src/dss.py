from config import *

PARENTS = []

def init_parents():
    global PARENTS
    PARENTS = list(range(VERTEX_AMOUNT))

def find(vertx):
    if PARENTS[vertx] == vertx:
        return vertx
    else:
        return find(PARENTS[vertx])


def merge(edge):
    PARENTS[find(edge[SOURCE])] = find(edge[TARGET])


def connectivityCheck():
    check = find(TERMINALS[T1_INDEX])
    if check != find(TERMINALS[T2_INDEX]) or check != find(TERMINALS[T3_INDEX]):
        return False
    return True
