#input: a matrix
#output: converse the input matrix

M = [ [1,2,3,4], ['a','b','c','d'], ['A','B','C'] ]
max = 0
for i in M:
    if len(i) > max:
        max = len(i)

for j in range(max):
    for i in range(len(M)):
        if j < (len(M[i])):
            print M[i][j],
    j += 1
    print

#output item according to frequency
import random
data = {"A":2, "B":2, "C":4, "D":6, "E": 11}
def list_method():
    all_data = []
    for k, v in data.items():
        for i in range(v):
            all_data.append(k)
    n = random.randint(0,len(all_data)-1)
    return all_data[n]

itemA = 0
itemB = 0
itemC = 0
itemD = 0
itemE = 0
n = 0
while n < 1000:
    item = list_method()
    if item == 'A': itemA += 1
    if item == 'B': itemB += 1
    if item == 'C': itemC += 1
    if item == 'D': itemD += 1
    if item == 'E': itemE += 1
    n += 1
print 'A:', itemA, 'B:', itemB, 'C:', itemC, 'D:', itemD, 'E:', itemE
