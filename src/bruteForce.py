from utilities import calculateDistance

def closestPair(arrayCoordinate):
    closest = 1000000
    tempi = -1
    tempj = -1
    eucledianCount = 0
    for i in range(len(arrayCoordinate)-1):
        for j in range(i+1,len(arrayCoordinate)):
            eucledianCount+=1
            temp = calculateDistance(arrayCoordinate[i],arrayCoordinate[j],len(arrayCoordinate[i]))
            if temp<closest:
                closest = temp
                tempi = i
                tempj = j
    return tempi,tempj,eucledianCount