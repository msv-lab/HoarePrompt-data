#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 2 <= n <= 2*10^5.
- ai are integers such that -10^9 <= ai <= 10^9 and all ai are pairwise distinct.
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
        
    #State of the program after the  for loop has been executed: `cities` is an integer value based on user input, `coordinates` is a list of integers sorted in ascending order with at least 1 element. The loop will iterate through all elements of the coordinates list, updating `dist` to the smallest difference between consecutive elements, and `count` to the number of occurrences of that smallest difference. `index`, `x`, and `temp_dist` will have final values based on the last iteration of the loop.
    print(str(dist) + ' ' + str(count))
#Overall this is what the function does:The function `func` reads an integer `cities` from the standard input, followed by a list of integer coordinates. It then sorts the coordinates, calculates the smallest difference between consecutive elements, and counts the occurrences of that smallest difference. Finally, it prints the smallest difference and the count of occurrences. The function does not accept any parameters and operates based on the provided preconditions.

