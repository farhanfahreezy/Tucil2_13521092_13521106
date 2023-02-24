import generateCoordinate as gc
import bruteForce as bf
import displayCoordinate as dc
import time

def mainBF():
    n = int(input("n: "))
    r = int(input("r: "))
    arrayCoordinate = gc.generateCoordinate(n,r)

    start = time.time()*1000
    tempi,tempj = bf.closestPair(arrayCoordinate)
    timetaken = time.time()*1000 - start

    print("Closest Pair: ",end="")
    gc.printCoordinate(arrayCoordinate[tempi])
    print(" ",end="")
    gc.printCoordinate(arrayCoordinate[tempj])
    print()

    print("Executed Time:", timetaken,"ms")

    dc.displayCoordinate(arrayCoordinate,arrayCoordinate[tempi],arrayCoordinate[tempj])

mainBF()