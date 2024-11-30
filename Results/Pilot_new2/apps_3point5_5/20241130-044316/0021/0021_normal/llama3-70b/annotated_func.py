#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100. The list a contains n distinct integers from 1 to n.**
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function `func` reads an integer `n` and a list of `n` distinct integers. It then calculates the maximum distance between the positions of 1 and `n` in the list, the minimum distance between these positions, and prints the maximum of these two distances along with `n - 1 - min_dist`. The function does not return any value directly but prints the calculated result. The function requires user input for `n` and the list `a` and operates on these values to determine the output.

