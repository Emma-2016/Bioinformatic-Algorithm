#Input: Integers k and d followed by a collection of paired k-mers PairedReads.
#Output: A string Text with (k, d)-mer composition equal to PairedReads.

import sys
sys.setrecursionlimit(1000000)
def StringSpelledByGappedPatterns(kmers, k, d):
    firstKmers = []
    secondKmers = []
    for i in kmers:
        first, second = i.split('|')
        firstKmers.append(first)
        secondKmers.append(second)
    firstPattern = StringReconstruction(firstKmers)
    secondPattern = StringReconstruction(secondKmers)

    for i in range((k+d), len(firstPattern)):
        if firstPattern[i] != secondPattern[i-k-d]:
            return "There is no string spelled by the gapped patterns"
    return firstPattern + secondPattern[-d-k:]

def StringReconstruction(kmers):
    outputString = ''
    EulerPath = EulerianPath(kmers)
    outputString = GenomePath(EulerPath)
    return outputString

def kmersPatterns(kmers):
    output = {}
    prefixs = []
    for i in kmers:
        prefixs.append(i[:-1])
    prefixs = set(prefixs)
    for j in prefixs:
        suffixs = []
        for k in kmers:
            if j == k[:-1]:
                suffixs.append(k[1:])
        suffixs.sort()
        output[j] = suffixs
    return output

def kmersPatternsBackwards(kmers):
    output = {}
    suffixs = []
    for i in kmers:
        suffixs.append(i[1:])
    suffixs = set(suffixs)
    for j in suffixs:
        prefixs = []
        for k in kmers:
            if j == k[1:]:
                prefixs.append(k[:-1])
        output[j] = prefixs
    return output

def EulerianPath(kmers):
    graph = kmersPatterns(kmers)
    graphBackwards = kmersPatternsBackwards(kmers)
    graphValues = []
    graphNodes = []
    for i in graph:
        #print i, ' -> ', graph[i]
        graphValues = graphValues + graph[i]
        graphNodes.append(i)
        graphNodes = graphNodes + graph[i]

    outNode = ''
    inNode = ''
    outNodeList = []
    graphNodes = set(graphNodes)
    for j in graphNodes:
        if j not in graph:
            graph[j] = []
        outDegree = len(graph[j])
        inDegree = graphValues.count(j)
        if outDegree > inDegree:
            inNode = j
        elif outDegree < inDegree:
            outNode = j
        else:
            pass
    if outNode and inNode:
        graph[outNode].append(inNode)
        outNodeList.append(outNode)
        a = traceOutNode(outNode, graph, outNodeList) 
    else:
        inNode = graph.keys()[0]

    circuit = []
    circuit = findCircuit(inNode, graph, circuit, outNodeList)
    circuit.reverse()
    if outNode:
        circuit.pop()
    return circuit

def findCircuit(i, graph, circuit, outNodeList):
    if len(graph[i]) == 0:
        circuit.append(i)
    else:
        while len(graph[i]):
            #position = random.randint(0, len(graph[i])-1)
            j = graph[i][0]
            #if position == len(graph[i])-1:
                #position -= 1
            #else:
                #position += 1
            for outNode in outNodeList:
                if outNode in graph[j] and len(graph[i]) > 1:
                    j = graph[i][1]
            graph[i].remove(j)
            findCircuit(j, graph, circuit, outNodeList)
        circuit.append(i)
    return circuit

def traceOutNode(outNode, graphBackwards, outNodeList):
    for i in graphBackwards:
        if outNode in graphBackwards[i]:
            if len(graphBackwards[i]) > 1:
                #print 'outNode end:', outNode
                return outNodeList
            else:
                outNode = i
                outNodeList.append(i)
                traceOutNode(outNode, graphBackwards, outNodeList)
                return outNodeList

def GenomePath(EulerPath):
    Text = ''
    Text = EulerPath[0]
    for i in EulerPath[1:]:
        Text = Text + i[-1]
    return Text

input =''''''
lines = input.splitlines()
k, d = lines[0].split()
kmers = lines[1:]
print StringSpelledByGappedPatterns(kmers, int(k), int(d))
