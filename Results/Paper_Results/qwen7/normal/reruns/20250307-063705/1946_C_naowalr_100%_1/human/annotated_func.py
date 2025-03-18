#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each set of input data contains two integers n and k such that 1 ≤ k < n ≤ 10^5, and each subsequent line of input contains two integers v and u such that 1 ≤ v, u ≤ n representing an edge in the tree. Additionally, the sum of the values of n across all sets of input data does not exceed 10^5.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: `t` is an integer such that \(1 \leq t < 10^4\), `solve()` has been called the total number of times equal to the initial value of `t`, and the loop counter has decreased to 0.
    #
    #This means that after all iterations of the loop have finished, `t` will be less than its initial value and will be non-negative (since it starts from a positive integer and decreases by 1 each iteration). The function `solve()` will have been executed exactly `t` times, which is the initial value of `t` before any iterations began. The loop counter, which started at `t` and was decremented by 1 in each iteration, will now be 0.
#Overall this is what the function does:The function processes multiple sets of input data, each containing an integer `t`, followed by pairs of integers `n` and `k`, and then edges represented by pairs of integers `v` and `u`. For each set, it calls the `solve()` function `t` times. After processing all sets, it ensures that `t` is reduced by one for each call to `solve()` and eventually becomes zero. The function does not return any value but modifies the state by processing the input data and calling `solve()` repeatedly.

