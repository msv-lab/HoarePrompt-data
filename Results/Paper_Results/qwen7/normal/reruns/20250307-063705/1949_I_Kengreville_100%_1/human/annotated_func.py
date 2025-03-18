#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n, where for each 0 ≤ i < n, x[i], y[i] are integers such that -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is an integer such that 1 ≤ r[i] ≤ 10^9. visited is a list of boolean values of length n, initially all set to False. coef is a list of length n, initially all set to None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: After the loop executes all iterations, `i` is equal to `n`, `n` is an input integer, `x`, `y`, and `r` are lists of length `n` where each element `x[j]`, `y[j]`, and `r[j]` (for `j` in range `n`) are integers assigned the values from the input split during the respective iteration of the loop. The `visited` list remains a list of boolean values of length `n` all set to `False`, and the `coef` list remains a list of length `n` filled with `None`.
    #
    #This means that after the loop completes, the variable `i` will have the value `n`, indicating that the loop has executed `n` times. Each of the lists `x`, `y`, and `r` will contain `n` elements, each populated with integer values provided by the user through the `input()` function during each iteration of the loop. The `visited` and `coef` lists remain unchanged as they were not modified within the loop.
    tot = 0
    bipartite = True
    ok = False
    for i in range(n):
        if not visited[i]:
            coef[i] = 1
            tot = 0
            bipartite = True
            dfs(i)
            ok = ok or bipartite and tot != 0
        
    #State: Output State: All elements in the `visited` list are marked as `True`, `coef` list has exactly one element set to `1` (at index `i` where `i` is the last index processed by the loop), all other elements in `coef` are `None`, `tot` is `0`, `bipartite` remains `True`, `ok` is `True`.
    #
    #Explanation: After the loop completes all its iterations, every vertex (index) in the graph represented by the lists `x`, `y`, and `r` will have been visited (`visited` list will have all `True` values). The `coef` list will contain exactly one `1` (set during the first visit of any unvisited node) and all other elements will remain `None`. The variable `tot` will be `0` as it is reset to `0` at the start of each iteration and never incremented. Since the loop ensures `bipartite` remains `True` unless a contradiction is found, and no contradictions were found, `bipartite` stays `True`. Finally, `ok` remains `True` because it is updated only when `bipartite` is `True` and `tot` is not `0`, which did not happen in any iteration.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: All elements in the `visited` list are marked as `True`, `coef` list has exactly one element set to `1` (at index `i` where `i` is the last index processed by the loop), all other elements in `coef` are `None`, `tot` is `0`, `bipartite` remains `True`, and `ok` is either `True` or `False` depending on whether the bipartite property holds true throughout the process.
#Overall this is what the function does:The function processes three lists \(x\), \(y\), and \(r\) of length \(n\) to determine if a bipartite matching exists where each element in \(x\) and \(y\) can be matched with an element in \(r\) under certain constraints. If such a matching exists and satisfies the condition that the total number of matches is non-zero, it prints 'YES'. Otherwise, it prints 'NO'. After processing, all elements in the `visited` list are marked as `True`, the `coef` list contains exactly one element set to `1` (indicating the starting node of the matching process), and all other elements are `None`. The `tot` variable is set to `0`, and the `bipartite` flag remains `True` unless a contradiction is found.

