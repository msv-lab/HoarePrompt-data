#State of the program right berfore the function call: n is an integer representing the size of the n x n checkered field, where 2 ≤ n ≤ 1000; m is a non-negative integer representing the number of banned cells, where 0 ≤ m ≤ 100,000; and each banned cell is defined by its coordinates (xi, yi) where 1 ≤ xi, yi ≤ n and all provided coordinates are distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    ban, r, c, ans = [rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0
    for (x, y) in ban:
        r[x], c[y] = 0, 0
        
    #State of the program after the  for loop has been executed: `n` is an integer, `m` is a non-negative integer, `ban` is a list of `m` items, `r` is a list of size `n + 1` where all elements corresponding to the first elements of `ban` are 0, `c` is a list of size `n + 1` where all elements corresponding to the second elements of `ban` are 0, `ans` is 0.
    for i in range(2, 2 + (n - 2) // 2):
        ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
        
    #State of the program after the  for loop has been executed: `n` is an integer, `m` is a non-negative integer, `ban` is a list of `m` items, `r` is a list of size `n + 1`, `c` is a list of size `n + 1`, `ans` is updated based on the sums calculated during the loop, if it executes, else `ans` is 0.
    if (n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2])) :
        ans += 1
    #State of the program after the if block has been executed: *`n` is an integer, `m` is a non-negative integer, `ban` is a list of `m` items, `r` is a list of size `n + 1`, `c` is a list of size `n + 1`. If `n` is odd and either `r[(n + 1) // 2]` or `c[(n + 1) // 2]` is true, then `ans` is updated to `ans + 1`. If the condition is not met, `ans` remains 0.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (the size of an n x n checkered field) and a non-negative integer `m` (the number of banned cells). It processes the banned cell coordinates, updates the row and column availability, and calculates the total number of available cells. If `n` is odd and the middle cell is not banned, it increments the total by 1. Finally, it prints the total number of available cells. The function does not handle cases where `m` exceeds the total cells available or where invalid coordinates for banned cells may be provided.

