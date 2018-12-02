# -*- coding: utf-8 -*-
from tools import generateSavePath, writeLine, timeFunction
from dynamic_programming import AlgoProgDyn
from greedy_algorithm import AlgoGlouton, TestGloutonCompatible
import random

def generateRandomSystem(k, p_max):
	""" int x int -> list[int]
	returns a list of integers corresponding
	to a randomly generated system of <k> 
	capacities whose maximum value is <p_max> 
	"""
	# V: list[int]
	V = [1]
	# i, val: int
	i = 1
	while i < k:
		val = random.randint(2, p_max)
		if val not in V:
			V.append(val)
			i += 1
	return sorted(V)
		
def gloutonCompatibleSystemsProportion(k_min=10, k_max=100, p_max=1000, no_sys=20):
	""" int x int x int x int -> float
	returns the proportion of greedy-compatible
	systems of capacities whose:
	- length ranges from <k_min> to <k_max>
	- maximum capacity value is set to <p_max>
	N.B. the tests were carried out for
	<no_sys> systems of each length
	"""
	# n, g, k, i: int
	n = 0
	g = 0
	for k in range(k_min, k_max+1):
		for i in range(no_sys):
			# V: list[int]
			V = generateRandomSystem(k, p_max)
			if TestGloutonCompatible(k, V):
				g += 1
			n += 1
	print(g, n)
	return g / n

def nonGloutonCompatibleSystemsData(k_min=10, k_max=100, p_max=1000, no_sys=10, f=10000):
	""" int x int x int x int x int ->
	writes in the file <fn> the time and
	the obtained number of jars for both
	the dynamic programming and greedy
	algorithms for non-greedy-compatible
	systems (see above) and a confiture
	quantity varying from <p_max> to
	<f*p_max>
	"""
	# fn: str
	global fn
	# writeLine(fn, 'dp_t\t\t\tdp_n\tga_t\t\t\tga_n\n', mode='w')
	for k in range(k_min, k_max+1):
		for i in range(no_sys):
			# V: list[int]
			V = generateRandomSystem(k, p_max)
			if not TestGloutonCompatible(k, V):
				for S in range(p_max, f*p_max+1):
					dp_t, dp_n = timeFunction(AlgoProgDyn, k, V, S)
					ga_t, ga_n = timeFunction(AlgoGlouton, k, V, S)
					writeLine(fn, f'{dp_t:.6e}\t{dp_n}\t\t{ga_t:.6e}\t{ga_n}\n')

def greedyOptimalityStatistics():
	""" -> float x int x float x float x float x float x float x float
	returns the average and greatest gaps
	between the dynamic programming and the 
	greedy algorithm performances obtained
	from the data file <fn>
	"""
	def totalGreatest(td, gd, d):
		""" number x number x number -> number x number
		returns the sum of <td> and <d>,
		and the greatest number so far
		between <gd> and <d>
		"""
		if d > gd:
			gd = d
		return td+d, gd

	# noGC, td_n, gd_n: int
	noGC = 0
	td_n = 0
	gd_n = 0
	# td_np, gd_np, td_t, gd_t, td_tp, gd_tp: float
	td_np = 0.
	gd_np = 0.
	td_t = 0.
	gd_t = 0.
	td_tp = 0.
	gd_tp = 0.
	# fn: str
	global fn	
	with open(fn, 'r') as f:
		for line in f:
			noGC += 1
			dp_t, dp_n, ga_t, ga_n = tuple(map(float, line.split()))
			td_n, gd_n = totalGreatest(td_n, gd_n, ga_n - dp_n)
			td_np, gd_np = totalGreatest(td_np, gd_np, (ga_n - dp_n) / dp_n)
			td_t, gd_t = totalGreatest(td_t, gd_t, dp_t - ga_t)
			td_tp, gd_tp = totalGreatest(td_tp, gd_tp, (dp_t - ga_t) / ga_t)
	return td_n / noGC, gd_n, td_np / noGC, gd_np, td_t / noGC, gd_t, td_tp / noGC, gd_tp

def printStatistics(ag_n, gg_n, ag_np, gg_np, ag_t, gg_t, ag_tp, gg_tp):
	""" float x int x float x float x float x float x float x float ->
	prints the statistics associated to the
	8 parameters
	"""
	def averageGreatest(av, gr):
		"""
		"""
		print(f"\tThe average gap is {av:3.2e}")
		print(f"\tThe greatest gap is {gr:3.2e}")
	
	print("================================================================")
	print("Comparison between the greedy and dynamic programming algorithms")
	print("Number of jars (best: dynamic programming)")
	averageGreatest(ag_n, gg_n)
	print("Percentage of the number of jars")
	averageGreatest(100*ag_np, 100*gg_np)
	print("Execution time (best: greedy algorithm)")
	averageGreatest(ag_t, gg_t)
	print("Percentage of the execution time")
	averageGreatest(100*ag_tp, 100*gg_tp)
	print("================================================================")

if __name__ == '__main__':
	# p: float
	p = gloutonCompatibleSystemsProportion(k_max=100, p_max= 200, no_sys=20)
	print(f"The percentage of greedy-compatible systems is {100*p}")
	# fn: str
	fn = generateSavePath('stats.txt')
	# nonGloutonCompatibleSystemsData(no_sys=1, f=10)
	printStatistics(*greedyOptimalityStatistics())
