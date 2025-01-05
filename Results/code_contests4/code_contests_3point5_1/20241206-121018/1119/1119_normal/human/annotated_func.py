#State of the program right berfore the function call: **Precondition**: 
- n and m are integers where 2 ≤ n ≤ 1000 and 0 ≤ m ≤ 105.
- The coordinates of banned cells are distinct and each coordinate is within the range 1 to n.
- The field rows are numbered from 1 to n and columns are numbered from 1 to n.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: `r[x]` and `c[y]` will be 0 for all x, y in `ban`
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `r[x]` and `c[y]` are both 0 for all x, y in `ban`, `i` is `n//2`, `ans` is the sum of specified values for all `i` from 2 to `n//2`
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`r[x]` and `c[y]` are both 0 for all x, y in `ban`, `i` is `n//2`, `ans` is the sum of specified values for all `i` from 2 to `n//2` with an additional 1 added. If `n` is odd and either `r[(n + 1) // 2]` or `c[(n + 1) // 2]` is non-zero, then the program enters the if condition and the state remains the same.
    print(ans)
#Overall this is what the function does:The function `func` reads input integers `n` and `m`, then processes banned cell coordinates `ban` and calculates a value `ans`. It iterates over the rows and columns, updating their values based on the banned cells. It then calculates the sum of specific values for pairs of rows and columns. If `n` is odd and the middle row or column is not banned, it increments the sum by 1. Finally, it prints the calculated `ans`. The function does not explicitly return a value.

