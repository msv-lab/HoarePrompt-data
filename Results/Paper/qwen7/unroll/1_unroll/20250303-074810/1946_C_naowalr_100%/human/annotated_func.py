#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5, and for each edge described by v and u, 1 ≤ v, u ≤ n.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5, and for each edge described by v and u, 1 ≤ v, u ≤ n. After executing the loop, the variable `solve()` has been called `t` times.
#Overall this is what the function does:The function processes input data consisting of `t` sets of values, where each set includes integers `n` and `k` (with `1 ≤ k < n ≤ 10^5`) and a series of edges defined by pairs of integers `v` and `u` (with `1 ≤ v, u ≤ n`). For each set of input data, the function calls `solve()` exactly once. After processing all sets, the function returns no value but ensures that `solve()` has been executed `t` times.

