#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `T` is an input integer where 1 ≤ T ≤ 2 · 10^4 and must be 0, `N` is a sorted list of integers, `cur` is the largest integer in `N` that is not greater than `cur + 1` at the start of the loop, `M` is a dictionary where the keys are the unique integers in `N` that are not greater than `cur + 1` and the values are the counts of these integers in `N`, and `cnt` is a list containing all the unique integers from `N` that are not greater than `cur + 1` and have a count of 1 in `M`. If the length of `cnt` is at least 2, `cur` is the second smallest unique integer in `cnt` that is not greater than `cur + 1` at the start of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `n` and a list `a` of `n` integers. For each test case, it sorts the list `a`, then iterates through the sorted list to find the largest integer `cur` such that all integers in `a` up to `cur` are unique and consecutive starting from 0. If the sum of the counts of these unique integers equals `n`, it increments `cur` by 1. Finally, it prints the value of `cur`. If there are at least two unique integers in `a` that are consecutive and have a count of 1, `cur` is set to the second smallest of these integers before printing.

