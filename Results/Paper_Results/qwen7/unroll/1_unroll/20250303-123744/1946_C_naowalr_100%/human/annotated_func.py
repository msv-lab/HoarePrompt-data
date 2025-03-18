#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and each set also contains n - 1 lines describing the edges of the tree where each line contains two integers v and u such that 1 ≤ v, u ≤ n.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and each set also contains n - 1 lines describing the edges of the tree where each line contains two integers v and u such that 1 ≤ v, u ≤ n. After executing the loop, the variable `t` is decremented by 1 for each iteration, and the `solve()` function is called with the input data for each set of input.
    #
    #In simpler terms: The number of sets of input data (represented by `t`) is reduced by one after all iterations of the loop have finished.
#Overall this is what the function does:The function processes a series of input data sets representing tree structures. Each data set contains an integer t, followed by integers n and k, and then n-1 lines describing the edges of the tree. For each set, the `solve()` function is called to process the tree data. After processing all sets, the value of t is reduced by the number of sets processed. The function does not return any value but modifies the input data by decrementing t and performing operations on the tree structure as specified by n, k, and the edges.

