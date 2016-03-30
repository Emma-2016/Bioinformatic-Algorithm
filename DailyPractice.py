#input: A DNA string s of length at most 1000 nt.
#output: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
s = 'AACGATGGCGTATT'
countA = s.upper().count('A')
countG = s.upper().count('G')
countC = s.upper().count('C')
countT = s.upper().count('T')
print "%d %d %d %d" % (coutnA, countG, countC, countT)

#input: A DNA string t having length at most 1000 nt.
#output: The transcribed RNA string of t.
from string import maketrans
t = 'AACGATGGCGTATT'
inStr = 'tT'
outStr = 'uU'
tranStr = maketrans(inStr, outStr)
print t.translate(tranStr)

#input: A DNA string s of length at most 1000 bp.
#output: The reverse complement sc of s.
from string import maketrans
inStr = 'agctAGCT'
outStr = 'tcgaTCGA'
tranStr = maketrans(inStr, outStr)
s = 'AAAACCCGGT'
print s[::-1].translate(tranStr)

#input: Positive integers n<=40 and k<=5.
#output: The total number of rabbit pairs that will be present after nn months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).
#this in fact is to generate a fibonacci sequence with special increment. While searching for solution, key word 'yield' is introduced. Besides, I came across iterable object.
def fab(n, k):  #where n is generation and k is how many rabit pair were produced each generation;
    generation, a, b = 0, 0, 1
    while generation < n:
        yield b 
        a, b = b, a*k+b
        generation += 1
for i in fab(33,5):
    print i
