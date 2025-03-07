#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n <= 2*10^5 and 1 <= m <= 10^4. The array a contains n integers where each integer a_i satisfies 1 <= a_i <= 10^4. The string s consists of n characters, each of which is either 'L' or 'R'. The sum of n across all test cases does not exceed 2*10^5.
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
        
    #State: For each test case, `res` is a list of `n` elements where each element is the value of `ans % m % MOD` after each division, `ans` is the final value of the product of all elements in `arr` divided by the appropriate elements in `arr` as specified by `s`, modulo `MOD`, `c` is `n`, `l` and `r` are final values depending on the sequence of 'L's and non-'L's in `s`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates a sequence of values based on the product of an array of integers, divided by elements specified by a sequence of 'L' and 'R' characters, and returns these values modulo a given number.

