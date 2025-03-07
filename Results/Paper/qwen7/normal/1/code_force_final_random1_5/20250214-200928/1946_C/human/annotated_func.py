#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers such that 1 ≤ k < n ≤ 10^5, and v and u are integers such that 1 ≤ v, u ≤ n.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: The function `solve()` has been called three times. The value read from `sys.stdin.readline()` is `N + 1`, where `N` is the number of iterations the loop will execute. All other variables in their initial states remain unchanged.
    #
    #This means that the loop will continue to execute until the value read from `sys.stdin.readline()` is equal to the total number of iterations, which is `N + 1`. After that, the loop will terminate, and `solve()` will have been called `N + 1` times.
#Overall this is what the function does:The function reads an integer `t` from standard input, which determines the number of times the `solve()` function will be called (up to `t` times). After executing `solve()` `t` times, the function terminates without returning any value.

