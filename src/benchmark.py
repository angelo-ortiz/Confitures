# -*- coding: utf-8 -*-
from exhaustive_search import RechercheExhaustive
from dynamic_programming import AlgoProgDyn
from greedy_algorithm import AlgoGlouton
import random
import timeit

def generateSavePath(d_value, dn="data"):
    """ str x int -> str
    returns the absolute path of the file associated
    to the d=<d_value> time measuring be TODO
    """
    from os.path import dirname, realpath, join
    fn = f"d_{d_value}_results.txt"
    return join(dirname(dirname(realpath(__file__))), dn, fn)
                     
def generateV(d, k):
	""" int x int -> list[int]
	"""
	# V : list[int]
	V = [1]
	# val : int
	val = 1
	for i in range(k-1):
		val *= d
		V.append(val)
	return V

def generateSvalues():
	""" -> list[int]
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
		

def testFunction(f, k, V, S):
	""" (fun int x list[int] x int x bool -> _) x int x list[int] x int -> float
	"""
	t0 = timeit.default_timer()
	f(k, V, S, False)
	tf = timeit.default_timer()
	return (tf - t0)
			
# def sequenceAleatoire(n):
#     """ int -> str
#     rend une séquence aléatoire d'ADN de taille n 
#     """
#     seq = ''
#     for i in range(n):
#         seq += random.choice('AGCT')
#     return seq

# def mesureTimeRec(f, k_values, V, S):
# 	line = str(S)
# 	for k in k_values:
# 		t0 = timeit.default_timer()
# 		f(k, V, S)
# 		tf = timeit.default_timer()
# 		time = tf - t0
# 		line += "\t{time}"
# 	return line

# def test():
#     for i in range(11,19):
#         seq = SeqAleatoire(i)
#         print("i : " + str(i))
#         print("Rec : ")
#         mesureTimeRec(seq)
#         """print("Iter : ")
#         mesureTimeIter(seq)"""
#         print("==================================")

# def jeuEssai(seq):
#     print("Rec : ")
#     mesureTimeRec(seq)
#     print("==================================")
#     print("Iter : ")
#     mesureTimeIter(seq)

if __name__ == '__main__':
	# TODO a file per function + exh search always executing first
	# S case (must change)
	d_values = [2, 3, 4]
	f_values = [RechercheExhaustive, AlgoProgDyn, AlgoGlouton]
	S_values = generateSvalues()
	k_values = [2, 4, 6, 8, 10]
	print("S\tk\tDP\t\t\tGA")
	for d in d_values:
		for k in k_values:
			V = generateV(d, k)
			contd = [True]*3
			for S in S_values:
				line = f"{S}\t{k}"
				for i in range(len(f_values)):
					time = None
					if contd[i]:
						time = testFunction(f[i], k, V, S)
					line += f"\t{time}"
					if time >= 60:
						contd[i] = False
				print(line)
			

