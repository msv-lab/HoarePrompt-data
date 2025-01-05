#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000, and a is a list of n distinct integers where each integer ai satisfies -10^9 ≤ ai ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 200,000; `coordinates` is a list of length at least `n`; `dist` is the minimum distance between consecutive elements in `coordinates`; `count` is the number of times `dist` occurs among the distances between consecutive elements in `coordinates`.
    print(str(dist) + ' ' + str(count))
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 200,000) and reads a list of `n` distinct integers representing coordinates. It calculates the minimum distance between consecutive coordinates after sorting them and counts how many times this minimum distance occurs. Finally, it prints the minimum distance and its count. The function does not return any value but instead outputs the results directly.

