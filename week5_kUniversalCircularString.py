#Input: An integer k.
#Output: A k-universal circular string.

def kUniversalCircularString(k):
    num = 0
    binnary = []
    for i in range(k):
        num += 2**i
    for j in range(num+1):
        j = bin(j)[2:]
        shortage = k - len(j)
        shortage = '0' * shortage
        biNum = shortage + j
        binnary.append(biNum)
    binString = StringReconstruction(binnary)
    return binString

def StringReconstruction(kmers):
    outputString = ''
    EulerPath = EulerianPath(kmers)
    outputString = GenomePath(EulerPath)
    return outputString

def EulerianPath(kmers):
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

        suffixs = []
        for k in kmers:
            if j == k[:-1]:
                suffixs.append(k[1:])
        suffixs.sort()
        output[j] = suffixs
    return output

def GenomePath(EulerPath):
    Text = ''
    #Text = EulerPath[0]
    for i in EulerPath[:-1]:    #there is a modification here since it is circus
        Text = Text + i[-1]
    return Text

print kUniversalCircularString(9)
