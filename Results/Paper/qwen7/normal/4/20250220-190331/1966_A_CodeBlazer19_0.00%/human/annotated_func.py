#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the list of integers c contains n integers such that 1 ≤ c_i ≤ 100 for each c_i in c.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: Output State: The loop has executed `t` times. For each iteration, `k` is an integer input from the user split by space and converted to an integer, `l` is a list of integers input from the user split by space and converted using `map(int, input().split())`, and `i` is equal to `t`. After executing the loop, `n` will be the first integer input for the last iteration, `k` will be the second integer input for the last iteration, and `l` will be the list of integers for the last iteration.
    #
    #In simpler terms, after all iterations of the loop have finished, `i` will be equal to `t`, `n` will be the `n` value from the last iteration, `k` will be the `k` value from the last iteration, and `l` will be the list `l` from the last iteration. All previous inputs for `n`, `k`, and lists `l` will have been processed and printed `k-1` for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (number of test cases), followed by pairs of integers `n` and `k` (where `n` is the size of the list and `k` is an integer), and a list of `n` integers `c`. For each test case, it prints `k - 1`. After processing all test cases, it outputs nothing explicitly, but the state of the program includes the last processed values of `n`, `k`, and `c`.

