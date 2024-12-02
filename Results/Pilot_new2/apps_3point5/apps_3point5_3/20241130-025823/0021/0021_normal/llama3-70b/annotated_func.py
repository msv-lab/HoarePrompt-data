#State of the program right berfore the function call: 
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function reads an integer input n, followed by a list of integers. It then calculates the maximum distance between the positions of 1 and n in the list, the minimum distance between the positions of 1 and n in the list, and prints the maximum of the two distances along with n - 1. The function does not accept any parameters and does not return anything.

