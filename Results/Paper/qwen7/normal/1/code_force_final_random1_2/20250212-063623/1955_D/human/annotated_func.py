#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2⋅10^5. a is a list of n integers such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n. b is a list of m integers such that 1 ≤ b_i ≤ 10^6 for all 1 ≤ i ≤ m. The sum of n over all test cases does not exceed 2⋅10^5, and the sum of m over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: All values in `cnt_b` are 0, `curr` is 0, `ans` retains the value it had after the last iteration of the loop, and `n` and `m` retain their values from the last iteration of the loop.
    #
    #Explanation: After the loop has executed all its iterations, the dictionary `cnt_b` will have been reset for each element in `b_values`, making all its values 0. The variable `curr` will be reset to 0 after the last iteration. The variable `ans` will retain the value it had after the last iteration of the loop, as no further changes are specified for `ans` beyond what was described for the first three iterations. The variables `n` and `m` will retain their values from the last iteration of the loop, as they are not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it compares elements from two lists \(a\) and \(b\). It counts the occurrences of elements in \(b\) and checks if a sliding window of size \(m\) in list \(a\) contains at least \(k\) elements also present in \(b\). The function prints the total count of such windows across all test cases. After processing each test case, it resets the count for elements in \(b\) and keeps track of the current count of matching elements within the sliding window.

