#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n ≤ 100 and 0 ≤ m ≤ min(1000, (n(n-1))/2).**
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    edges, ans = [rints() for _ in range(m)], [[] for _ in range(n)]
    for i in range(1, n + 1):
        ans[i - 1].append([i, i])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ n ≤ 100, `m` is a non-negative integer such that 0 ≤ m ≤ min(1000, (n(n-1))/2), `edges` is a list of sublists with necessary information for the final value of `n`, `ans` is a list of `n` lists where the `i-1`th list contains the sublist `[i, i]` for all `i` from 1 to `n`
    for (i, j) in enumerate(edges):
        ans[j[0] - 1].append([i + n + 1, j[0]])
        
        ans[j[1] - 1].append([i + n + 1, j[1]])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a non-negative integer, `edges` is a list of sublists with additional sublists, `ans` is a list of `n` lists with multiple new sublists appended to various lists
    for i in range(n):
        print(len(ans[i]))
        
        for j in ans[i]:
            print(*j)
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to the length of `ans` list, `i` is equal to `n`, `ans` is a list of lists where each list has been printed by the loop
#Overall this is what the function does:The function `func` reads in two positive integers `n` and `m` within specified ranges. It then creates a list `edges` based on input and modifies a list `ans` accordingly. Subsequently, it prints out the length of each sublist in `ans` along with their contents. The function does not accept any parameters explicitly, but it operates based on user input.

