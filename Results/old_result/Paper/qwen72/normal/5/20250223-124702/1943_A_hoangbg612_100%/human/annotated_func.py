#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    T = int(input())
    for _ in range(T):
        S = int(input())
        
        N = list(map(int, input().split()))
        
        N.sort()
        
        cur = -1
        
        M = {}
        
        for num in N:
            if num > cur:
                if num > cur + 1:
                    cur += 1
                    break
                cur = num
                M[cur] = 1
            else:
                M[cur] += 1
        
        if sum([M[k] for k in M.keys()]) == S:
            cur += 1
        
        cnt = []
        
        for k in M.keys():
            if M[k] == 1:
                cnt.append(k)
        
        if len(cnt) >= 2:
            cur = cnt[1]
        
        print(cur)
        
    #State: The value of `cur` is the second smallest unique integer in the list `N` if there are at least two unique integers. If there is only one unique integer or no unique integers, `cur` is the largest integer in the list `N` or `cur` is the only unique integer plus one, respectively. The values of `t`, `n`, `a`, and `T` remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads an integer `S` and a list of integers `N`. It then processes the list `N` to find the second smallest unique integer if there are at least two unique integers. If there is only one unique integer or no unique integers, it returns the largest integer in the list `N` or the only unique integer plus one, respectively. The function prints the result for each test case. The values of `t`, `n`, and `a` remain unchanged.

