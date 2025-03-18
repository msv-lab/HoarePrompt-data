#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers where 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5; a is a list of n integers where 1 ≤ a_i ≤ 10^6; b is a list of m integers where 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations of the loop, `t` is decremented by the number of test cases processed, `n`, `m`, and `k` retain their last assigned values from the final test case, `a` and `b` retain their last assigned lists from the final test case, `b_values` is a set containing the unique elements from the final `b`, `cnt_b` is a list of length 1000001 with all elements in `b_values` set to 0, `ans` is the total number of valid subarrays found across all test cases, `curr` is the number of elements in the final sliding window of size `m` that are in `b_values` and have a non-negative count in `cnt_b`.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by integers `n`, `m`, and `k`, and two lists of integers `a` and `b`. For each test case, it counts the number of contiguous subarrays of length `m` in `a` that contain at least `k` elements present in `b` and prints this count. After processing all test cases, the function has no return value, but it has printed the results for each test case. The internal state of the function, including variables like `cnt_b`, `b_values`, `ans`, and `curr`, is reset or updated appropriately for each new test case.

