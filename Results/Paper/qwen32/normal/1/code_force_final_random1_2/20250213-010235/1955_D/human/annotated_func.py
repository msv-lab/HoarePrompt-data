#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 × 10^5. a is a list of n integers where each element satisfies 1 ≤ a_i ≤ 10^6. b is a list of m integers where each element satisfies 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 × 10^5, and the sum of m over all test cases does not exceed 2 × 10^5.
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
        
    #State: `cnt_b` is a list of 1,000,001 zeros, `ans` holds the total number of times `curr` was greater than or equal to `k` across all test cases, and all other variables (`n`, `m`, `k`, `a`, `b`, and `b_values`) reflect the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers and two additional integers. For each test case, it determines how many contiguous subarrays of length `m` in the first list contain at least `k` elements that also appear in the second list. It then prints the count of such subarrays for each test case.

