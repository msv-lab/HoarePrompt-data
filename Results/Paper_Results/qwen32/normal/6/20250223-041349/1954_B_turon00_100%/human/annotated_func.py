#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n across all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is 0, `n` is the last input integer, `a` is the last input list of integers, `tmp` is the first element of the last `a`, `cnt` is the length of the last contiguous sequence of elements equal to `tmp` in the last `a`, `ans` is the minimum length of contiguous sequences of equal elements found across all iterations of the loop. If `n` is 1 or `ans` equals `n`, the output for that iteration is `-1`; otherwise, it is `ans`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the minimum length of contiguous sequences of equal elements in the list `a`. If the list consists of a single element or if the entire list is a single contiguous sequence, it outputs `-1`. Otherwise, it outputs the minimum length of such sequences.

