#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100. The list a contains n distinct integers from 1 to n.**
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function `func` reads an integer `n` and a list of `n` distinct integers from 1 to `n`. It then calculates the maximum distance between the positions of the integers 1 and `n` in the list, calculates the minimum distance between them, and prints the maximum of these two distances. The function works under the constraint that `n` is an integer such that 2 <= n <= 100.

