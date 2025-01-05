#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2*10^5. The list of city coordinates, a1, a2, ..., an, consists of n pairwise distinct integers where -10^9 <= ai <= 10^9.**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 2*10^5, `cities` is an input integer, `coordinates` contains the city coordinates sorted in ascending order. `dist` is the smallest distance between two consecutive cities, `count` is the number of times this smallest distance occurs.
    print(str(dist) + ' ' + str(count))
#Overall this is what the function does:The function `func` reads an integer `cities` from the standard input and a list of integers `coordinates` representing city coordinates. It sorts the coordinates, calculates the smallest distance `dist` between consecutive cities, and counts how many times this smallest distance occurs. Finally, it prints the smallest distance and the count. The function does not explicitly return any value.

