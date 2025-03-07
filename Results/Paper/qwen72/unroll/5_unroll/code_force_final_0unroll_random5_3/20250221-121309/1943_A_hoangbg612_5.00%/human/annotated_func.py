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
        
        for i in range(cur):
            if M[i] <= i:
                cur = i
                break
        
        print(cur)
        
    #State: The variable `cur` will hold the largest integer such that all integers from 0 to `cur` are present in the list `N` and their counts in `M` are at least equal to their values. The dictionary `M` will contain the counts of these integers. The list `N` will be sorted. The variables `t`, `n`, and `a` will remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads an integer `S` and a list of integers `N`. It then sorts the list `N` and processes it to determine the largest integer `cur` such that all integers from 0 to `cur` are present in `N` and their counts in `N` are at least equal to their values. The function prints `cur` for each test case. The variables `t`, `n`, and `a` are not modified by the function.

