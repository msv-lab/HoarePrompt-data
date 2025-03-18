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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, max_val is 1000000, cnt_b is a list of 1000001 zeros.
    #
    #Explanation: The given code processes multiple test cases within the loop. For each test case, it updates the `cnt_b` list based on the input values but resets `cnt_b` to all zeros at the end of each test case. Therefore, after all iterations of the loop, the `cnt_b` list remains a list of 1000001 zeros.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it counts the occurrences of elements in list `b` within list `a`. It then checks if the count of common elements between `a` and `b` meets or exceeds a specified threshold `k`. If so, it increments the answer counter. After processing all test cases, it prints the total count of such instances and resets the count array `cnt_b` to zero for the next iteration. The function ultimately ensures that the count array `cnt_b` is reset to all zeros after processing all test cases.

