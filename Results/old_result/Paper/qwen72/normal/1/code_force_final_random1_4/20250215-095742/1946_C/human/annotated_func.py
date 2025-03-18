#State of the program right berfore the function call: The `solve` function is expected to handle the processing of each set of input data, where each set includes the number of vertices `n` and the number of edges to remove `k`, with the constraints \(1 \le k < n \le 10^5\). Additionally, `n - 1` lines follow, each containing two integers `v` and `u` representing an edge in the tree, with \(1 \le v, u \le n\).
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: The number of sets of input data is equal to the integer value read from `sys.stdin.readline()`, `_` is equal to this integer value minus 1, and the function `solve()` has been called this many times.
#Overall this is what the function does:The function `func_1` reads an integer from standard input which represents the number of test cases. For each test case, it calls the `solve` function. After processing all test cases, the function has no return value and the state of the program indicates that the `solve` function has been called the specified number of times. The function does not modify any global variables or states outside of its scope.

