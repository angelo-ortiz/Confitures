# -*- coding: utf-8 -*-
from tools import readFile, validateData, printSolution
from exhaustive_search import RechercheExhaustive
from dynamic_programming import AlgoProgDyn
from greedy_algorithm import AlgoGlouton
import argparse

def printMenu():
	print('=========================== Algorithms\' test ===========================')
	print('1.- Exhaustive search')
	print('2.- Dynamic programming')
	print('3.- Greedy algorithm')
	print('\nPlease enter \'q\' to quit')
	opt = input('Which one would you like to run? ')
	print('========================================================================')
	return opt

ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', required=True, help='path of the instance file')
args = vars(ap.parse_args())
fn = str(args['path'])

S, k, V = readFile(fn)
validateData(S, k, V)

contd = True
while contd:
	opt = printMenu()
	try:
		nopt = int(opt)
		if nopt == 1:
			printSolution('exhaustive search', RechercheExhaustive(k, V, S), V)
		elif nopt == 2:
			printSolution('dynamic programming', AlgoProgDyn(k, V, S), V)
		elif nopt == 3:
			printSolution('greedy', AlgoGlouton(k, V, S), V)
		else:
			print('Please enter a valid option [1-3]')
		print('========================================================================\n')
	except:
		if opt == 'q':
			contd = False
		else:
			print('Please enter \'q\' to quit\n')
