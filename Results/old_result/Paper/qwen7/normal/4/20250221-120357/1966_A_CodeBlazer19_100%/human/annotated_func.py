#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the next line of each test case contains n integers c_1, c_2, ..., c_n such that 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: Output State: The loop will execute `t` times. After all iterations, the variables `n`, `k`, `l`, and `p` will retain their final values determined by the last iteration of the loop. Specifically, `n` and `k` will be the values entered on the last iteration, `l` will be the list of integers entered on the last iteration, and `p` will be a list of counts of each unique element in `l`. If the maximum count in `p` is greater than or equal to `k`, the program will print `k - 1` during the last iteration; otherwise, it will print `n`.
    #
    #In summary, the output state after all iterations will reflect the state of the variables as they were on the last iteration of the loop, with `n`, `k`, `l`, and `p` updated based on the inputs provided during the last execution of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), followed by pairs of integers n and k, and a list of n integers. For each test case, it calculates the count of each unique element in the list and checks if the maximum count is greater than or equal to k. If true, it prints k - 1; otherwise, it prints n. After processing all test cases, it outputs the results for each case.

