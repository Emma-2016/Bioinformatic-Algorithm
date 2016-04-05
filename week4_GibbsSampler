import random

def GibbsSampler(Dna, k, t, N): 
  M = RandomMotifs(Dna, k, t)
  BestMotifs = M 
  for j in range(N):
      i = random.randint(1, t-1)
      del M[i]
      profile = ProfileWithPseudocounts(M)
      newMotif = ProfileGeneratedString(Dna[i], profile, k)
      M.insert(i, newMotif)
      if Score(M) < Score(BestMotifs):
        BestMotifs = M 
  return BestMotifs

def Pr(Text, profile):
    p = 1
    n = len(Text)
    for i in range(n):
        symbol = Text[i]
        p = p*profile[symbol][i]
    return p
    
def Normalized(Probabilities):
    normalized = {}
    sumAll = sum(Probabilities.values())
    for i in Probabilities:
        normalized[i] = Probabilities[i] / sumAll
    return normalized

def WeightedDie(Probabilities):
    kmer = ''
    newProbabilities = {}
    previous = 0 
    for i in Probabilities:
        v = Probabilities[i] + previous
        newProbabilities[i] = []
        newProbabilities[i].append(previous)
        newProbabilities[i].append(v)
        previous = v
    p = random.uniform(0, 1)
    for i in newProbabilities:
        if p > newProbabilities[i][0] and p <=newProbabilities[i][1]:
            kmer = i
    return kmer

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0, n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalized(probabilities)
    return WeightedDie(probabilities)

def RandomMotifs(Dna, k, t):
    motifs = []
    n = len(Dna[0])
    for i in range(t):
        num = random.randint(0, n-k)
        motifs.append(Dna[i][num:num+k])
    return motifs

def ProfileWithPseudocounts(motifs):
    t = len(motifs)
    t = t + 4.0
    k = len(motifs[0])
    profile = {}
    count = CountWithPseudocounts(motifs)
    for i in count:
        profile[i] = []
        for j in range(k):
            num = count[i][j] / t
            profile[i].append(num)
    return profile

def CountWithPseudocounts(M):
    count = {}
    t = len(M)
    k = len(M[0])
    for i in 'AGCT':
        count[i] = []
        for j in range(k):
            count[i].append(1)
    for i in range(t):
        for j in range(k):
            symbol = M[i][j]
            count[symbol][j] += 1
    return count

def Score(M):
    d = 0
    consensus = Consensus(M)
    t = len(M)
    for i in range(t):
        d += HammingDistance(consensus, M[i])
    return d

def Consensus(M):
    consensus = ''
    count = CountWithPseudocounts(M)
    k = len(M[0])
    m = 0
    item = ''
    for j in range(k):
        for i in 'AGCT':
            if count[i][j] > m:
                m = count[i][j]
                item = i
        consensus = consensus + item
    return consensus

def HammingDistance(consensus, patternNow):
    d = 0
    n = len(consensus)
    for i in range(n):
        if consensus[i] == patternNow[i]:
            continue
        else:
            d += 1
    return d

def RepeatedGibbsSampler(Dna, k, t, N):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(20):
        Motifs = GibbsSampler(Dna, k, t, N)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs
Dna = ['GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC', 'CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG', 'ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC', 'GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC', 'GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG', 'CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA', 'GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA', 'GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG', 'GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG', 'TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC']
t = 10
k = 15
N =100
BestMotifs = RepeatedGibbsSampler(Dna, k, t, N)
print(BestMotifs)
print(Score(BestMotifs))
