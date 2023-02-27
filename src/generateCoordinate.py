import random

def generateCoordinate(n,r):
    arrayOfCoordinate = [ [0 for i in range(r)] for j in range(n)]
    for i in range(n):
        for j in range(r):
            arrayOfCoordinate[i][j] = random.uniform(-1000,1000)
    return arrayOfCoordinate

def printCoordinate(coordinate):
    print("(",end="")
    for i in range(len(coordinate)):
        if (i != len(coordinate)-1):
            print(str(coordinate[i])+",",end="")
        else:
            print(coordinate[i],end="")
    print(")",end="")

def printArrayCoordinate(arrayCoordinate):
    for i in range(len(arrayCoordinate)):
        printCoordinate(arrayCoordinate[i])
        print()

# printArrayCoordinate(generateCoordinate(10,3))
        
