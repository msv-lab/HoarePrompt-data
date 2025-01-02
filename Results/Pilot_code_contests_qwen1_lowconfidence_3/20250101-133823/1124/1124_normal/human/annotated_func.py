#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, m is an integer such that 0 ≤ m ≤ 10^5, and the subsequent m lines each contain two integers xi and yi such that 1 ≤ xi, yi ≤ n, representing the coordinates of banned cells. All given cells are distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 1000\); `m` is an integer such that \(0 < m \leq 10^5\); `ban` is a list of `m` lists each containing 4 integers; `r` is a list of length `n + 1` with all elements set to `1`, except for positions `x` and `y` which are both `0`; `c` is a list of length `n + 1` with all elements set to `1`, except for positions `x` and `y` which are both `0`; `ans` is `0`.
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `ans` is equal to the sum of `r[i] + r[n - i + 1] + c[i] + c[n - i + 1]` for all valid `i` in the range `2` to `2 + (n - 2) // 2`, `r` and `c` remain unchanged, where `i` is within the specified range.
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: `ans` is the sum of `r[i] + r[n - i + 1] + c[i] + c[n - i + 1]` for all valid `i` in the range `2` to `2 + (n - 2) // 2`, plus 1 if `n` is an odd number and either the middle element of `r` or the middle element of `c` is non-zero. `r` and `c` remain unchanged.
    print(ans)
#Overall this is what the function does:The function accepts an n x n grid configuration with constraints on the range of n (2 ≤ n ≤ 1000) and m (0 ≤ m ≤ 10^5), along with a list of banned cells (xi, yi) such that 1 ≤ xi, yi ≤ n. It then calculates the number of valid paths from the top-left corner (1, 1) to the bottom-right corner (n, n) while avoiding all banned cells. The function returns the total count of such valid paths. If n is odd, it also checks the central cell (n+1)//2 for either row or column to ensure there is no ban there.

