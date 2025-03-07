#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: T is an input integer where 1 ≤ T ≤ 2⋅10^4. For each test case, the variable `cur` is set to the second smallest number in the sorted list `N` if there are at least two numbers that appear exactly once in the list `N`. If no such number exists, `cur` remains -1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \) and a list of \( n \) non-negative integers. For each test case, it sorts the list and then identifies the second smallest number that appears exactly once in the list. If no such number exists, it sets the result to -1. Finally, it prints the result for each test case.

