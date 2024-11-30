#State of the program right berfore the function call: 
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
#Overall this is what the function does:The function prompts the user for an integer `n` and a list of integers `a`. It then calculates the maximum distance between the indices of the values 0 and `n-1` in the list `a`, and prints this maximum distance. The function does not accept any parameters and does not return any value.

