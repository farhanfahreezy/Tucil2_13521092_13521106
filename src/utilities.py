import math

def partition(Array: list[list[float]], left: int, right: int, dimension: int) -> (list[list[float]], int):
    """Function to find the partition index
    
    :param Array: Array of points
    :param left: Index of the left-most value
    :param right: Index of the right-most value
    :param dimension: The dimension to be sorted by
    :return: (list[list[float]], int)
    """

    pivot = Array[right][dimension-1]

    i = left-1

    for j in range(left, right):
        if (Array[j][dimension-1] <= pivot):
            i += 1
            Array[i], Array[j] = Array[j], Array[i]

    Array[i+1], Array[right] = Array[right], Array[i+1]

    return (Array, i + 1)

def quickSort(Array: list[list[float]], left: int, right: int, dimension: int) -> list[list[float]]:
    """Function to sort the array A by the value of the d-th dimension

    :param Array: Array of points
    :param left: Index of the left-most value
    :param right: Index of the right-most value
    :param dimension: The dimension to be sorted by (1, 2, 3, ...)
    :return: list[list[float]]
    """

    if (left < right):
        Array, index = partition(Array, left, right, dimension)

        quickSort(Array, left, index-1, dimension)

        quickSort(Array, index+1, right, dimension)

    return Array

def calculateDistance(first_point: list[float], second_point: list[float], size: int) -> float:
    """Calculate the distance between P1 and P2
    
    :param first_point: Coordinate (list) of the first point.
    :param second_point: Coordinate (list) of the second point.
    :param size: Size of first_point and second_point.
    :return: float
    """

    value = 0 
    for i in range(size):
        value += (first_point[i] - second_point[i])**2
    return math.sqrt(value)

def pointToStr(point):
    strPoint = "("
    for i in range(len(point)):
        strPoint+=str(round(point[i],2))
        if(i!=len(point)-1):
            strPoint+=","
    return strPoint+")"

