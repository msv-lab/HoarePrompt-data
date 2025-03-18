#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a is a list of n distinct integers where each integer is in the range from 1 to n.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100) and a list `a` containing `n` distinct integers ranging from 1 to `n`. It calculates the maximum distance between the positions of the integers 1 and `n` in the list, while also considering the distance from the ends of the list. The function prints the maximum distance calculated but does not return any value.

