#State of the program right berfore the function call: **
def func():
    n = int(input())
    a = list(map(int, input().split()))
    min_pos = a.index(1)
    max_pos = a.index(n)
    dist1 = abs(0 - max_pos)
    dist2 = abs(n - 1 - max_pos)
    dist3 = abs(0 - min_pos)
    dist4 = abs(n - 1 - min_pos)
    max_distance = max(dist1, dist2, dist3, dist4)
    print(max_distance)
#Overall this is what the function does:The function `func` reads an integer input `n`, followed by a list of integers. It then calculates the maximum distance of the indices of the first element `1` and the last element `n` in the list from the boundaries (`0` and `n-1`). Finally, it prints the maximum calculated distance. The function does not accept any parameters and does not return any value.

