#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. Additionally, a list of n integers c represents the numbers written on the cards, where 1 ≤ c_i ≤ 100 for each i.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: Output State: `t` must be greater than 0, `i` is equal to `t-1`, `n` is an input integer, `k` is an input integer, `l` is a list of integers obtained from the input split and mapped to integers.
    #
    #In natural language: After the loop has executed all its iterations, the variable `t` must still be greater than 0 (since it was initially an integer between 1 and 500, and the loop continues as long as `i < t`). The variable `i`, which starts at 0 and increments by 1 in each iteration, will be equal to `t-1` after the last iteration. The values of `n`, `k`, and `l` will correspond to the inputs provided for each iteration of the loop, but since the loop has completed, these values will not change further.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers `n` and `k`, and a list of `n` integers `c`. For each test case, it prints the value `k - 1`. After processing all test cases, the function does not return any value but outputs the results for each test case.

