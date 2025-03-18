#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n across all test cases does not exceed 3 * 10^5.
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
        
    #State: For each test case, the output will be the length of the shortest contiguous subarray in `a` that contains all elements of the same value, or -1 if all elements in `a` are the same or if `n` is 1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the length of the shortest contiguous subarray in `a` that contains all elements of the same value, or returns -1 if all elements in `a` are the same or if `n` is 1.

