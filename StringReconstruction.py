#Input: A list of k-mers Patterns.
#Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

import sys
sys.setrecursionlimit(1000000)

def StringReconstruction(kmers):
    outputString = ''
    EulerPath = EulerianPath(kmers)
    outputString = GenomePath(EulerPath)
    return outputString

def EulerianPath(kmers):
    import re
    graph = kmersPatterns(kmers)
    graphValues = []
    graphNodes = []
    for i in graph:
        graphValues = graphValues + graph[i]
        graphNodes.append(i)
        graphNodes = graphNodes + graph[i]
    outNode = ''
    inNode = ''
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
    else:
        inNode = graph.keys()[0]
    circuit = []
    circuit = findCircuit(inNode, graph, circuit, outNode)
    circuit.reverse()
    if outNode:
        circuit.pop()
    return circuit
#['GGC', 'GCT', 'CTT', 'TTA', 'TAC', 'ACC', 'CCA']

def findCircuit(i, graph, circuit, outNode):
    if len(graph[i]) == 0:
        circuit.append(i)
    else:
        while len(graph[i]):
            j = graph[i][0]
            if outNode in graph[j] and len(graph[i]) > 1:
                j = graph[i][1]
            else:
                if len(graph[i]) > 1 and j == outNode:
                    j = graph[i][1]
            graph[i].remove(j)
            findCircuit(j, graph, circuit, outNode)
        circuit.append(i)
    return circuit

def kmersPatterns(kmers):
    output = {}
    prefixs = []
    for i in kmers:
        prefixs.append(i[:-1])
    prefixs = set(prefixs)
    for j in prefixs:
        output[j] = []
        suffixs = []
        for k in kmers:
            if j == k[:-1]:
                suffixs.append(k[1:])
        suffixs.sort()
        output[j] = suffixs
    return output
#['CTT->TTA', 'ACC->CCA', 'GCT->CTT', 'GGC->GCT', 'TAC->ACC', 'TTA->TAC']

def GenomePath(EulerPath):
    Text = ''
    Text = EulerPath[0]
    for i in EulerPath[1:]:
        Text = Text + i[-1]
    return Text

kmer = '' #input kmers
kmers = kmer.splitlines()
print StringReconstruction(kmers)
