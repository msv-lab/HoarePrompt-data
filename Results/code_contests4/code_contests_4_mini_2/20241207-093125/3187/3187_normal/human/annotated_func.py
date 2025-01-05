#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, m is an integer such that 0 ≤ m ≤ min(1000, (n(n-1))/(2)), and m pairs of colors are given where each pair consists of two integers representing colors numbered from 1 to n.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    edges, ans = [rints() for _ in range(m)], [[] for _ in range(n)]
    for i in range(1, n + 1):
        ans[i - 1].append([i, i])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `ans` is a list containing `n` elements, where each element `ans[i-1]` contains the list `[[i, i]]` for `i` from 1 to `n`.
    for (i, j) in enumerate(edges):
        ans[j[0] - 1].append([i + n + 1, j[0]])
        
        ans[j[1] - 1].append([i + n + 1, j[1]])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `ans` is a list containing `n` elements, where each `ans[i-1]` contains the original `[[i, i]]` plus all appended elements from the edges related to node `i`.
    for i in range(n):
        print(len(ans[i]))
        
        for j in ans[i]:
            print(*j)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `i` is equal to `n`; `ans` is a list containing `n` elements where all elements of `ans[0]` to `ans[n-1]` have been printed, and each element of `ans[i]` has been printed with its corresponding values.
#Overall this is what the function does:The function accepts two integers `n` and `m`, where `1 ≤ n ≤ 100` and `0 ≤ m ≤ min(1000, (n(n-1))/(2))`. It processes `m` pairs of colors and constructs a list of lists called `ans`, where each element `ans[i]` contains pairs representing the nodes associated with color `i`. The function then prints the number of entries in each `ans[i]` followed by the entries themselves. The output may vary based on the input pairs provided, but the function does not return any value; it only prints the results.

