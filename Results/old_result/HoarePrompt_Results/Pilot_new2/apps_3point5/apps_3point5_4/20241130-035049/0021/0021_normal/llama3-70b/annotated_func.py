#State of the program right berfore the function call: ** n is an integer such that 2 <= n <= 100. The list a contains n distinct integers where each integer ai is in the range 1 <= ai <= n.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    pos1 = a.index(1)
    posn = a.index(n)
    max_dist = max(abs(pos1 - posn) - 1, n - 2)
    min_dist = min(abs(pos1 - posn) - 1, n - 2)
    print(max(max_dist, n - 1 - min_dist))
#Overall this is what the function does:The function reads an integer n from input and a list of n integers. It then finds the positions of the integers 1 and n in the list and calculates the maximum possible distance between these positions, excluding the endpoints. It prints this maximum distance.

