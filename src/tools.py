# -*- coding: utf-8 -*-
import timeit

def generateSavePath(fn, dn='data'):
	""" str x str -> str
    returns a string corresponding to the absolute
	path of the data file <fn>
	"""
	from os.path import dirname, realpath, join
	return join(dirname(dirname(realpath(__file__))), dn, fn)
                     
def readFile(fn):
    """ str -> int x int x list[int]
    reads the data file <fn> and returns the
    confiture quantity, the length of the system
    of capacities and the system itself
    """
    with open(fn, "r") as f:
        args = f.readline().split()
        S, k = tuple(map(int, args))
        caps = f.readline().split()
        V = list(map(int, caps))
        return S, k, V

def writeLine(fn, line, mode='a'):
    """ str x list[str] ->
    writes the string <line> into the data
    file <fn> on mode:
    - 'a' = append
    - 'w' = overwrite
    """
    with open(fn, mode) as f:
        f.write(line)

def validateData(S, k, V):
	""" int x int x list[int]
	checks that the length system of capacities
	<V> matches <k> and that the capacities are
	ordered in an ascending way, otherwise it
	terminates the programme
	"""
	if len(V) != k:
		print(f'Error: the number of capacities ({len(V)}) does not match k = {k}')
		exit(1)
	V.sort()
	for i in range(1, k):
		if V[i-1] == V[i]:
			print('Error: there are at least two equal capacities')
			exit(1)        
        
def printSolution(name, res, V=None, verbose=True):
	""" str x tuple[int, list[int]] x list[int] x list[int] x bool ->
	prints the results ofthe algorithm <name>
	and eventually the number of jars of each
	capacity depending on <verbose>
	"""
	print(f'The {name} algorithm found an optimum solution using {res[0]} jars')
	if verbose and (res[1] is not None):
		print('capacity\tquantity')
		for i in range(len(V)):
			print(f'{V[i]}\t\t{res[1][i]}')

def timeFunction(f, k, V, S):
	""" (int x list[int] x int x bool -> tuple[int, _]) x int x list[int] x int -> 
	tuple[float, int]
	returns the execution time of the function
	<f> for the given arguments, and the number
	of jars of the its solution
	"""
	# t0, tf: float
	t0 = timeit.default_timer()
	# n: int
	n,_ = f(k, V, S, display=False)
	tf = timeit.default_timer()
	return (tf - t0, n)
			
