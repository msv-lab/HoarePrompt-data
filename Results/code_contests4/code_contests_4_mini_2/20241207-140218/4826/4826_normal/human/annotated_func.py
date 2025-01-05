#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000, and a is a list of n distinct integers where each integer ai satisfies -1,000,000,000 ≤ ai ≤ 1,000,000,000.
def func():
    cities = int(sys.stdin.readline())
    coordinates = map(int, sys.stdin.readline().split())
    coordinates.sort()
    dist = 2 * 10 ** 9
    count = 0
    for (index, x) in enumerate(coordinates):
        if index < len(coordinates) - 1:
            temp_dist = coordinates[index + 1] - x
            if temp_dist < dist:
                dist = temp_dist
                count = 1
            elif temp_dist == dist:
                count += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 200,000; `a` is a list of `n` distinct integers; `cities` is an input integer; `coordinates` is a sorted iterable of integers with at least 2 integers; `dist` is the minimum distance between any two consecutive integers in `coordinates`; `count` is the count of pairs of consecutive integers in `coordinates` that have the distance equal to `dist`.
    print(str(dist) + ' ' + str(count))
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 200,000) and a list of `n` distinct integers. It calculates the minimum distance between any two consecutive integers in the sorted list of coordinates and counts how many pairs of consecutive integers have that minimum distance. The function then prints the minimum distance and the count of such pairs.

