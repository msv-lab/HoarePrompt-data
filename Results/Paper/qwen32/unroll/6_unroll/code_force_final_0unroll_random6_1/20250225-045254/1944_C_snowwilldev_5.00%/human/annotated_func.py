#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 2 · 10^5, and a list of n integers a where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: - The variable `t` (the number of test cases) remains unchanged.
    #- The variables `N`, `a`, and `cnt` will be in their final state corresponding to the last test case processed.
    #- The variable `t` inside the loop (which counts unique elements appearing exactly once) will be in its final state for the last test case.
    #- The loop will have printed the index `i` for the last test case where the condition `t >= 2` or `cnt[i] == 0` is met.
    #
    #Given the nature of the loop, the exact value of the variables `N`, `a`, and `cnt` for the last test case will depend on the input data for that test case. However, the format for the output state should reflect the state of the variables after the last test case is processed.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` and a list of `n` integers `a`. It then determines and prints the smallest index `i` such that either the count of `i` in the list `a` is zero or at least two unique elements in `a` appear exactly once.

