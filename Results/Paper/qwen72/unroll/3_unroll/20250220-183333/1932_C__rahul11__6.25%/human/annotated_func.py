#State of the program right berfore the function call: The function processes multiple test cases. For each test case, n and m are integers where 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4, a is a list of n integers where 1 ≤ a_i ≤ 10^4, and s is a string of n characters, each being either 'L' or 'R'. The sum of n values across all test cases does not exceed 2·10^5.
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
        
    #State: The loop processes each test case and prints the resulting list `res` for each test case. After all iterations of the loop, the variables `n`, `m`, `arr`, `s`, `MOD`, and the test cases themselves remain unchanged. The variables `res`, `ans`, `c`, `l`, and `r` are reset and recalculated for each new test case. For each test case, `res` is a list of `n` integers where `res[0]` is the product of all elements in `arr` modulo `m` and then modulo `MOD`, and subsequent elements in `res` are the product of the remaining elements in `arr` after removing elements from the left or right based on the characters in `s`, all modulo `m` and then modulo `MOD`.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it takes integers `n` and `m`, a list of `n` integers `arr`, and a string `s` of `n` characters (each being 'L' or 'R'). It calculates a list `res` of `n` integers where `res[0]` is the product of all elements in `arr` modulo `m` and then modulo `10^9 + 6`. For subsequent elements in `res`, it updates the product by dividing it by the current element from the left or right of `arr` based on the corresponding character in `s`, and then takes the result modulo `m` and `10^9 + 6`. After processing each test case, it prints the list `res`. The function does not return any value, and the variables `n`, `m`, `arr`, `s`, and `MOD` remain unchanged across test cases.

