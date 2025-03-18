#State of the program right berfore the function call: t is an integer such that 1 <= t <= 2 * 10^4, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: After the loop executes all the iterations, the value of `cur` will be the largest integer such that the number of occurrences of each integer from 0 to `cur` in the list `N` is at most equal to the integer itself. The values of `t`, `n`, `a`, and `T` remain unchanged.
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads an integer `S` and a list of integers `N`. It then sorts the list `N` and determines the largest integer `cur` such that the number of occurrences of each integer from 0 to `cur` in the list `N` is at most equal to the integer itself. Finally, it prints the value of `cur` for each test case. The function does not return any value. The values of `t`, `n`, and `a` (as described in the initial state) are not directly modified by the function.

