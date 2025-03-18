#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5, and v and u are integers such that 1 ≤ v, u ≤ n. Additionally, the sum of the values of n across all sets of input data does not exceed 10^5.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: The integer value read from standard input is reduced to 0 after the loop executes all its iterations.
    #
    #Explanation: Given that the integer value is decremented by 1 with each iteration of the loop, and it must be at least 1 after 3 iterations, it will reach 0 after the loop has completed all its iterations (i.e., when the integer value becomes 0 and the loop condition fails).
#Overall this is what the function does:The function reads an integer `t` from standard input, which represents the number of test cases. For each test case, it calls the `solve()` function. After processing all test cases, the integer `t` is reduced to 0. The function internally processes values for `n`, `k`, `v`, and `u` based on given constraints, performs certain operations, and does not return any value.

