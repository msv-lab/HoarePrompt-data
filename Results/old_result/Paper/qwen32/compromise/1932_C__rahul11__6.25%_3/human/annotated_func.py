#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4. a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^4. s is a string of length n consisting of characters 'L' and 'R'. The sum of all n values across all test cases does not exceed 2·10^5.
def func():
    MOD = 10 ** 9 + 6
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        s = list(input())
        
        res = [0] * n
        
        ans = 1
        
        for i in arr:
            ans *= i
        
        res[0] = ans % m % MOD
        
        c = 1
        
        l = 0
        
        r = n - 1
        
        for k in range(n - 1):
            if s[k] == 'L':
                ans = ans // arr[l] % MOD
                res[c] = ans % m % MOD
                l += 1
            else:
                ans = ans // arr[r] % MOD
                res[c] = ans % m % MOD
                r -= 1
            c += 1
        
        print(*res)
        
    #State: `res` is a list of `n` integers where each element is the result of the division operations modulo `m` and `MOD`, `ans` is `1`, `c` is `n`, `l` is equal to `r`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n` and `m`, a list `a` of `n` integers, and a string `s` of length `n` containing 'L' and 'R'. For each test case, it calculates a list `res` of `n` integers where each element is the result of a series of division operations on the product of all elements in `a`, modulo `m` and `10^9 + 6`, based on the directions specified in `s`. It then prints the list `res` for each test case.

