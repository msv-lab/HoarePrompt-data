#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 100 and 0 ≤ m ≤ min(1000, (n(n-1))/2).**
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    edges, ans = [rints() for _ in range(m)], [[] for _ in range(n)]
    for i in range(1, n + 1):
        ans[i - 1].append([i, i])
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to `n`, `m` is within the specified range, `edges` is a list of lists of integers, `ans` contains `[[1, 1], [2, 2], [3, 3], ..., [n, n]]`
    for (i, j) in enumerate(edges):
        ans[j[0] - 1].append([i + n + 1, j[0]])
        
        ans[j[1] - 1].append([i + n + 1, j[1]])
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to `n`, `m` is within the specified range, `edges` is a list of lists of integers, `ans` contains `[[1, 1], [2, 2], [3, 3], ..., [n, n], [i + n + 1, j[0]], [i + n + 1, j[1]], [i + n + 2, j[0]], [i + n + 2, j[1]], ...]` with all possible combinations of `[i + n + x, j[0]]` and `[i + n + x, j[1]]` appended to the sublists at index `j[0] - 1` and `j[1] - 1` respectively.
    for i in range(n):
        print(len(ans[i]))
        
        for j in ans[i]:
            print(*j)
        
    #State of the program after the  for loop has been executed: All elements in `ans` have been printed, `i` is the last integer after the loop finishes executing, `n` is greater than the final value of `i`, all elements in `ans` have been printed, each sublist in `ans` has at least one element.
#Overall this is what the function does:The function `func` reads input values for `n` and `m`, creates a list of lists for `edges` based on subsequent inputs, and initializes `ans` with sublists containing individual elements from 1 to `n`. It then appends combinations of elements to specific sublists in `ans` based on the input `edges`. Finally, it prints the length and elements of each sublist in `ans`. The function does not specify a clear overall purpose or constraints beyond handling input data and list manipulation.

