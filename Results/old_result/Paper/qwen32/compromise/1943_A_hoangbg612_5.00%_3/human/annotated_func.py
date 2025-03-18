#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a. The array a contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The final value of `cur` will be the smallest integer `i` such that `M[i] <= i`, if such an `i` exists after all iterations. If no such `i` exists after all iterations, `cur` remains unchanged from its initial value for the last iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `S` and an array `N` of integers. It processes the array to determine the smallest integer `i` such that the count of `i` in the array is less than or equal to `i`. If no such `i` exists, it returns the next integer after the largest number in the array that satisfies the condition. The function prints this integer for each test case.

