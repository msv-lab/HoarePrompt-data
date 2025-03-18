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
        
    #State: After all iterations of the loop, the value of `cur` is printed for each test case. The values of `t`, `n`, `a`, and `T` remain unchanged. The dictionary `M` will contain the counts of unique elements in the list `N` that are used to determine the final value of `cur`. The list `N` will be sorted.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `S` and a list of integers `N`. It then processes the list `N` to determine the largest integer `cur` such that for all integers `i` in the range `[0, cur)`, the count of `i` in `N` is greater than `i`. The function prints the value of `cur` for each test case. The values of `T`, `S`, and `N` are not retained after each test case, and the function does not return any value.

