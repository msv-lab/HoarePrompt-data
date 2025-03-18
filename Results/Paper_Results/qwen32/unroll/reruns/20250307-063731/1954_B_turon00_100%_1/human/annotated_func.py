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
        
    #State: For each test case, the output will be the minimum length of any contiguous subarray in `a` that contains all elements of the same value, unless the array `a` consists of a single element or all elements in `a` are the same, in which case the output will be -1. The variable `t` will remain unchanged, and the variables `n`, `a`, `tmp`, `cnt`, and `ans` will not retain their values as they are local to each iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the minimum length of any contiguous subarray within `a` that contains all elements of the same value. If the array consists of a single element or all elements are the same, it returns -1. The function outputs the result for each test case.

