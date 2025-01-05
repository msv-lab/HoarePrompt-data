#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2*10^5. All ai are integers such that -10^9 <= ai <= 10^9 and are pairwise distinct.**
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
        
    #State of the program after the  for loop has been executed: `cities` is an integer input by the user, `coordinates` is a map object with at least one element. `dist` is the minimum difference between consecutive elements in the `coordinates` map object. `count` is the number of times the minimum difference occurs.
    print(str(dist) + ' ' + str(count))
#Overall this is what the function does:The function `func` reads an integer `cities` from the standard input, followed by a list of coordinates. It then sorts the coordinates, calculates the minimum distance between consecutive elements, and counts the occurrences of that minimum distance. Finally, it prints the minimum distance and the count of occurrences. The function does not explicitly return any value.

