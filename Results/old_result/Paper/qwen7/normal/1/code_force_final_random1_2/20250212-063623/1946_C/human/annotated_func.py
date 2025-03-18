#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and each of the next n - 1 lines contains two integers v and u such that 1 ≤ v, u ≤ n representing an edge in the tree. Additionally, the sum of the values of n for all sets of input data does not exceed 10^5.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: The value of `t` is an integer such that \(1 \leq t < 10^4\), and `num_iterations` is equal to \(t - 1\). The function `solve()` has been called `t` times.
    #
    #This means that after all iterations of the loop have finished, `t` will be one less than its initial value because the loop runs `t` times, incrementing `num_iterations` each time until it reaches `t - 1`. The function `solve()` will have been executed exactly `t` times.
#Overall this is what the function does:The function processes input data consisting of an integer t, followed by t sets of input data. Each set includes two integers n and k, and then n - 1 lines representing edges in a tree. For each set of input data, the function calls `solve()` exactly t times. After processing all input sets, the function does not return any value but modifies the internal state by incrementing a counter `num_iterations` up to `t - 1`.

