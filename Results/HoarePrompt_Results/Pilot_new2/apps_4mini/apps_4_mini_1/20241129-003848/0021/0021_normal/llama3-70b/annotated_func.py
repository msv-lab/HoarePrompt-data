#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a is a list of n distinct integers where each integer is in the range from 1 to n.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function accepts an integer `n` and a list `a` of `n` distinct integers, calculates the maximum distance between the positions of the integers 1 and `n`, and prints the result without returning any value.

