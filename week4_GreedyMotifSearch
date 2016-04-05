def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    t = len(Dna)
    n = len(Dna[0])
    for i in range(t):
        BestMotifs.append(Dna[i][0:k])

    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def CountWithPseudocounts(Motifs):
    count = {}
    t = len(Motifs)
    k = len(Motifs[0])
    for i in 'AGCT':
            count[i] = []
            for j in range(k):  #length of each element of motifs
                count[i].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    t = t + 4.0
    k = len(Motifs[0])
    profile = {}
    count = CountWithPseudocounts(Motifs)
    for i in 'AGCT':
        profile[i] = []
    for i in count:
        for j in range(k):
            num = (count[i][j])/t
            profile[i].append(num)
    return profile

def Consensus(Motifs):
    k = len(Motifs[0])
    consensus = ''
    count = CountWithPseudocounts(Motifs)
    for i in range(k):
        m = 0
        for j in 'AGCT':
            if count[j][i] > m:     #nice! no bother to use dict key-value pair
                m = count[j][i]
                frequentSymbol = j
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    consensus = Consensus(Motifs)
    t = len(Motifs)
    d = 0
    for i in range(t):
        PatternNow = ''.join(Motifs[i])
        d += HammingDistance(PatternNow, consensus)
    return d

def HammingDistance(Pattern, PatternNow):
    count = 0
    length1 = len(Pattern)
    length2 = len(PatternNow)
    if length1 == length2:
        for i in range(length1):
            if Pattern[i] == PatternNow[i]:
                continue
            else:
                count += 1
        return count
    else:
        return 0
def Pr(Text, Profile):
    p = 1
    n = len(Text)
    for i in range(n):
        symbol = Text[i]
        p = p * Profile[symbol][i]
    return p

def ProfileMostProbablePattern(Text, k, Profile):
    MostProbablePattern = ''
    n = len(Text)
    m = -1
    for i in range(n-k+1):
        pattern = Text[i:i+k]
        pro = Pr(pattern, Profile)
        if pro > m:
                MostProbablePattern = pattern
                m = pro
    return MostProbablePattern

Dna = ['GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC','CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG','ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC','GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC','GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG','CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA','GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA','GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG','GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG','TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC']
t = 10
k = 15

# Call GreedyMotifSearchWithPseudocounts(Dna, k, t) and store the output in a variable called Motifs
Motifs = GreedyMotifSearchWithPseudocounts(Dna, k, t)
print(Motifs)
print(Score(Motifs))
