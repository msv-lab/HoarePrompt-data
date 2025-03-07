#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2⋅10^5. a is a list of n integers where 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n. b is a list of m integers where 1 ≤ b_i ≤ 10^6 for all 1 ≤ i ≤ m. The sum of n over all test cases does not exceed 2⋅10^5, and the sum of m over all test cases does not exceed 2⋅10^5.
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
        
    #State: After all iterations of the loop, `b_values` will be empty, `cnt_b[i]` will be 0 for every `i` from 0 to 1000000, `i` will be equal to `n - m - 1`, `ans` will be incremented by 1 for each iteration where `curr` is greater than or equal to `k`, and `curr` will represent the net count of elements in `a` that are found in `b_values` with valid decremented counts.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, m, k, a (a list of n integers), and b (a list of m integers). For each test case, it counts how many times the condition (the number of elements in `a` that are also in `b` being at least `k`) is met within a sliding window of size `m` across `a`. It then prints the total count of such occurrences across all test cases. After processing, it resets the count arrays and values for the next test case.

