#State of the program right berfore the function call: t is an integer where 1 <= t <= 2 * 10^4, n is an integer where 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The value of `cur` is the largest integer such that all integers from 0 to `cur` are present in the list `N` and the sum of their counts in `M` is equal to `S`. The variable `M` is a dictionary that maps each integer from 0 to `cur` to its count in the list `N`. The variables `t`, `n`, `a`, and `T` remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from standard input. For each test case, it reads an integer `S` and a list of integers `N`. It then processes the list `N` to find the largest integer `cur` such that all integers from 0 to `cur` are present in `N` and the sum of their counts in `N` is equal to `S`. The function prints this value `cur` for each test case. The function does not return any value. The state of the program after the function concludes is that the value of `cur` is the largest integer satisfying the above conditions, and the variables `t`, `n`, and `a` remain unchanged.

