# -*- coding: utf-8 -*-
def readFile(fn):
    """ str -> int x int x list[int]
    
    """
    with open(fn, "r") as f:
        args = f.readline().split()
        S, k = tuple(map(int, args))
        caps = f.readline().split()
        V = list(map(int, caps))
        return S, k, V

def writeLine(fn, line):
    """ str x list[str] ->
    
    """
    with open(fn, 'a') as f:
        f.write(line)

def validateData(S, k, V):
	""" int x int x list[int]
	"""
	if len(V) != k:
		print(f'Error: the number of capacities ({len(V)}) does not match k = {k}')
		exit(1)
	V.sort()
	for i in range(1, k):
		if V[i-1] == V[i]:
			print('Error: there are at least two equal capacities')
			exit(1)        
        
def printSolution(name, n, A=None, V=None, verbose=False):
	""" str x int x list[int] x list[int] x bool ->
	
	"""
	print(f'The {name} algorithm found an optimum solution using {n} jars')
	if verbose and A:
		print('capacity\tquantity')
		for i in range(len(V)):
			print(f'{V[i]}\t\t{A[i]}')
