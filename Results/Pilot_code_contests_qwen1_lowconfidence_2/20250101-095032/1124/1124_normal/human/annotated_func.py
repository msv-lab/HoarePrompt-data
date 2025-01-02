#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, m is an integer such that 0 ≤ m ≤ 10^5, and there are m pairs of integers (xi, yi) such that 1 ≤ xi, yi ≤ n, representing the coordinates of banned cells. All given cells are distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `m` is 0, `ban` is an empty list, `r` is a list of length `n + 1` filled with 1s, `c` is a list of length `n + 1` filled with 1s, and `ans` is 0.
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: Output State:
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`n` is an integer, `r` is a list of integers, `c` is a list of integers, and `ans` is equal to the original value of `ans` plus 1. If `n` modulo 2 is not 0 and either the element at index `(n + 1) // 2` in list `r` is truthy or the element at index `(n + 1) // 2` in list `c` is truthy, then the condition is satisfied. Otherwise, the condition is not satisfied and the values of `n`, `r`, `c`, and `ans` remain unchanged.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (2 ≤ n ≤ 1000) and an integer `m` (0 ≤ m ≤ 10^5) representing the number of banned cells, along with `m` pairs of integers (xi, yi) (1 ≤ xi, yi ≤ n) indicating the coordinates of the banned cells. The function processes the banned cells by marking them in two lists `r` and `c` which represent rows and columns respectively. It then calculates the number of valid squares of different sizes that can be formed within the grid of size `n x n`, excluding the banned cells. Finally, it checks for a central cell if `n` is odd and adds one to the count if the central cell is not banned. The function returns the total count of valid squares.

