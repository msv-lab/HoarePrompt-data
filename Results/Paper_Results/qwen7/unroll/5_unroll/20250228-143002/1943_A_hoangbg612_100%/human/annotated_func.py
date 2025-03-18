#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: T is an input integer, and it is a positive integer such that 1 ≤ T ≤ 2⋅10^4. After all the executions of the loop have finished, for each input case, the variable `cur` holds the second smallest number that appears exactly once in the sorted list `N`, or the smallest number that appears more than once if no unique second smallest number exists.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( T \) (number of test cases), an integer \( N \) (length of the array), and an array of \( N \) integers. For each test case, it sorts the array and then identifies the second smallest number that appears exactly once in the sorted array. If no such number exists, it finds the smallest number that appears more than once. The function outputs the identified number for each test case.

