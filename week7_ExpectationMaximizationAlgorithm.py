#Input: Integers k and m, followed by a stiffness parameter β, followed by a set of points
#Data in m-dimensional space.
#Output: A set Centers consisting of k points (centers) resulting from applying the
#expectation maximization algorithm for soft k-means clustering. Select the first k points
#from Data as the first centers for the algorithm and run the algorithm for 100 E-steps
#and 100 M-steps. Results should be accurate up to three decimal places.

def EM(k, m , beta, points):
    e = 2.718281828
    centers = points[:k]

    round = 0
    while round < 100:
        HiddenMatrix = {}
        centerNew = {}
        for i in centers:
            joinList = []
            for j in range(m):
                joinList.append(str(i[j]))
            cK = ' '.join(joinList)
            HiddenMatrix[cK] = []

        for i in points:
            allDis = 0
            Dis = {}
            for j in centers:
                dis, pointStr, centerStr = calDis(i, j, m)
                dis = e ** ((-beta)*dis)
                Dis[centerStr] = []
                Dis[centerStr].append(dis)
                allDis += dis
            for n in Dis:
                dis = sum(Dis[n])
                HiddenMatrix[n].append(dis/allDis)
                centerNew[n] = []

        for n in range(m):
            pm = []
            for p in points:
                pm.append(p[n]) 
            for i in HiddenMatrix:
                pim = [a * b for a, b in zip(HiddenMatrix[i], pm)]
                pim1 = sum(pim)
                pim2 = sum(HiddenMatrix[i])
                centerNew[i].append(pim1 / pim2)

        centers = []
        for i in centerNew:
            centers.append(centerNew[i])

        round += 1

    return centers         

def calDis(i, j, m):
    sum = 0
    dis = 0
    joinListi = []
    joinListj = []
    for n in range(m):
        joinListi.append(str(i[n]))
        joinListj.append(str(j[n]))
        sum += (i[n] - j[n]) ** 2
    dis += sum ** 0.5
    istr = ' '.join(joinListi)
    jstr = ' '.join(joinListj)
    return dis, istr, jstr

input = '''2 2
2.7
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
beta = lines[1]
k = int(k)
m = int(m)
beta = float(beta)
points = []
for i in lines[2:]:
    point = i.split()
    for j in range(len(point)):
        point[j] = float(point[j])
    points.append(point)
newCenter = EM(k, m , beta, points)
for i in newCenter:
    for j in range(m):
        print '%.3f' % i[j],
    print
