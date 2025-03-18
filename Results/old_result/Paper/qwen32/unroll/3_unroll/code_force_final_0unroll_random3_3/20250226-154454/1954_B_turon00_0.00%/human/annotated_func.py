#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, for each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n, the array a is beautiful, and the sum of n over all test cases does not exceed 3 * 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: For each test case, the output is the minimum length of any contiguous subarray that contains only the first element of the array `a`. If all elements in the array are the same, the output is `-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the minimum length of any contiguous subarray that contains only the first element of the array `a`. If all elements in the array are the same, it outputs `-1`.

