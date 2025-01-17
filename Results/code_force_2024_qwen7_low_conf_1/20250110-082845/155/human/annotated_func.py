#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and n ≤ m ≤ 10^9, and a is a list of n integers such that 1 ≤ a_i ≤ m and all a_i's are pairwise distinct.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\); `a` is a sorted list of `n` integers such that \(1 \leq a_i \leq m\) and all `a_i`'s are pairwise distinct; `MOD` is \(10^9 + 7\); `inv_2` is \(500000000\); `inv_3` is \(3^{(10^9 + 6)} \mod (10^9 + 7)\); `tc` is the number of times the loop has executed; `m` is the last integer read from input; `inv_m` is \(m^{(MOD - 2)} \mod MOD\); `ans` is the cumulative sum of \((dist \times inv_m \mod MOD) \times (n \times inv_2 \mod MOD) \times ((m \times m - dist \times dist) \times inv_3 \mod MOD) \mod MOD\) for all iterations from 0 to `n-1`, modulo `MOD`; `n` is the last integer read from input; `dist` is \((a[(i + 1) \% n] - a[i]) \% m\), `prob_last` is \((dist \times inv_m) \% MOD\), `expected_getting_moved` is \(n \times inv_2 \% MOD\), `expected_time` is \(((m \times m - dist \times dist) \times inv_3) \mod MOD\); `ans` is within the range 0 to `MOD-1`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers `n` and `m`, and a list `a` of `n` distinct integers. It calculates and prints a cumulative value `ans` based on specific computations involving these inputs. Specifically, for each element in the list `a`, it computes a distance between consecutive elements (considering circular order), calculates probabilities and expected values related to these distances, and sums up these values modulo \(10^9 + 7\). The final `ans` is the sum of these computations for all test cases and is printed at the end. Potential edge cases include handling the modulo arithmetic correctly and ensuring that the list `a` is indeed sorted and contains distinct integers. The function does not handle invalid input directly; it assumes valid input as per the problem constraints.

