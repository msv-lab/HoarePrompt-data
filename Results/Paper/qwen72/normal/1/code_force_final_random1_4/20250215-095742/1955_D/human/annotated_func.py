#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5, representing the lengths of arrays a and b, and the required number of matching elements. a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: All elements in `b_values` have been processed, `cnt_b[i]` is 0 for all `i` in `b_values`, `n` is greater than or equal to `m`, `m` remains the same as the input integer, `k` remains the same as the input integer, `a` and `b` lists remain unchanged, and `ans` contains the number of valid subarrays of `a` of length `m` that contain at least `k` elements present in `b`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and two lists `a` and `b`. It calculates and prints the number of subarrays of `a` of length `m` that contain at least `k` elements present in `b`. The function does not return any value; instead, it prints the result for each test case. After processing all test cases, the lists `a` and `b` remain unchanged, and the counters for elements in `b` are reset to zero.

