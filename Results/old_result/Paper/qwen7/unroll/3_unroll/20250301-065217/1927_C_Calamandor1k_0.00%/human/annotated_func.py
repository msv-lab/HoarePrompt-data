#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^5; k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m); a is a list of n integers such that 1 ≤ a_i ≤ 10^6; b is a list of m integers such that 1 ≤ b_j ≤ 10^6; the sum of values n and m over all test cases does not exceed 4⋅10^5.
def func():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        len_a, len_b = len(a), len(b)
        
        count_a, count_b = 0, 0
        
        d = k // 2
        
        for i in range(max(len_a, len_b)):
            if len_a > i + 1:
                if a[i] <= k:
                    count_a += 1
            if len_b > i + 1:
                if b[i] <= k:
                    count_b += 1
        
        print('YES' if count_a >= d and count_b >= d else 'NO')
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each value of t, there are three lists a and b, and an integer k. After executing the loop, the values of a, b, and k are unchanged. The variable d is set to k // 2, and two counters count_a and count_b are updated based on the conditions in the loop. The result 'YES' or 'NO' is printed for each iteration, but the final state does not store these results; only the initial and final values of t, a, b, and k remain relevant.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers t, n, m, k, a (a list of n integers), and b (a list of m integers). For each test case, it counts how many elements in lists a and b are less than or equal to k/2. If both counts meet or exceed half of k, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

