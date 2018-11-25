# -*- coding: utf-8 -*-
from math import inf
from tools import printSolution

def AlgoProgDyn(k, V, S, display=True):
	""" int x list[int] x int x bool ->
	
	"""
	# M: list[list[int]]
	M = ConfitureForwards(k, V, S)
	# A: list[int]
	A = ConfitureBackwards(k, V, S, M)
	if display:
		printSolution("dynamic programming", M[S][k], A, V, True)

def ConfitureForwards(k, V, S):
	""" int x list[int] x int -> list[list[int]]
	
	"""
	# M: list[list[int]]
	M = initMatrix(S+1, k+1)
	for s in range(S+1):
		for i in range(k+1):
			M[s][i] = getMsi(V, M, s, i)
	return M

def initMatrix(rows, columns):
	""" int x int -> list[list[int]]
	
	"""
	M = []
	for r in range(rows):
		M.append([inf]*columns)
	return M

def getMsi(V, M, s, i):
	""" list[int] x list[list[int]] x int x int -> int
	
	"""
	if s == 0:
		return 0
	elif s < 0:
		return inf
	elif i == 0:
		return inf
	elif M[s][i] < inf:
		return M[s][i]
	else:
		return min(getMsi(V,M,s,i-1), getMsi(V,M,s-V[i-1],i)+1)

def ConfitureBackwards(k, V, S, M):
	""" int x list[int] x int x list[list[int]] -> list[int]
	
	"""
	# A: list[int]
	A = [0]*k
	# s, i: int
	s = S
	i = k
	while s != 0:
		if (i > 0) and (M[s][i] == M[s][i-1]):
			i -= 1
		else:
			A[i-1] += 1
			s -= V[i-1]
	return A
