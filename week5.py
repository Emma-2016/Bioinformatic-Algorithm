#CHALLENGE: Solve the De Bruijn Graph from a String Problem.
#Input: An integer k and a string Text.
#Output: DeBruijnk(Text), in the form of an adjacency list

line = 'AAGATTCTCTAAGA'
k = 4
kmers = []
for i in range(len(line)-k+1):
    kmer = line[i:i+k]
    prefix = kmer[:-1]
    suffix = kmer[1:]                   
    item = [prefix, suffix]
    kmers.append(item)

while len(kmers):
    suffix = []
    toDelete = []
    kmerNow = kmers.pop()
    kmerNowPrefix = kmerNow[0]
    kmerNowSuffix = kmerNow[1]
    suffix.append(kmerNowSuffix)

    for j in range(len(kmers)):
        if kmerNowPrefix == kmers[j][0]:
            suffix.append(kmers[j][1])
            toDelete.append(j)
    suffixWords = ",".join(suffix)
    print kmerNowPrefix,"->",suffixWords
    for k in toDelete:
        del kmers[k]
