# -*- coding: utf-8 -*-
from math import inf
from tools import printSolution

def AlgoGlouton(k, V, S, display=True):
	""" int x list[int] x int x bool -> int x list[int]
	returns the least possible number of jars as
	a whole and for every jar type as obtained
	by the greedy algorithm
	"""
	# A: list[int]
	A = [0]*k
	# s, i, n: int
	s = S
	i = k
	n = 0
	while s != 0:
		A[i-1] = s // V[i-1]
		s %= V[i-1]
		n += A[i-1]
		i -= 1
	return n, A

def TestGloutonCompatible(k, V):
	""" int x list[int] -> bool
	checks whether the system of capacities
	<V> is greedy-compatible or not
	"""
	if k >= 3:
		# S: int
		for S in range(V[2]+2, V[k-2]+V[k-1]):
			# j: int
			for j in range(k):
				if V[j] < S:
					# n, m: int
					n,_ = AlgoGlouton(k, V, S, display=False)
					m,_ = AlgoGlouton(k, V, S-V[j], display=False)
					if n > m+1:
						return False
	return True
