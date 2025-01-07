#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a is a list of n distinct integers where each integer is between 1 and n (inclusive).
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
#Overall this is what the function does:The function accepts an integer `n` (2 ≤ n ≤ 100) and a list `a` of `n` distinct integers (each between 1 and n inclusive), calculates the distances of the elements 1 and n from the ends of the list, and returns the maximum of those distances by printing it. If either integer 1 or n is not present in the list, a ValueError will occur.

