#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and a is a list of n distinct integers from 1 to n.**
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
#Overall this is what the function does:The function `func` reads an integer `n` followed by a list of `n` distinct integers. It then calculates the maximum distance between the indices of 0 and `n-1` in the list `a`, and prints this maximum distance. The function does not explicitly return any value.

