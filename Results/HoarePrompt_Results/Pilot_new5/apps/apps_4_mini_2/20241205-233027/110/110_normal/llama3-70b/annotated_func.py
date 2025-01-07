#State of the program right berfore the function call: n and m are positive integers representing the dimensions of the pond, r is a positive integer representing the size of the scoop, and k is a positive integer representing the number of fishes to be placed, such that 1 ≤ n, m ≤ 100000, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n·m, 100000).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts four positive integers `n`, `m`, `r`, and `k` representing the dimensions of a pond, the size of a scoop, and the number of fishes to be placed, respectively. It calculates the minimum of `k` and the total number of possible scoop placements in a `(n - r + 1) x (m - r + 1)` area, and then divides this result by the total number of placements. The function outputs the fraction of fishes that can be placed in relation to the total possible placements, which can range from 0 to 1.

