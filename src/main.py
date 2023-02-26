from generateCoordinate import generateCoordinate, printCoordinate, printArrayCoordinate
from displayCoordinate import displayCoordinate 
from bruteForce import closestPair
from divideAndConquer import solveDivideAndConquer
from utilities import calculateDistance
from time import time

def main():
    """Main function"""

    n = int(input("Enter amount of points (n)    : "))
    R = int(input("Enter dimension of points (R) : "))

    Array = generateCoordinate(n, R)

    choice = input("1) Brute Force\n2) Divide and Conquer\nChoose Algorithm    : ")

    start = time() * 1000

    if (choice == 0):
        first, second = closestPair(Array)
        distance = calculateDistance(Array[first], Array[second], R)
    else:
        first, second, distance = solveDivideAndConquer(Array, n, R)

    finish = time() * 1000

    time_taken = finish - start

    print("Closest Pair: ", end = '')
    printCoordinate(Array[first])
    printCoordinate(Array[second])
    print()

    print(f'Distance: {distance}')

    print("Executed Time: ", time_taken, "ms")

    if (R == 3):
        displayCoordinate(Array, Array[first], Array[second])

if (__name__ == '__main__'):
    main()
