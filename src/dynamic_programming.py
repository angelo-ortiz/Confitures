# -*- coding: utf-8 -*-
from math import inf
from tools import printSolution

def AlgoProgDyn(k, V, S, display=True):
	""" int x list[int] x int x bool -> int x list[int]
	returns the optimum number of jars as a whole
	and for every jar type as obtained by the
	dynamic programming algorithm
	"""
	# M: list[list[int]]
	M = ConfitureForwards(k, V, S)
	# A: list[int]
	A = ConfitureBackwards(k, V, S, M)
	return M[S][k], A

def ConfitureForwards(k, V, S):
	""" int x list[int] x int -> list[list[int]]
	returns the matrix <M> containing the optimum
	number of jars for every subproblem
	"""
	# M: list[list[int]]
	M = initMatrix(S+1, k+1)
	# s, i: int
	for s in range(S+1):
		for i in range(k+1):
			M[s][i] = getMsi(V, M, s, i)
	return M

def initMatrix(rows, columns):
	""" int x int -> list[list[int]]
	returns a <rows>x<columns> matrix initialised
	to +infinity for each and every cell of its
	"""
	# M: list[list[int]]
	M = []
	# r: int
	for r in range(rows):
		M.append([inf]*columns)
	return M

def getMsi(V, M, s, i):
	""" list[int] x list[list[int]] x int x int -> int
	returns M[s][i], i.e. the optimum number of
	jars for a confiture quantity of <s> and the
	system of capacities V[1..i]
	
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
	returns a list of integers corresponding to
	the number of jars used of each capacity
	type V[i] in the optimum solution given by M
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
