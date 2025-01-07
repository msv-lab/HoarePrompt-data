#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a is a list of n distinct integers where each integer is in the range 1 to n.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100) and a list `a` of `n` distinct integers ranging from 1 to `n`. It calculates the maximum distance between the positions of the integers 1 and `n` in the list, adjusting for the total length of the list. It then prints the maximum value between this calculated distance and the distance of `n-1 - min_dist`, where `min_dist` is calculated similarly. The function does not return a value, but only prints the result.

