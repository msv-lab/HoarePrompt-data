#State of the program right berfore the function call: 
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, then reads a list of integers separated by spaces. It calculates the maximum distance between the indices of 1 and `n`, as well as the minimum distance. It then prints the maximum value between the maximum distance and `n - 1` minus the minimum distance. The function does not accept any parameters and does not return any value.

