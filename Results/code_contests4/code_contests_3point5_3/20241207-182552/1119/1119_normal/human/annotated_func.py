#State of the program right berfore the function call: n and m are integers such that 2 <= n <= 1000, 0 <= m <= 105. The banned cells are represented as xi and yi where 1 <= xi, yi <= n.**
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: n and m are integers such that 2 <= n <= 1000, 0 <= m <= 105, `ban` is a list of pairs of values, `r` and `c` are lists of length n and m respectively with certain values being 0 based on the pairs in `ban`.
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `n` is greater than 2, `m` is as given, `ban` is a list of pairs, `r` and `c` are lists of length n and m respectively with certain values being 0 based on the pairs in `ban`, `ans` is incremented by the sum of specific values from lists `r` and `c` at indices `i`, `n - i + 1` for all i from 0 to (n - 2) // 2.
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`n` is greater than 2, `m` is as given, `ban` is a list of pairs, `r` and `c` are lists of length n and m respectively with certain values being 0 based on the pairs in `ban`, `ans` is incremented by the sum of specific values from lists `r` and `c` at indices `i`, `n - i + 1` for all i from 0 to (n - 2) // 2. If n is odd and there is a non-zero value at the center of lists `r` or `c`, then `ans` is incremented by 1. Otherwise, no change occurs to the program state.
    print(ans)
#Overall this is what the function does:The function `func` reads input values for n, m, and banned cells from stdin. It initializes lists `r` and `c` based on the banned cells. Then, it iterates through specified pairs of indices to calculate the sum of specific values from lists `r` and `c`. If n is odd and there is a non-zero value at the center of lists `r` or `c`, the sum is incremented by 1. Finally, the function prints the calculated sum `ans`.

