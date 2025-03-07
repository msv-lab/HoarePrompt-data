#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. Each test case consists of two integers n and k where 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100, followed by a list of n integers c_1, c_2, ..., c_n where 1 ≤ c_i ≤ 100.
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
        
    #State: The output state consists of `t` lines, each corresponding to the result of one test case from the input. For each test case, the output is either `k - 1` if the highest frequency of any number in the list `l` is at least `k`, or `n` if no number in the list `l` appears at least `k` times. The variables `n`, `k`, and `l` are re-assigned in each iteration of the loop, but `t` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`, followed by a list of `n` integers. For each test case, it determines if any number in the list appears at least `k` times. If so, it outputs `k - 1`; otherwise, it outputs `n`.

