# -*- coding: utf-8 -*-
from tools import generateSavePath, writeLine, timeFunction
from exhaustive_search import RechercheExhaustive
from dynamic_programming import AlgoProgDyn
from greedy_algorithm import AlgoGlouton
from math import inf
import random

def generateBenchmarkSavePath(fct, d_value, dn='data'):
	""" str x int -> str
	returns a string corresponding to the absolute
	path of the function <fct>'s data file for the
	the generator <d_value> of the system of
	capacities
	"""
	return generateSavePath(fct + f'_d{d_value}.txt')
                     
def generateExpoSystem(d, k):
	""" int x int -> list[int]
	returns a system of <k> capacities generated
	by <d>
	"""
	# V: list[int]
	V = [1]
	# val: int
	val = 1
	for i in range(k-1):
		val *= d
		V.append(val)
	return V

def generateSvalues():
	""" -> list[int]
	returns a list of all the S quantities that
	are going to be tested afterwards
	"""
	# base, values: list[int]
	base = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
	values = []
	# b, tmp: int
	tmp = base[0]
	for b in base[:-1]:
		while tmp < 10*b:
			values.append(tmp)
			tmp += b
	values.append(base[-1])
	return values
		

if __name__ == '__main__':
	d_values = [2, 3, 4]
	fct = [RechercheExhaustive, AlgoProgDyn, AlgoGlouton]
	fstr = ['es', 'dp', 'ga']
	S_values = generateSvalues()
	k_values = [2, 4, 6, 8, 10]
	print('Starting benchmark ...')
	for d in d_values:
		contd = [inf]*3
		fn = [None]*3
		for k in k_values:
			V = generateExpoSystem(d, k)
			for i in range(len(fct)):
				if fn[i] is None:
					fn[i] = generateBenchmarkSavePath(fstr[i], d)
					# writeLine(fn[i], 'k\ttime for various S values\n', mode='w')
				line = f'{k}'
				for S in S_values:
					if S >= contd[i]:
						break
					time, _ = timeFunction(fct[i], k, V, S)
					line += f'\t{time:.6e}'
					if time >= 60:
						contd[i] = S
				writeLine(fn[i], line + '\n')
			print(contd)
		print(f'The tests for d={d} finished correctly')
	print('Benchmark done!')
			

