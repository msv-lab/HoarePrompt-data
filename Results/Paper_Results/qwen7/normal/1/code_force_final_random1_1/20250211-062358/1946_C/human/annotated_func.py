#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5. The subsequent n - 1 lines contain pairs of integers v and u such that 1 ≤ v, u ≤ n, representing the edges of the tree.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: `t` is an integer such that \(0 \leq t < 10^4\).
    #
    #Explanation: Given that `t` starts within the range \(1 \leq t \leq 10^4\) and with each iteration of the loop, `t` is decremented by 1, after all iterations of the loop, `t` will be less than 0 but since `t` cannot be negative, it will be 0. Therefore, after the loop executes all its iterations, `t` will be 0.
#Overall this is what the function does:The function processes multiple test cases, each involving a tree structure defined by the number of nodes (n) and edges (n-1). For each test case, it calls the `solve()` function to handle the tree data. After processing all test cases, it ensures that the variable `t`, initially within the range 1 to 10^4, is reduced to 0. The function does not return any value but modifies the state of the program by decrementing `t` until it reaches 0.

