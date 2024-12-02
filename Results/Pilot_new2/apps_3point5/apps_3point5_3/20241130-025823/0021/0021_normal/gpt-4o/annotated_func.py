#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100. The input array a contains n distinct integers from 1 to n.**
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
#Overall this is what the function does:The function `func` reads an integer `n` and an array `a` of length `n` containing distinct integers from 1 to `n`. It then calculates the maximum distance of the indices of the minimum value (1) and maximum value (`n`) in the array from the boundaries (0 and `n-1`), and prints this maximum distance value. The function does not have a return value.

