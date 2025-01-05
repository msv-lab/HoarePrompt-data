#State of the program right berfore the function call: n is an integer between 1 and 100 (inclusive), m is a non-negative integer such that 0 <= m <= min(1000, (n(n-1))/(2)), and for each of the m lines, there are two integers representing pairs of colors (from 1 to n) which harmonize with each other.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    edges, ans = [rints() for _ in range(m)], [[] for _ in range(n)]
    for i in range(1, n + 1):
        ans[i - 1].append([i, i])
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 (inclusive), `m` is a non-negative integer such that 0 <= `m` <= min(1000, (n(n-1))/(2)), `edges` is a list of `m` elements, each being a list of integers, `ans` is a list containing `n` elements, each being a list with the format [[i, i]] for `i` from 1 to `n`.
    for (i, j) in enumerate(edges):
        ans[j[0] - 1].append([i + n + 1, j[0]])
        
        ans[j[1] - 1].append([i + n + 1, j[1]])
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100; `m` is non-negative and less than or equal to min(1000, (n(n-1))/(2)); `edges` is a list of `m` elements; `ans` contains `n` elements, each being a list that includes the initial `[[i, i]]` for `i` from 1 to `n` plus the lists appended for each edge processed.
    for i in range(n):
        print(len(ans[i]))
        
        for j in ans[i]:
            print(*j)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `ans` contains `n` non-empty iterables, each `ans[i]` has been fully printed, `i` is equal to `n - 1`, and `j` is the last element of `ans[n-1]`.
#Overall this is what the function does:The function accepts no parameters and processes a list of edges representing pairs of harmonizing colors. It constructs a result list for each color and prints the number of entries for each color’s list, followed by the entries themselves. Each list will include the color itself and any additional colors from the edges. The function does not return any value.

