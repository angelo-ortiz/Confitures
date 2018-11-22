from tools import readFile
from exhaustive_search import RechercheExhaustive
from dynamic_programming import AlgoProgDyn
from greedy_algorithm import AlgoGlouton

fn = input("Enter the filename: ")
re = input("Would you like to execute the exhaustive search algorithm (y/n): ")
re.lower()
S, k, V = readFile(fn)
print(f"S={S}")
print(f"k={k}")
print(f"V={V}")
AlgoProgDyn(k, V, S)
AlgoGlouton(k, V, S)
if re == "y" or re == "yes":
	RechercheExhaustive(k, V, S)

