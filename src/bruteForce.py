from utilities import calculateDistance

def closestPair(arrayCoordinate):
    closest = 1000000
    tempi = -1
    tempj = -1
    count = 0
    for i in range(len(arrayCoordinate)-1):
        for j in range(i+1,len(arrayCoordinate)):
            count+=1
            temp = calculateDistance(arrayCoordinate[i],arrayCoordinate[j],len(arrayCoordinate[i]))
            if temp<closest:
                closest = temp
                tempi = i
                tempj = j
    return tempi,tempj