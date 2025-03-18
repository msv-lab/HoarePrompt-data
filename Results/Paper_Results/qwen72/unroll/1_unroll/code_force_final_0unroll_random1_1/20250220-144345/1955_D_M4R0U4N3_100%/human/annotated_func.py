#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, and b is a list of m integers where each integer b_i satisfies 1 <= b_i <= 10^6.
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
        
    #State: t is an integer such that 1 <= t <= 10^4, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, b is a list of m integers where each integer b_i satisfies 1 <= b_i <= 10^6, max_val is 1000000, cnt_b is a list of 1000001 zeros.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads three integers `n`, `m`, and `k`, followed by two lists of integers `a` and `b`. It then counts the number of contiguous subarrays of length `m` in `a` where at least `k` elements are present in `b` and prints this count. After processing all test cases, the function resets the count array `cnt_b` to a list of 1000001 zeros. The function does not return any value.

