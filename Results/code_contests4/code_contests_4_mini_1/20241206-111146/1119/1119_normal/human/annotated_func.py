#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, m is a non-negative integer such that 0 ≤ m ≤ 10^5, and m pairs of integers (xi, yi) representing the coordinates of banned cells are provided, where 1 ≤ xi, yi ≤ n and all (xi, yi) pairs are distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: `ban` is a list of length `m`, `ans` is 0, `r` is a list of length `n + 1` filled with 0s at the indices corresponding to the first element of each pair in `ban`, `c` is a list of length `n + 1` filled with 0s at the indices corresponding to the second element of each pair in `ban`.
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `ban` is a list of length `m`, `ans` is the cumulative sum from the iterations, `r` is a list of length `n + 1` filled with 0s, `c` is a list of length `n + 1` filled with 0s, and `i` is equal to \(2 + \frac{n - 2}{2}\) if \(n \geq 4\) or does not exist if \(n < 4\).
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`ban` is a list of length `m`, `ans` is increased by 1 if `n` is odd and either `r[(n + 1) // 2]` or `c[(n + 1) // 2]` is non-zero, while `r` and `c` remain lists of length `n + 1` filled with 0s. The variable `i` is equal to \(2 + \frac{n - 2}{2}\) if \(n \geq 4\) or does not exist if \(n < 4\).
    print(ans)
#Overall this is what the function does:The function accepts two integers, `n` (where 2 ≤ n ≤ 1000) and `m` (where 0 ≤ m ≤ 100,000), representing the size of a grid and the number of banned cells, respectively. It takes `m` pairs of coordinates that denote the banned cells within an `n x n` grid. The function calculates the total count of valid positions based on the rows and columns that are not banned, and it accounts for a specific condition when `n` is odd. The result is printed as an integer. If there are no banned cells, the function still returns a meaningful result based on the grid configuration.

