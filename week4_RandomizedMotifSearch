import random
def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        profile = ProfileWithPseudocounts(M)
        M = Motifs(Dna, profile, k)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs

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

def Motifs(Dna, profile, k):
    motifs = []
    t = len(Dna)
    for i in range(t):
        motif = ProfileMostProbablePattern(Dna[i], k, profile)
        motifs.append(motif)
    return motifs

def ProfileMostProbablePattern(Text, k, profile):
    mostProbablePattern = ''
    n = len(Text)
    m = 0
    for i in range(n-k+1):
        text = Text[i:i+k]
        p = Pr(text, profile)
        if p > m:
            m = p
            mostProbablePattern = text
    return mostProbablePattern

def Pr(Text, profile):
    p = 1
    n = len(Text)
    for i in range(n):
        symbol = Text[i]
        p = p*profile[symbol][i]
    return p

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

Dna = ['GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC', 'CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG', 'ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC', 'GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC', 'GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG', 'CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA', 'GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA', 'GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG', 'GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG', 'TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC']
t = 10
k = 15
N = 100

# Call RandomizedMotifSearch(Dna, k, t) N times, storing the best-scoring set of motifs
# resulting from this algorithm in a variable called BestMotifs
def RepeatedRandomizedMotifSearch(Dna, k, t, N):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(N):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrentScore = Score(Motifs)
        if CurrentScore < BestScore:
            BestScore = CurrentScore
            BestMotifs = Motifs
    return BestMotifs

BestMotifs = (RepeatedRandomizedMotifSearch(Dna, k, t, N))
print(BestMotifs)
print(Score(BestMotifs))
