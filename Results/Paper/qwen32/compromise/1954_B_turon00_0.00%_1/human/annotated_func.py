#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n across all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is 0, `n` is the last input integer, `a` is the last list of integers read from the input, `tmp` is the first element of the last `a`, `aa` is a set containing the unique elements from the last `a`, `cnt` is the count of the last sequence of consecutive elements equal to `tmp` in the last `a`, and `ans` is the minimum count of any sequence of consecutive elements equal to `tmp` found during all iterations of the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the minimum length of consecutive sequences of the first element in the list `a`. If all elements in the list are the same, it outputs `-1`. Otherwise, it prints the minimum length of such sequences.

