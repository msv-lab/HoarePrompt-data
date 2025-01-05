#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200000, and a is a list of n distinct integers where each integer is in the range of -10^9 to 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 200000, `cities` is an input integer, `coordinates` is a sorted list with at least 2 elements, `dist` is the smallest distance between consecutive elements in `coordinates`, `count` is the number of times this minimum distance occurs.
    print(str(dist) + ' ' + str(count))
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 200000) and reads a list of `n` distinct integers representing coordinates. It calculates the smallest distance between any two consecutive coordinates and counts how many times this minimum distance occurs. The function then prints the smallest distance and the count of its occurrences.

