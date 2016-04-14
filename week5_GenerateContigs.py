#Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).
#Input: A collection of k-mers Patterns. 
#Output: All contigs in DeBruijn(Patterns).

import re

def MaximalNonBranchingPaths(kmers):
    Paths = []
    graph = {}
    m = re.match(' -> ', kmers[0])
    if m == None: graph = CreateGraph1(kmers)
    else: graph = CreateGraph2(kmers)

    #find oneINoneOUT node and put them into a list
    inNodes = []
    outNodes = []
    oneINoneOUT = []
    for i in graph:
        inNodes.append(i)
        outNodes = outNodes + graph[i]
    nodes = inNodes + outNodes
    nodes = set(nodes)
    for i in nodes:
        if i not in graph:
            graph[i] = []
        inEdge = outNodes.count(i)
        outEdge = len(graph[i])
        if inEdge <= 1 and outEdge <= 1:
            oneINoneOUT.append(i)
    #print oneINoneOUT  #check if the oneINoneOUT set is right or not ['1', '2', '5', '4', '7', '6']

    #go through each node
    graph2 = {}
    toDel = []
    for i in nodes:
        if i not in oneINoneOUT:
            if len(graph[i]) > 0:
                for j in graph[i]:
                    NonBrachingPath = []
                    NonBrachingPath.append(i)
                    NonBrachingPath.append(j)
                    while j in oneINoneOUT:
                        if len(graph[j]) > 0:
                            NonBrachingPath.append(graph[j][0])
                            toDel.append(j)
                            j = graph[j][0]
                        else:
                            break
                    Paths.append(NonBrachingPath)
        else:
            if i in graph and len(graph[i]) > 0: #in case final node whose length is 0
                graph2[i] = graph[i]
    toDel = set(toDel)
    for i in toDel:
        del graph2[i]

    isolatedCycle = FindIsolatedCycle(graph2)
    Paths = Paths + isolatedCycle

    if m == None:
        Paths = ConvertFormat1(Paths)
    else:
        Paths = ConvertFormat2(Paths)

    return Paths

def FindIsolatedCycle(graph):
    isolatedCycle = []

    graphNodes = []
    graphValues = []
    for i in graph:
        graphValues = graphValues + graph[i]
        graphNodes.append(i)
        graphNodes = graphNodes + graph[i]
    outNode = []
    inNode = []
    graphNodes = set(graphNodes)
    for j in graphNodes:
        if j not in graph:
            graph[j] = []
        outDegree = len(graph[j])
        inDegree = graphValues.count(j)
          if outDegree > inDegree:
            inNode.append(j)
        elif outDegree < inDegree:
            del graph[j]
            outNode.append(j)
        else:
            pass
  
    for i in inNode:  #find the path not the cycle
        NonBrachingPath = []
        if len(graph[i]) == 1:
            NonBrachingPath.append(i)
            j = graph[i][0]
            graph.pop(i)
            NonBrachingPath.append(j)
            while j in graph:
                if len(graph[j])== 1:
                    NonBrachingPath.append(graph[j][0])
                    j_ = j
                    j = graph[j][0]
                    del graph[j_]
                else: break
        if len(NonBrachingPath) > 0:
            isolatedCycle.append(NonBrachingPath)

    remainedNodes = graph.keys()
    for i in remainedNodes:
        NonBrachingPath = []
        if (i in graph) and len(graph[i]) == 1:
            NonBrachingPath.append(i)
            j = graph[i][0]
            NonBrachingPath.append(j)
            while j in remainedNodes:
                if len(graph[j]) == 1:
                    j_ = j
                    j = graph[j][0]
                    del graph[j_]
                    if j == i:
                        break
                    else:
                        NonBrachingPath.append(j)
        if len(NonBrachingPath) > 0:
            isolatedCycle.append(NonBrachingPath)
  
    return isolatedCycle

def CreateGraph1(kmers):
  '''In case the input is DNA string, and convert it to prefix and suffix'''
    graph = {}
    prefix = []
    for i in kmers:
        prefix.append(i[:-1])
    for i in set(prefix):
        suffix = []
        for j in kmers:
            if i == j[:-1]:
                suffix.append(j[1:])
        graph[i] = suffix
    return graph

def CreateGraph2(kmers):
    '''In case the input is something like 1 -> 2,4, and convert it to list'''
    graph = {}
    for i in kmers:
        matchObj = re.match('(.*) -> (.*)', i)

        inNode = matchObj.group(1)
        outNode = matchObj.group(2).split(',')
        graph[inNode] = outNode
    return graph

def ConvertFormat1(paths):
    Paths = []
    for i in paths:
        out = i[0]
        for j in i[1:]:
            out = out + j[-1]
        Paths.append(out)
    return Paths

def ConvertFormat2(paths):
    Paths = []
    for i in paths:
        out = ' -> '.join(i)
        Paths.append(out)
    return Paths

input = ''''''  #input could be numbers node or DNA string
kmers = input.splitlines()
path = MaximalNonBranchingPaths(kmers)
for i in path:
    print i
