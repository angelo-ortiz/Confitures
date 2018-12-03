# -*- coding: utf-8 -*-
from math import inf
from tools import printSolution

def RechercheExhaustive(k, V, S, display=True):
	""" int x list[int] x int x bool -> int x list[int]
	returns the optimum number of jars as a whole
	as obtained by the exhaustive search algorithm
	"""
	# n: int
	n = RechercheExhaustiveRec(k, V, S)
	return n, None

def RechercheExhaustiveRec(k, V, s):
	""" int x list[int] x int -> int
	returns the optimum number of jars obtained for
	a confiture quantity of <s> and for a system of
	capacities <V>
	"""
	# NbCont, x: int
	if s < 0:
		return inf
	elif s == 0:
		return 0
	else:
		NbCont = s
		for i in range(k):
			x = RechercheExhaustiveRec(k, V, s-V[i])
			if x+1 < NbCont:
				NbCont = x + 1
		return NbCont
