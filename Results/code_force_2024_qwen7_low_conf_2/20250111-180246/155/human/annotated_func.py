#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, for each test case, n and m are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and n ≤ m ≤ 10^9, and a is a list of n integers such that 1 ≤ a_i ≤ m and all a_i's are pairwise distinct.
def func():
    MOD = 10 ** 9 + 7
    inv_2 = (MOD + 1) // 2
    inv_3 = pow(3, MOD - 2, MOD)
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        
        a = sorted(list(map(int, input().split())))
        
        inv_m = pow(m, MOD - 2, MOD)
        
        ans = 0
        
        for i in range(n):
            dist = (a[(i + 1) % n] - a[i]) % m
            prob_last = dist * inv_m % MOD
            expected_getting_moved = n * inv_2 % MOD
            expected_time = (m * m - dist * dist) * inv_3 % MOD
            ans += prob_last * expected_getting_moved % MOD * expected_time % MOD
            ans %= MOD
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `tc` is the number of iterations the loop has executed, `ans` is the accumulated sum of `prob_last * expected_getting_moved * expected_time` for all `i` from 0 to `n-1`, modulo `MOD`. If `tc` is 0, `ans` is 0. `n` and `m` are input integers, `a` is a sorted list of integers obtained from the input, `inv_m` is `m` raised to the power of `MOD - 2` modulo `MOD`.
#Overall this is what the function does:The function processes a series of test cases defined by the number of test cases \(t\), the size of a list \(n\), the upper limit \(m\), and a list of integers \(a\). For each test case, it calculates and prints a value based on the sorted list \(a\), the values of \(n\) and \(m\), and predefined constants such as \(inv_2\) and \(inv_3\). The final output for each test case is the result of a complex computation involving distances between elements in the list \(a\), probabilities, and expected times, all taken modulo \(10^9 + 7\). The function ensures that \(t\) is within the range \(1 \leq t \leq 10^4\). If \(t\) is outside this range, it does not process any test cases and behaves as though no test cases were provided. The function does not return a value; instead, it prints the result for each test case directly.

