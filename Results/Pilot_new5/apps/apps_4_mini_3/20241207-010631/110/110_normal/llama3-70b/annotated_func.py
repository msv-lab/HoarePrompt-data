#State of the program right berfore the function call: n and m are positive integers representing the dimensions of the pond (1 ≤ n, m ≤ 10^5), r is a positive integer representing the size of the scoop (1 ≤ r ≤ min(n, m)), and k is a positive integer representing the number of fishes to be placed in the pond (1 ≤ k ≤ min(n·m, 10^5)).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts four positive integer parameters: `n` and `m` representing the dimensions of a pond, `r` representing the size of a scoop, and `k` representing the number of fishes to be placed in the pond. It calculates the minimum between `k` and the total possible positions for placing the fishes, which is determined by the area of the pond that is not obstructed by the scoop's size. Finally, it returns the ratio of this minimum value to the total number of possible positions for placing the fishes in the pond. This means that the function outputs a float representing the proportion of fishes that can be placed in the valid area of the pond.

