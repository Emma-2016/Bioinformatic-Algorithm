##Farthest First Traversal heuristic, whose pseudocode is shown below
#FarthestFirstTraversal(Data, k) 
# Centers ← the set consisting of a single randomly chosen point from Data
# while |Centers| < k 
#   DataPoint ← the point in Data maximizing d(DataPoint, Centers) 
#   add DataPoint to Centers 
# return Centers 
#Input: Integers k and m followed by a set of points Data in m-dimensional space.
#Output: A set Centers consisting of k points (centers) resulting from applying
#FarthestFirstTraversal(Data, k), where the first point from Data is chosen as the first center to initialize the algorithm.

def FarthestFirstTraversal(k, m, points):
    centers = []
    centers.append(points[0])

    cluster = {}
    joinList = []
    for j in range(m):  #mutable variable can not use as key, so convert it into string;
        joinList.append(str(points[0][j]))  #float type can not join directly, so first convert it into str
    clusterK = ' '.join(joinList)
    cluster[clusterK] = points[1:]

    while len(centers) < k:
        centerNew = clusterCenter(k, m, cluster, centers)
        centers.append(centerNew)
    return centers

def clusterCenter(k, m, cluster, centers):
    centerNew = []
    maxDis = 0
    centerNewStr = ''
    pDic = {}
#Compare all pair distance between points and corresponding centers and keep track which distance is the largest
    for i in centers:
        joinList = []
        for j in range(m):
            joinList.append(str(i[j]))
        clusterK = ' '.join(joinList)
        ownCluster = cluster[clusterK]
        for p in ownCluster:    #calculate distance between each point and its corresponding center
            sum = 0
            dis = 0
            joinList = []
            n = 0
            while n < m:
                joinList.append(str(p[n]))
                sum += (i[n] - p[n])  ** 2
                n += 1
            dis = sum ** 0.5
            pKey = ' '.join(joinList)
            pKey = clusterK + ':' + pKey
            pDic[pKey] = dis    #put all pair distance pair into a hash
            if dis > maxDis:
                maxDis = dis
                centerNewStr = pKey #mark down the largest distance

    newCluster = []
    originalCenter, newCenter = centerNewStr.split(':')
    newCenterPoint = newCenter.split()
    for i in range(len(newCenterPoint)):    #convert the new center back to float type
        newCenterPoint[i] = float(newCenterPoint[i])

    if (len(centers) + 1) < k:  #decide if it is necessary to assign points to the new centers
        clusterNow = cluster[originalCenter]
        for  p in clusterNow:
            sum = 0
            dis = 0
            n = 0
            joinList = []
            while n < m:
                joinList.append(str(p[n]))
                sum += (newCenterPoint[n] - p[n]) ** 2
                n += 1
            dis = sum ** 0.5
            pKey = ' '.join(joinList)
            pKey = originalCenter + ':' + pKey
            if pDic[pKey] > dis:
                newCluster.append(p)
                cluster[originalCenter].remove(p)
        cluster[newCenter] = newCluster
    return newCenterPoint

input ='''3 2
0.0 0.0
5.0 5.0
0.0 5.0
1.0 1.0
2.0 2.0
3.0 3.0
1.0 2.0'''
lines = input.splitlines()
k, m = lines[0].split()
points = []
for i in lines[1:]:
    L = i.split()
    for j in range(len(L)):
        L[j] = float(L[j])
    points.append(L)

centers = FarthestFirstTraversal(int(k), int(m), points)
for i in centers:
    for j in range(len(i)):
        print i[j],
    print
