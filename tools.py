# -*- coding: utf-8 -*-
def readFile(fn):
    """
    str : filename
    """
    with open(fn, "r") as f:
        args = f.readline().split()
        S, k = tuple(map(int, args))
        caps = f.readline().split()
        V = list(map(int, caps))
        if len(V) != k:
            print("Error: incorrect number of capacities")
            exit(1)
        return S, k, V
