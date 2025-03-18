#State of the program right berfore the function call: For each test case, n and m are integers representing the lengths of arrays a and b respectively, where 1 ≤ n, m ≤ 2·10^5. k is an even integer such that 2 ≤ k ≤ 2·min(n, m). Arrays a and b consist of integers where 1 ≤ a_i, b_j ≤ 10^6 for all valid indices i and j. The total sum of n and m across all test cases does not exceed 4·10^5. The number of test cases, t, satisfies 1 ≤ t ≤ 10^4.
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
        
    #State: The values of `t`, `n`, `m`, `k`, `a`, and `b` remain unchanged from their initial state.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integer arrays `a` and `b`, and an even integer `k`. For each test case, it checks if at least half of the first `k` elements in both arrays `a` and `b` are less than or equal to `k`. It then prints 'YES' if both conditions are met, otherwise 'NO'.

