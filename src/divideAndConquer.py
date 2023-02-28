from utilities import quickSort, calculateDistance

def closestStrip(strip: list[list[float]], size: int, delta: float, count: int) -> float:
    """Find the smallest distance in the strip array.
    :param strip: Strip array solved in a two dimensional plane
    :param size: Number of elements in the array
    :param delta: Delta value
    """

    point_one = strip[0]
    point_two = strip[0]
    min_dist = delta

    strip = quickSort(strip, 0, len(strip)-1, 1)

    for i in range(size):
        for j in range(i+1, size):
            if (strip[j][1] - strip[i][1] >= min_dist):
                break
            count += 1
            if (calculateDistance(strip[i], strip[j], len(strip[i])) < min_dist):
                point_one = strip[i]
                point_two = strip[j]
                min_dist = calculateDistance(strip[i], strip[j], len(strip[i]))

    if (min_dist == delta):
        return point_one, point_two, float("inf"), count 
    else:
        return point_one, point_two, min_dist, count

def divideAndConquer(Array: list[list[float]], size: int, dimension: int, count: int) -> (list[float], list[float], float):
    """Solve the closest pair problem with divide and conquer algorithm, returns the index of closest points. Array should be sorted by the last dimension beforehand.
    :param Array: Array of points
    :param size: Number of elements in the array
    :dimension: Number of dimension in the points
    :return: (list[float], list[float], float)
    """

    # Divide
    if (size == 1):
        return (Array[0], Array[0], float("inf"), count)
    if (size == 2):
        return (Array[0], Array[1], calculateDistance(Array[0], Array[1], len(Array[0])), count+1)

    mid = size // 2
    mid_point = Array[mid]

    left_first_point, left_second_point, left_delta, count = divideAndConquer(Array[:mid], mid, dimension, count)
    right_first_point, right_second_point, right_delta, count = divideAndConquer(Array[mid:], size-mid, dimension, count)

    if (left_delta < right_delta):
        first_point = left_first_point
        second_point = left_second_point
        delta = left_delta
    else:
        first_point = right_first_point
        second_point = right_second_point
        delta = right_delta

    strip = []
    for i in range(size):
        if (abs(Array[i][dimension-1] - mid_point[dimension-1]) < delta):
            strip.append(Array[i])

    # Conquer

    # Check if 2nd dimension. If not, then we call dnc for all points in the strip
    if (dimension != 2):
        strip = quickSort(strip, 0, len(strip)-1, dimension-1)

        point_one, point_two, strip_delta, count = divideAndConquer(strip, len(strip), dimension-1, count)

        if (strip_delta < delta):
            return point_one, point_two, strip_delta, count
        else:
            return first_point, second_point, delta, count
        
    else:
        point_one, point_two, strip_delta, count = closestStrip(strip, len(strip), delta, count)
        
        if (strip_delta == float("inf")):
            return first_point, second_point, delta, count
        else:
            return point_one, point_two, strip_delta, count

def solveDivideAndConquer(Array: list[list[float]], size: int, dimension: int) -> (int, int, float, int):
    """Calls the divideAndConquer function to retrieve the values of first_point and second_point, then returns the index of first_point and second_point from the unsorted Array
    :param Array: Array of points
    :param size: Number of elements in the array
    :dimension: Number of dimension in the points
    :return: (int, int, float)
    """
    Array = quickSort(Array, 0, len(Array)-1, dimension)

    first_point, second_point, distance, count = divideAndConquer(Array, size, dimension, 0)

    first_index = -1
    second_index = -1

    i = 0
    while (i < size):
        if (Array[i] == first_point):
            first_index = i
        if (Array[i] == second_point):
            second_index = i
        i += 1

    return first_index, second_index, distance, count
