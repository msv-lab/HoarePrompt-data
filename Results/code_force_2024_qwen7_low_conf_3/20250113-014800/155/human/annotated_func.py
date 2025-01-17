#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers satisfying 1 ≤ n ≤ 3⋅10^5 and n ≤ m ≤ 10^9. The array a contains n distinct integers such that 1 ≤ a_i ≤ m for each 1 ≤ i ≤ n.
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
        
    #State of the program after the  for loop has been executed: `ans` is the sum of the product of `prob_last`, `expected_getting_moved`, and `expected_time` for each iteration, all taken modulo `MOD`; `i` is `n`; `n` is the value of the first input integer; `m` is the value of the second input integer; `a` is a sorted list of integers; `inv_m` is the modular inverse of `m` modulo `MOD`; the loop will execute at least `tc` times if `tc` is a positive integer, otherwise `ans` remains `0`.
#Overall this is what the function does:The function processes a series of test cases, each containing a positive integer `tc` representing the number of test cases, followed by pairs of integers `n` and `m`, and an array `a` of `n` distinct integers. For each test case, it calculates a value `ans` based on specific mathematical operations involving the given integers and their properties. The operations include calculating distances, probabilities, and expected values, all taken modulo `10^9 + 7`. The final `ans` for each test case is printed. If no test cases are provided (`tc` is zero), `ans` remains `0`.

The function performs the following steps:
1. Reads the number of test cases `tc`.
2. For each test case, reads `n` and `m`.
3. Reads the array `a` of `n` distinct integers.
4. Calculates the modular inverse of `m` modulo `10^9 + 7`.
5. Iterates over the elements of `a` to compute `dist`, `prob_last`, `expected_getting_moved`, and `expected_time`.
6. Updates `ans` with the product of `prob_last`, `expected_getting_moved`, and `expected_time`, all taken modulo `10^9 + 7`.
7. Prints the final `ans` for each test case.

Potential edge cases:
- If `tc` is `0`, no test cases are processed, and `ans` remains `0`.
- If `n` is `0`, the array `a` will be empty, and the loop will not execute, leaving `ans` unchanged.
- If `m` is `1`, the distance calculations will result in `0`, and `prob_last` will also be `0`, making the contributions to `ans` negligible.
- If `a` contains duplicate integers, the function will treat them as distinct due to the requirement that `a` contains `n` distinct integers.

