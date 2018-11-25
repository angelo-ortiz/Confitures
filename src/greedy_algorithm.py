# -*- coding: utf-8 -*-
from math import inf
from tools import printSolution

def AlgoGlouton(k, V, S, display=True):
	""" int x list[int] x int x bool -> 
	
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
	if display:
		printSolution("greedy", n, A, V, True)
