#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4, a is a list of n integers where 1 ≤ a_i ≤ 10^4, and s is a string of n characters, each being either 'L' or 'R'. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop has completed all iterations. `t` is an integer where 1 ≤ t ≤ 10^4, `_` is a placeholder for the loop iteration, `arr` is a list of `n` integers provided by the user input, `n` is an integer provided by the user input and must be greater than 1, `m` is an integer provided by the user input, `s` is a list of characters from the user input, `res` is a list of `n` integers where each element at index `k` (0 ≤ k < n) is `ans % m % MOD` after the corresponding iteration, `ans` is the final value after all updates based on the characters in `s`, `i` is the last element in `arr`, `c` is `n`, `l` is the number of 'L' characters in `s`, `r` is `n - 1 -` the number of 'R' characters in `s`, `k` is `n - 1`, and `MOD` remains unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n` and `m`, a list `arr` of `n` integers, and a string `s` of `n` characters ('L' or 'R'). For each test case, it calculates a product of the integers in `arr`, then iteratively updates this product based on the characters in `s`. The final result is a list `res` of `n` integers, where each element at index `k` (0 ≤ k < n) is the updated product modulo `m` and then modulo `10^9 + 6`. The function prints the list `res` for each test case. After the function concludes, the state of the program is such that all test cases have been processed, and the list `res` has been printed for each test case. The variables `t`, `n`, `m`, `arr`, `s`, and `MOD` retain their initial or updated values as per the function's execution, but the function does not return any value.

