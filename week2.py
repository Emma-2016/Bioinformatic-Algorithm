# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
# that is to count the symbol numbers in certain DNA string
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[:(n//2)] #the genome is circus
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array
#function created last week
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
# improved version of SymbolArray
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[:n//2]
    array[0] = PatternCount(symbol, Genome[:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i] == symbol:
            array[i] -= 1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] += 1
    return array

# Input:  A String Genome
# Output: Skew(Genome)
# Calculate the GC variation change
def Skew(Genome):
    skew = {}
    n = len(Genome)
    skew[0] = 0
    for i in range(1, n+1):
        skew[i] = skew[i-1]
        if Genome[i-1] == "G":
            skew[i] += 1
        elif Genome[i-1] == "C":
            skew[i] -= 1
        else: continue
    return skew

# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = []
    skew = Skew(Genome)
    minial = min(skew.values())
    for i in range (1,len(skew)):
        if skew[i] == minial:
            positions.append(i)
    return positions

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    count = 0
    lengthq = len(q)
    lengthp = len(p)
    if lengthq == lengthp:
        for i in range(lengthq):
            if q[i] == p[i]: continue
            else:
                count += 1
        return count
    else:
        return 0

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(len(Text)-len(Pattern)+1):
        PatternNow = Text[i:i+len(Pattern)]
        dis = HammingDistance(Pattern, PatternNow)
        if dis <= d:
            positions.append(i)
    return positions
