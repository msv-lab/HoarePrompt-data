#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and each of the next n - 1 lines contains two integers v and u such that 1 ≤ v, u ≤ n representing an edge in the tree.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and each of the next n - 1 lines contains two integers v and u such that 1 ≤ v, u ≤ n representing an edge in the tree, after executing the loop all t sets of input data have been processed by the function solve().
#Overall this is what the function does:The function processes multiple sets of input data, each containing an integer t, followed by t sets of tree structures defined by integers n and k, and the edges of the tree. After processing all input sets, it ensures that all specified trees have been analyzed according to the given parameters.

