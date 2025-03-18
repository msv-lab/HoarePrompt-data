#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a is a list of n distinct integers where each integer a[i] satisfies 1 ≤ a[i] ≤ n.
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
#Overall this is what the function does:The function accepts an integer `n` (2 ≤ n ≤ 100) and a list `a` of `n` distinct integers (1 ≤ a[i] ≤ n). It calculates the maximum distance from either end of the list (index 0 or index n-1) to the positions of the integers 1 and n in the list `a`. The function then prints this maximum distance. However, it does not handle cases where the input does not meet the specified constraints, such as invalid integers or improper list lengths.

