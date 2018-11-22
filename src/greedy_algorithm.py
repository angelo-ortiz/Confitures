# -*- coding: utf-8 -*-
from math import inf
from tools import printSolution

def AlgoGlouton(k, V, S):
	"""
	int x list[int] x int -> 
	"""
	# A: list[int]
	A = [0]*k
	# s, i, n: int
	s = S
	i = k
	n = 0
	while s != 0:
		A[i-1] = s // V[i-1]
		s = s % V[i-1]
		n = n + A[i-1]
		i = i - 1
	printSolution("de l'algorithme glouton", n, A, V, True)
