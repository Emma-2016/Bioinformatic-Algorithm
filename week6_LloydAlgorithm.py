#Input: Integers k and m followed by a set of points Data in m-dimensional space.
#Output: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and Centers, where the first k points from Data are selected as the first k centers.

import random 
def LloydAlgorithm(k, m, points):
    newCenterPoints = []

    centersNumRange = range(len(points))
    centerNum = random.sample(centersNumRange, k) # different start centers lead to different output. Don't know how to fix yet.

    centers = []
    for i in centerNum:
        centers.append(points[i])
    print centers

    cluster = centerToCluster(centers, points, m)
    newCenterPoints = clusterToCenter(cluster)

    while len(newCenterPoints) and (newCenterPoints != centers):
        cluster = centerToCluster(newCenterPoints, points, m)
        centers = newCenterPoints
        newCenterPoints = clusterToCenter(cluster)
    else:
        return newCenterPoints

def centerToCluster(centers, points, m):
    cluster = {}

    for i in centers:
        joinList = []
        for j in range(m):
            joinList.append(str(i[j]))
        clusterK = ' '.join(joinList)
        cluster[clusterK] = []
        cluster[clusterK].append(i)

    for p in points:
        minDis = float('inf')
        belongTo = []
        for c in centers:
            dis = calDis(p, c, m)
            if dis < minDis:
                minDis = dis
                belongTo = c
        joinList = []
        for e in belongTo:
            joinList.append(str(e))
        clusterK = ' '.join(joinList)
        cluster[clusterK].append(p)

    return cluster

def clusterToCenter(cluster):
    gravityList = []
    for i in cluster:
        gravity = calGravity(cluster[i])
        gravityList.append(gravity)
    return gravityList

def calGravity(points):
    gravity = []
    pointNum = len(points)
    m = len(points[0])
    for i in range(m):
        gravity.append(0)
        sum = 0
        for  j in range(pointNum):
            sum += points[j][i]
        gravity[i] = sum / pointNum
    return gravity

def calDis(i, j, m):
    dis = 0
    sum = 0
    n = 0
    while n < m:
        sum += (i[n] - j[n]) ** 2
        n += 1
    dis = sum ** 0.5
    return dis

input = '''2 2
1.3 1.1
1.3 0.2
0.6 2.8
3.0 3.2
1.2 0.7
1.4 1.6
1.2 1.0
1.2 1.1
0.6 1.5
1.8 2.6
1.2 1.3
1.2 1.0
0.0 1.9'''

lines = input.splitlines()
k, m = lines[0].split()
k = int(k)
m = int(m)
points = []
for i in lines[1:]:
    point = i.split()
    for j in range(m):
        point[j] = float(point[j])
    points.append(point)

centers = LloydAlgorithm(k, m, points)
for i in centers:
    for n in range(m):
        print '%.3f' % i[n],
    print
