# Solve the Squared Error Distortion Problem.
# Input: Integers k and m, followed by a set of centers Centers and a set of points Data.
# Output: The squared error distortion Distortion(Data, Centers).

def SquaredErrorDistortion(k, m, centers, points):
    squaredErrorDistortion = 0
    disList = []
    for i in points:
        minDis = float('inf')
        for j in centers:
            dis = float(calDis(i, j, m))
            if dis < minDis:
                minDis = dis
                belongTo = j
        minDis = minDis ** 2
        disList.append(minDis)
    sum = 0
    for D in disList:
        sum += D
    squaredErrorDistortion = sum / len(disList)
    return squaredErrorDistortion

def calDis(point, center, m):
    dis = 0
    sum = 0
    n = 0
    while n < m:
        sum += (point[n] - center[n]) ** 2
        n += 1
    dis += sum ** 0.5
    return dis

centersInput = '''2 2
2.31 4.55
5.96 9.08'''
pointsInput = '''3.42 6.03
6.23 8.25
4.76 1.64
4.47 4.33
3.95 7.61
8.93 2.97
9.74 4.03
1.73 1.28
9.72 5.01
7.27 3.77'''
centersLines = centersInput.splitlines()
k, m = centersLines[0].split()
k = int(k)
m = int(m)
centers = centersLines[1:]
for i in range(k):
    centerPoints = centers[i].split()
    for j in range(m):
        centerPoints[j] = float(centerPoints[j])
    centers[i] = centerPoints

points = pointsInput.splitlines()
for i in range(len(points)):
    coordinates = points[i].split()
    for j in range(m):
        coordinates[j] = float(coordinates[j])
    points[i] = coordinates
    
D = SquaredErrorDistortion(k, m, centers, points)
print '%.3f' % D
