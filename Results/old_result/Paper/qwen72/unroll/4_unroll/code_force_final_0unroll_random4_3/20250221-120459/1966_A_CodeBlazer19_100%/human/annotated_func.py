#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, n and k are integers for each test case where 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100, and c is a list of n integers where 1 ≤ c_i ≤ 100.
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
        
    #State: The loop has finished executing all iterations, and the values of `t`, `n`, `k`, and `c` remain unchanged. The output of the loop will be a series of integers, each either `k - 1` or `n`, depending on the condition `max(p) >= k` for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case is defined by an integer `n` and an integer `k`, along with a list `l` of `n` integers. For each test case, the function checks if any integer in the list `l` appears at least `k` times. If so, it prints `k - 1`; otherwise, it prints `n`. After processing all test cases, the function terminates, and the values of `t`, `n`, `k`, and `l` are not modified. The function does not return any value, but it produces a series of integer outputs, one for each test case.

