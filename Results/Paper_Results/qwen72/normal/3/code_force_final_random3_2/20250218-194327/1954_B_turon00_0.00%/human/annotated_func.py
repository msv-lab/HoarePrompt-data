#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of integers of length n where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a list of integers of length `n` where 1 ≤ a_i ≤ n, `a` is guaranteed to be beautiful, `i` is `n-1`, `tmp` is equal to `a[0]`, `aa` is a set containing the unique elements from the list `a`, if the length of `aa` is 1, then `ans` is `n` and `cnt` is `n`, if the length of `aa` is greater than 1, then `ans` is the minimum of its current value and `cnt`, and `cnt` remains the same.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then processes the list `a` to find the minimum length of consecutive segments of the same integer, excluding segments of the entire list if all elements are identical. If all elements in `a` are the same, it prints `-1`. Otherwise, it prints the minimum length of such segments. After processing all test cases, `t` is 0, and the function has no return value.

