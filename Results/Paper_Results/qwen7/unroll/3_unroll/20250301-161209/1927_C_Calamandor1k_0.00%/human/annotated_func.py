#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^5, and k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m). Additionally, the sum of values n and m over all test cases in a test does not exceed 4⋅10^5. Arrays a and b contain integers such that 1 ≤ a_i, b_j ≤ 10^6 for all i and j.
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
        
    #State: Output State: The output state will consist of "YES" or "NO" printed for each iteration of the loop based on the conditions specified within the loop. For each test case (determined by the value of `t`), the program checks two lists `a` and `b` against the threshold `k` and prints "YES" if at least half of the elements in both lists are less than or equal to `k`, otherwise it prints "NO".
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers t, n, m, k, and two arrays a and b. It then checks if at least half of the elements in both arrays a and b are less than or equal to the integer k. If this condition is met for both arrays, it prints "YES"; otherwise, it prints "NO". This process is repeated for each of the t test cases.

