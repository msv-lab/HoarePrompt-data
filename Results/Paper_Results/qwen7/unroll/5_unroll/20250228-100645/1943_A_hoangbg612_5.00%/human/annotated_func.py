#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), followed by a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. It is also guaranteed that the sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: T is an integer input, 1 ≤ T ≤ 2 ⋅ 10^4, and for each input T, the output is the maximum value of `cur` after processing all the lists `N`. The value of `cur` is determined based on the conditions within the loop, and it represents the largest number that satisfies the given constraints for each list `N`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n followed by a list of n integers. For each test case, it sorts the list of integers and then determines the maximum value of `cur` based on specific conditions. Finally, it prints the maximum value of `cur` for each test case.

