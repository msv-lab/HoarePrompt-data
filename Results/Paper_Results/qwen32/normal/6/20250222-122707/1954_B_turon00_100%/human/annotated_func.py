#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n over all test cases does not exceed 3 * 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        if n == 1 or ans == n:
            print(-1)
        else:
            print(ans)
        
    #State: The output state after all iterations is a series of `t` printed values, where each value is either `-1` if `n` is 1 or all elements in `a` are the same, or the minimum length of consecutive elements in `a` that are equal.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the minimum length of consecutive equal elements in the list `a`. If all elements in `a` are the same or `n` is 1, it returns `-1`. Otherwise, it returns the minimum length of such consecutive elements.

