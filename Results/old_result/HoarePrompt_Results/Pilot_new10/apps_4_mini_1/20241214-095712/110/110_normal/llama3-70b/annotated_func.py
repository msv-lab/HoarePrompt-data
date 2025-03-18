#State of the program right berfore the function call: n and m are integers representing the dimensions of the pond, r is an integer representing the size of the scoop, and k is an integer representing the number of fishes, with the constraints 1 ≤ n, m ≤ 10^5, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n·m, 10^5).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts four integers as input: `n` (pond length), `m` (pond width), `r` (scoop size), and `k` (number of fishes). It calculates the maximum number of fishes that can be found within a scoopable area of the pond and returns the proportion of that maximum to the total possible number of scoopable positions. If the total number of scoopable positions is zero (which happens if `n` is less than or equal to `r` or `m` is less than or equal to `r`), the function will perform the division but may yield an undefined behavior. Therefore, there is a potential edge case where division by zero can occur.

