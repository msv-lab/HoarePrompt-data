#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and for each set, n - 1 lines follow, each containing two integers v and u such that 1 ≤ v, u ≤ n, representing an edge in the tree.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and for each set, n - 1 lines follow, each containing two integers v and u such that 1 ≤ v, u ≤ n, representing an edge in the tree. After executing the loop, the value of t remains unchanged, and for each set of input data, the values of n and k, as well as the edges defined by v and u, remain the same as the initial state.
#Overall this is what the function does:The function processes input data consisting of an integer t, followed by t sets of input data. Each set includes two integers n and k, and n-1 lines representing edges in a tree. After processing, it outputs information based on the given input data. The function does not return any value but modifies the internal state based on the input. The value of t remains unchanged, and the values of n, k, and the edges remain the same as the initial state after processing.

