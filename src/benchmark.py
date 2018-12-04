# -*- coding: utf-8 -*-
from tools import generateSavePath, writeLine, timeFunction
from exhaustive_search import RechercheExhaustive
from dynamic_programming import AlgoProgDyn
from greedy_algorithm import AlgoGlouton
from math import inf
import random

def generateBenchmarkSavePath(fct, d_value):
	""" str x int -> str
	returns a string corresponding to the absolute
	path of the function <fct>'s data file for the
	the generator <d_value> of the system of
	capacities
	"""
	return generateSavePath(fct + f'_d{d_value}.txt')
                     
def generatePlotSavePath(fct, d_value, S_value):
	""" str x int -> str
	returns a string corresponding to the absolute
	path of the function <fct>'s data file for the
	the generator <d_value> of the system of
	capacities and a confiture quantity <S_value>
	"""
	return generateSavePath(fct + f'_d{d_value}_S{S_value}.txt')
                     
def generateExpoSystem(d, k):
	""" int x int -> list[int]
	returns a system of <k> capacities generated
	by <d>
	"""
	# V: list[int]
	V = [1]
	# val, i: int
	val = 1
	for i in range(k-1):
		val *= d
		V.append(val)
	return V

def generateSvalues(b=10, p=15):
	""" int x int -> list[int]
	returns a list of all the S quantities that
	are going to be tested afterwards
	"""
	# values: list[int]
	values = []
	# i, i_max: int
	i = b
	i_max = pow(b, p) 
	while i < i_max:
		values.extend(range(i, i*b, i))
		i *=b
	values.append(i_max)
	return values

def algorithmsBenchmark(fct, fstr, d_values, S_values, k_values):
	""" list[fun] x list[str] x list[int] x list[int] x list[int] ->
	
	"""
	print('Starting benchmark ...')
	# d, k, i, S: int
	for d in d_values:
		# contd, V: list[int]
		contd = [inf]*3
		# fn: list[str]
		fn = [None]*3
		for k in k_values:
			V = generateExpoSystem(d, k)
			for i in range(len(fct)):
				if fn[i] is None:
					fn[i] = generateBenchmarkSavePath(fstr[i], d)
					# writeLine(fn[i], 'k\ttime for various S values\n', mode='w')
				# line: str	
				line = f'{k}'
				for S in S_values:
					if S >= contd[i]:
						break
					# time: float
					time, _ = timeFunction(fct[i], k, V, S)
					line += f'\t{time:.6e}'
					if time >= 60.:
						contd[i] = S
				writeLine(fn[i], line + '\n')
			print(contd)
		print(f'The tests for d={d} finished correctly')
	print('Benchmark done!')

def generatePlotFiles(fct, d, S_plot, S_values):
	""" str x int x list[int] x list[int] ->
	"""
	# fn: str
	fn = generateBenchmarkSavePath(fct, d)
	# indices: list[int]
	indices = [S_values.index(S) for S in S_plot]
	# files: list[str]
	files = [generatePlotSavePath(fct, d, S) for S in S_plot]
	with open(fn, 'r') as f:
		# line: str
		for line in f:
			#line_str, list[str]
			line_str = line.split()
			# k: int
			k = int(line_str.pop(0))
			# line_values: list[number]
			line_values = list(map(float, line_str))
			# i: int
			for i in range(len(S_plot)):
				if indices[i] < len(line_values):
					writeLine(files[i], f'{k}\t{line_values[indices[i]]}\n')
	
if __name__ == '__main__':
	# fct: list[fun]
	fct = [RechercheExhaustive, AlgoProgDyn, AlgoGlouton]
	# fstr: list[str]
	fstr = ['es', 'dp', 'ga']
	# d_values, S_values, k_values: list[int]
	d_values = [2, 3, 4]
	S_values = generateSvalues(b=10, p=15)
	k_values = range(2, 31, 2)
	algorithmsBenchmark(fct, fstr, d_values, S_values, k_values)
	generatePlotFiles('ga', 2, [400000000, 4000000000, 40000000000], S_values)
	generatePlotFiles('dp', 3, [5000, 20000, 80000], S_values)
	generatePlotFiles('es', 4, [30, 40, 50], S_values)
