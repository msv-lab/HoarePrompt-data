#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. The sum of n over all test cases does not exceed 3 \cdot 10^5.
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4. For each `i` from 0 to `t-1`, `n` is the number of elements in the list `a`, where `a` is a list of integers. After executing the loop, `ans` is the minimum length of consecutive segments with the same integer in each list `a`. If `n` is 1 or `ans` equals `n`, then `-1` is printed; otherwise, `ans` is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then determines the minimum length of consecutive segments with the same integer in the list `a`. If the list has only one element or the minimum segment length equals the list size, it prints `-1`; otherwise, it prints the minimum segment length.

