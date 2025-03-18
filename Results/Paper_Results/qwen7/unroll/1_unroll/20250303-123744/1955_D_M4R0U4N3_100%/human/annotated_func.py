#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 ⋅ 10^5. a is a list of n integers such that 1 ≤ a_i ≤ 10^6. b is a list of m integers such that 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, max_val is 1000000, cnt_b is a list of 1000001 zeros.
    #
    #Explanation: The loop processes multiple test cases. For each test case, it updates the `cnt_b` list based on the input arrays `a` and `b`, calculates the value of `ans`, and then resets `cnt_b` to zero for the next iteration. After all iterations of the loop are completed, the `cnt_b` list is reset to zero for every test case, so it remains a list of 1000001 zeros. The values of `t` and `max_val` remain unchanged as they are not affected by the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes integers t, n, m, k, a (a list of n integers), and b (a list of m integers). For each test case, it counts the number of valid subarrays in a that contain at least k elements also present in b. It prints the count for each test case and resets the count array cnt_b to zero after processing each test case. The function does not return any value but prints the result for each test case.

