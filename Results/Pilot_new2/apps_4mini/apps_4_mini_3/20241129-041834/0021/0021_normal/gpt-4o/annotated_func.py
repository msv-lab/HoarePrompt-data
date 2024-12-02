#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a is a list of n distinct integers where each integer is in the range [1, n].
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
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100) and a list `a` of `n` distinct integers (ranging from 1 to n). It calculates the maximum distance from the positions of the integers 1 and n to both ends of the list (index 0 and index n-1) and prints this maximum distance. The function does not include any handling for invalid input cases or checks beyond the initial assumptions about the input.

