#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 2 ≤ n ≤ 1000, 0 ≤ m ≤ 105. The banned cells are represented as distinct coordinates (x, y) where 1 ≤ x, y ≤ n.**
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: ban is a list of length m with all elements updated, r is a list of length n+1 with the first element as 0 and the rest filled with 1s, c is a list of length n+1 with the second element as 0 and the rest filled with 1s, ans is 0, n and m remain unchanged
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `ban` is a list of length `m` with all elements updated, `r` is a list of length `n+1` with the first element as 0 and the rest filled with 1s, `c` is a list of length `n+1` with the second element as 0 and the rest filled with 1s, `ans` has been increased by the sum of `r[i], r[n - i + 1], c[i], c[n - i + 1]` for all valid `i` values in the loop, `i` is at least 2, `(n - 2) // 2` is positive, `n` and `m` remain unchanged
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`ban` is a list of length `m` with all elements updated, `r` is a list of length `n+1` with the first element as 0 and the rest filled with 1s, `c` is a list of length `n+1` with the second element as 0 and the rest filled with 1s, `ans` has been increased by the sum of `r[i], r[n - i + 1], c[i], c[n - i + 1]` for all valid `i` values in the loop, `i` is at least 2, `(n - 2) // 2` is positive, `n` and `m` remain unchanged. After entering the if condition, the program state satisfies the condition: `n` is odd and either `r[(n + 1) // 2]` or `c[(n + 1) // 2]` is non-zero, `ans` is increased by 1.
    print(ans)
#Overall this is what the function does:The function `func` reads input values for `n` and `m`, initializes lists `ban`, `r`, `c`, and `ans`, where `ban` represents banned cell coordinates, `r` and `c` are lists with constraints, and `ans` is set to 0. It then updates `r` and `c` based on the banned cell coordinates. After that, it calculates `ans` by summing specific elements from `r` and `c`. If `n` is odd and a specific condition is met, `ans` is incremented by 1. The function then prints the final value of `ans`. The function does not accept any parameters and does not have a return value.

