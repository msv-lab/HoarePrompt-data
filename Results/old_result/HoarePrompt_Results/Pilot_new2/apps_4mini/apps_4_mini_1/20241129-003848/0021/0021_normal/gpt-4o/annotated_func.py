#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a is a list of n distinct integers where each integer is between 1 and n inclusive, representing a permutation of size n.
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
#Overall this is what the function does:The function reads an integer `n` (2 ≤ n ≤ 100) and a list `a` of `n` distinct integers representing a permutation of size `n` (each integer is between 1 and `n` inclusive). It then calculates the maximum distance of the positions of the integers `1` and `n` from both ends of the list (the first position and the last position), and prints the maximum of these distances.

