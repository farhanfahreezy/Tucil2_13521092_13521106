import generateCoordinate as gc

def distance(c1,c2):
    return ((c2[0]-c1[0])**2+(c2[1]-c1[1])**2+(c2[2]-c1[2])**2)**(0.5)

def closestPair(arrayCoordinate):
    closest = 1000000
    tempi = -1
    tempj = -1
    count = 0
    for i in range(len(arrayCoordinate)-1):
        for j in range(i+1,len(arrayCoordinate)):
            count+=1
            temp = distance(arrayCoordinate[i],arrayCoordinate[j])
            if temp<closest:
                closest = temp
                tempi = i
                tempj = j
    return tempi,tempj