#State of the program right berfore the function call: The function `func` is not properly defined for the given problem. The function should accept parameters for the number of test cases, the lengths of arrays `a` and `b`, the required number of matching elements `k`, and the arrays `a` and `b` themselves.
def func():
    max_val = 1000000
    cnt_b = [0] * (max_val + 1)
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        for i in range(m):
            cnt_b[b[i]] += 1
        
        b_values = set(b)
        
        ans = 0
        
        curr = 0
        
        for i in range(m):
            if a[i] in b_values:
                cnt_b[a[i]] -= 1
                if cnt_b[a[i]] >= 0:
                    curr += 1
        
        if curr >= k:
            ans += 1
        
        for i in range(n - m):
            if a[i] in b_values:
                cnt_b[a[i]] += 1
                if cnt_b[a[i]] > 0:
                    curr -= 1
            if a[i + m] in b_values:
                cnt_b[a[i + m]] -= 1
                if cnt_b[a[i + m]] >= 0:
                    curr += 1
            if curr >= k:
                ans += 1
        
        print(ans)
        
        for i in b_values:
            cnt_b[i] = 0
        
    #State: `cnt_b` is a list of 1000001 zeros, `max_val` is 1000000, and `ans` is the number of valid subarrays of length `m` in `a` where at least `k` elements are in `b` and have not been counted more than once.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the lengths of two arrays `a` and `b`, the required number of matching elements `k`, and the arrays themselves. It then counts the number of subarrays of length `m` in `a` where at least `k` elements match elements in `b` and have not been counted more than once. The function prints the count of such valid subarrays for each test case. After processing all test cases, `cnt_b` is reset to a list of 1000001 zeros, `max_val` remains 1000000, and no value is returned.

