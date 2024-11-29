#State of the program right berfore the function call: n is an integer where 2 ≤ n ≤ 100, and a is a list of n distinct integers such that each integer a[i] (1 ≤ a[i] ≤ n) represents a permutation of the integers from 1 to n.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function accepts an integer `n` and a list `a`, where `n` is a permutation of integers from 1 to `n`, and computes two distances based on the positions of the integers 1 and `n` within the list. It calculates the maximum distance between these positions and prints the greater value between `max_dist` and the difference of `n - 1 - min_dist`. The function does not handle any invalid input cases, such as the input not being a valid permutation or being out of the specified range.

