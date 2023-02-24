import generateCoordinate as gc
import bruteForce as bf

def mainBF():
    n = int(input("n: "))
    r = int(input("r: "))
    arrayCoordinate = gc.generateCoordinate(n,r)
    tempi,tempj = bf.closestPair(arrayCoordinate)
    gc.printArrayCoordinate(arrayCoordinate)
    print("Closest Pair: ",end="")
    gc.printCoordinate(arrayCoordinate[tempi])
    print(" ",end="")
    gc.printCoordinate(arrayCoordinate[tempj])

mainBF()