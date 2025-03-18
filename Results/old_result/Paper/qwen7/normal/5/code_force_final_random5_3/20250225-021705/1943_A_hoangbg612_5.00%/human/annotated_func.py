#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After the loop executes all iterations, `cur` will be the maximum value in `N` that satisfies the condition `num > cur`, or the second-highest number plus one if the highest number does not satisfy the condition. All values in `M` will be either 1 (if the key is greater than `cur`) or will be the count of occurrences of numbers less than or equal to `cur` in `N`. The sum of all values in `M` will still equal `S`. `i` will be 0 since the loop has completed all its iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer \( n \) and a list \( a \) of \( n \) non-negative integers. It then sorts the list and iterates through it to find the maximum value \( cur \) that meets specific conditions. If no such value exists, it sets \( cur \) to the second-highest number plus one. Finally, it prints the value of \( cur \) for each test case.

