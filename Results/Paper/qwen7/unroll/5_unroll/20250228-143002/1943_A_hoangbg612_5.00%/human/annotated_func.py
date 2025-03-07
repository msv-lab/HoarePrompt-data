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
        
        for i in range(cur):
            if M[i] <= i:
                cur = i
                break
        
        print(cur)
        
    #State: Output State: T is an input integer such that 1 ≤ T ≤ 2⋅10^4. For each input, the variable cur is set to the maximum value such that there are no gaps in the sequence from 0 to cur-1, or the largest number that satisfies the conditions within the given constraints.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer `T` (1 ≤ T ≤ 20,000) representing the number of test cases. For each test case, it takes another positive integer `S` and a list `N` of `n` non-negative integers (1 ≤ n ≤ 200,000, 0 ≤ a_i < n). It sorts the list `N` and then determines the maximum value `cur` such that there are no gaps in the sequence from 0 to `cur-1`. If no such `cur` exists, it sets `cur` to the largest number satisfying the conditions. Finally, it prints the value of `cur` for each test case.

