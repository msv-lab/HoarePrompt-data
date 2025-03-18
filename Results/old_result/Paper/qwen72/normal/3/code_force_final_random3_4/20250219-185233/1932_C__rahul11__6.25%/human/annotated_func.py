#State of the program right berfore the function call: The function `func` is expected to be called within a program that processes multiple test cases. Each test case consists of an integer n (1 ≤ n ≤ 2·10^5) representing the length of the array a, an integer m (1 ≤ m ≤ 10^4) for the modulus operation, a list of n integers a (1 ≤ a_i ≤ 10^4) representing the elements of the array, and a string s of length n consisting of characters 'L' and 'R'. The total sum of n across all test cases does not exceed 2·10^5.
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
        
    #State: `n` remains unchanged, `k` is `n - 1`, `c` is `n`, `ans` is the final value of `ans` after all updates, `res` is a list of length `n` where each element is `ans % m % MOD` after each iteration, `l` is the number of 'L' characters in `s`, and `r` is `n - 1 - l`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n`, an integer `m`, a list of `n` integers `a`, and a string `s` of length `n` consisting of characters 'L' and 'R'. For each test case, it calculates the product of all elements in `a`, then iteratively updates this product by dividing it by elements from either the start or the end of `a` based on the characters in `s`. The function prints a list of length `n` where each element is the updated product modulo `m` and further modulo `10^9 + 6` after each iteration. The function does not return any value; it only prints the results.

