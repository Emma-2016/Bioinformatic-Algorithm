# Input:  A set of kmers Motifs
# Output: Count(Motifs)
#count = {'A': [1, 2, 1, 0, 0, 2], 
          'C': [2, 1, 4, 2, 0, 0], 
          'G': [1, 1, 0, 2, 1, 1], 
          'T': [1, 1, 0, 1, 4, 2]}
def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in 'AGCT':
        count[symbol] = [] #make a mistake here.
        for i in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
    
# Input:  A list of kmers Motifs, same as the input of Count
# Output: the profile matrix of Motifs, as a dictionary of lists
profile = {'A': [0.2, 0.4, 0.2, 0.0, 0.0, 0.4], 
          'C': [0.4, 0.2, 0.8, 0.4, 0.0, 0.0], 
          'G': [0.2, 0.2, 0.0, 0.4, 0.2, 0.2], 
          'T': [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]}
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = Count(Motifs)
    for i in count:
        profile[i] = []
        for j in range(k):
            num = (count[i][j])/t
            profile[i].append(num)
    return profile

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs
# consensus is the best kmer for each position, best means the highest probability
def Consensus(Motifs):
    k = len(Motifs[0])
    consensus = ''
    count = Count(Motifs)
    for i in range(k):
        m = 0
        for j in 'AGCT':
            if count[j][i] > m:     #nice! no bother to use dict key-value pair
                m = count[j][i]
                frequentSymbol = j
        consensus += frequentSymbol
    return consensus

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers
# That is calculate hamming distance for each two kmer among the motifs
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

# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
# That is calculate the probabilty for any input string
def Pr(Text, Profile):
    p = 1
    n = len(Text)
    for i in range(n):
        symbol = Text[i]
        p = p * Profile[symbol][i]
    return p

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
# That is find out the most probable kmer hinding inside the input text
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

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
# find out the motifs hinding among several DNA strings
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
