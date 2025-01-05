#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n ≤ 100 and 0 ≤ m ≤ min(1000, (n(n-1))/2).**
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    edges, ans = [rints() for _ in range(m)], [[] for _ in range(n)]
    for i in range(1, n + 1):
        ans[i - 1].append([i, i])
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to `n`, `m` is a positive integer satisfying the given constraints, `edges` is a list of lists of integers, `ans` contains [[1, 1], [2, 2], ..., [n, n]]
    for (i, j) in enumerate(edges):
        ans[j[0] - 1].append([i + n + 1, j[0]])
        
        ans[j[1] - 1].append([i + n + 1, j[1]])
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to `n`, `m` is a positive integer, `edges` contains all the lists of integers, `ans` contains the updated values after all iterations of the loop, `i` is the total number of iterations, `j` is the last list of integers in `edges`
    for i in range(n):
        print(len(ans[i]))
        
        for j in ans[i]:
            print(*j)
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `i` is equal to n-1, `j` is the last element in `ans[i]`, `ans` contains elements, the length of the last element in `ans` is printed
#Overall this is what the function does:The function `func` reads two positive integers `n` and `m`, then constructs a list `ans` with elements [[1, 1], [2, 2], ..., [n, n]]. It then updates `ans` based on the values in `edges`. Finally, it prints the length of each element in `ans` and the elements themselves. The function does not explicitly return any value.

