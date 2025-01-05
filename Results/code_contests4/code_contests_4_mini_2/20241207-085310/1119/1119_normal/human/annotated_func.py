#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, m is a non-negative integer such that 0 ≤ m ≤ 100, and for each of the m banned cells, the coordinates (xi, yi) are integers satisfying 1 ≤ xi, yi ≤ n, with all banned cells being distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000; `m` is a non-negative integer; `ban` is a list with `m` elements; `r` is a list where elements at indices corresponding to the first elements of `ban` are 0, and all other elements remain 1; `c` is a list where elements at indices corresponding to the second elements of `ban` are 0, and all other elements remain 1; `ans` is 0.
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `ans` is the sum of all specified elements from `r` and `c` during each iteration, `i` is `2 + (n - 2) // 2` (which is the value after the final iteration), `n` is at least 4.
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`ans` is the sum of all specified elements from `r` and `c` during each iteration plus 1, `i` is `2 + (n - 2) // 2`, `n` is at least 4 and odd, and either `r[(n + 1) // 2]` or `c[(n + 1) // 2]` is non-zero.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (2 ≤ n ≤ 1000) and a non-negative integer `m` (0 ≤ m ≤ 100) representing the number of banned cells in a grid. It reads the coordinates of these banned cells and calculates a value `ans` based on the number of unbanned rows and columns. The function returns the computed value `ans`, which counts how many valid cells remain unblocked by the banned cells, with an additional count if `n` is odd and the middle cell is unbanned.

