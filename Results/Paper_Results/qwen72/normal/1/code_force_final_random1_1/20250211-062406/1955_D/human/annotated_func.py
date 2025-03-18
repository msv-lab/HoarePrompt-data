#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers where 1 ≤ k ≤ m ≤ n ≤ 2 × 10^5; a is a list of n integers where 1 ≤ a_i ≤ 10^6; b is a list of m integers where 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 × 10^5, and the sum of m over all test cases does not exceed 2 × 10^5.
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
        
    #State: After the loop executes all iterations, the variable `ans` contains the total number of valid subarrays of length `m` in `a` where at least `k` elements match elements in `b` and their counts in `cnt_b` are non-negative. The list `cnt_b` is reset to zero for all elements in `b_values`. The lists `a` and `b` remain unchanged, and the variables `n`, `m`, and `k` retain their initial values. The variable `curr` is the final count of elements in the last subarray of `a` that are in `b_values` and have non-negative counts in `cnt_b`.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it takes integers `n`, `m`, and `k`, and two lists `a` and `b` as inputs. It calculates the number of subarrays of length `m` in `a` where at least `k` elements match elements in `b` and their counts in `cnt_b` are non-negative. The function prints the result for each test case. After processing all test cases, the lists `a` and `b` remain unchanged, and the variables `n`, `m`, and `k` retain their initial values. The list `cnt_b` is reset to zero for all elements in `b_values`.

