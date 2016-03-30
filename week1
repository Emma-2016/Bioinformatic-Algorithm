# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(text, k):
    count = {}
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        count[i] = PatternCount(pattern, text)
    return count

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequenPatternsNotDuplicates = remove_duplicate(FrequentPatterns)
    return FrequenPatternsNotDuplicates
def remove_duplicate(x):
    y = x
    L = []
    d = {}
    for i in y:
        d[i] = 0
    for i in d:
        L.append(i)
    return L

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = ''
    L = list(Pattern)
    while (len(L)):
        revComp = revComp + complement(L.pop())
    return revComp

# Input:  A character Nucleotide
# Output: The complement of Nucleotide
# Together with ReverseComplement function, we can produce reverse complement of DNA string
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    if (Nucleotide == "A"):
        comp = "T"
    if (Nucleotide == "T"):
        comp = "A"   
    if (Nucleotide == "C"):
        comp = "G"
    if (Nucleotide == "G"):
        comp = "C"    
    return comp

# Input: Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions
