#State of the program right berfore the function call: n and m are integers such that 2 ≤ n ≤ 1000 and 0 ≤ m ≤ 105. The following m lines each contain two integers xi and yi such that 1 ≤ xi, yi ≤ n, representing the coordinates of the banned cells. All given cells are distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000 (inclusive); `m` is less than or equal to the number of updates made to `r` and `c` through the loop; `ban` is a list of `m` integers; `r` is a list of length `n + 1` with elements updated to `0` at indices specified by `x` in `ban` and all other elements still `1`; `c` is a list of length `n + 1` with elements updated to `0` at indices specified by `y` in `ban` and all other elements still `1`; `ans` is `0`.
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `ans` is the sum of `r[i] + r[n - i + 1] + c[i] + c[n - i + 1]` for all valid `i` from 2 to `(n - 2) // 2`, `n` must be at least 4, `m` is less than or equal to the number of updates made to `r` and `c` through the loop, `ban` is a list of `m` integers, `r` is a list of length `n + 1` with elements updated to `0` at indices specified by `x` in `ban` and all other elements are `1`, `c` is a list of length `n + 1` with elements updated to `0` at indices specified by `y` in `ban` and all other elements are `1`.
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`ans` is the sum of `r[i] + r[n - i + 1] + c[i] + c[n - i + 1]` for all valid `i` from 2 to `(n - 2) // 2`, plus 1 if the condition `(n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2]))` holds true. `n` must be at least 4, `m` is less than or equal to the number of updates made to `r` and `c` through the loop, `ban` is a list of `m` integers, `r` is a list of length `n + 1` with elements updated to `0` at indices specified by `x` in `ban` and all other elements are `1`, `c` is a list of length `n + 1` with elements updated to `0` at indices specified by `y` in `ban` and all other elements are `1`.
    print(ans)
#Overall this is what the function does:The function processes an integer \( n \) (the size of the grid) and another integer \( m \) (the number of banned cells). It then takes \( m \) lines of input, each containing two integers \( x_i \) and \( y_i \) representing the coordinates of banned cells on a \( n \times n \) grid. After processing the banned cells, the function calculates the number of paths from the top-left corner (1,1) to the bottom-right corner (n,n) that do not pass through any of the banned cells. This is done by summing up the values of specific grid positions and adding a potential additional path if the grid size \( n \) is odd. The function returns the total count of such paths as an integer.

