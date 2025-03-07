#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), an integer representing the size of the array a, followed by a line containing n integers a_1, a_2, \ldots, a_n where 0 ≤ a_i < n. It is also given that the sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `T` is an integer obtained from `int(input())`, and it is a positive integer such that 1 ≤ `T` ≤ 2⋅10^4. For each value of `S` and list `N`, after executing the loop, `cur` is the maximum number such that there are at least `cur+1` numbers in `N` that are greater than or equal to `cur`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` representing the size of an array `a`, followed by `n` integers `a_1, a_2, ..., a_n` where each `a_i` is in the range [0, n-1]. For each test case, it sorts the array, then determines the maximum number `cur` such that there are at least `cur+1` numbers in the array that are greater than or equal to `cur`. If the sum of counts of these numbers equals `S` (an integer input for each test case), it increments `cur` by 1. Finally, it prints the maximum value of `cur` found for each test case.

