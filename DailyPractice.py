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
