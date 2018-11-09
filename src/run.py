from tools import readFile
from dynamic_programming import AlgoProgDyn
from exhaustive_search import RechercheExhaustive

fn = input("Enter the filename: ")
S, k, V = readFile(fn)
print(f"S={S}")
print(f"k={k}")
print(f"V={V}")
AlgoProgDyn(k, V, S)
RechercheExhaustive(k, V, S)

