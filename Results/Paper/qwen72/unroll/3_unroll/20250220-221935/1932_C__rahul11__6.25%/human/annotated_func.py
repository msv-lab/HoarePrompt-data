#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4, a is a list of n integers where 1 ≤ a_i ≤ 10^4, and s is a string of length n consisting only of the characters 'L' and 'R'. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: For each test case, the loop computes a list `res` of length `n` where `res[0]` is the product of all elements in `arr` modulo `m` and then modulo `MOD`. For each subsequent index `k` in `res`, if `s[k-1]` is 'L', `res[k]` is the product of the remaining elements in `arr` from the left side (excluding the first `k` elements) modulo `m` and then modulo `MOD`. If `s[k-1]` is 'R', `res[k]` is the product of the remaining elements in `arr` from the right side (excluding the last `k` elements) modulo `m` and then modulo `MOD`. The loop then prints the list `res` for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n` and `m`, a list `arr` of `n` integers, and a string `s` of length `n` consisting only of the characters 'L' and 'R'. For each test case, it computes a list `res` of length `n` where `res[0]` is the product of all elements in `arr` modulo `m` and then modulo `10^9 + 6`. For each subsequent index `k` in `res`, if `s[k-1]` is 'L', `res[k]` is the product of the remaining elements in `arr` from the left side (excluding the first `k` elements) modulo `m` and then modulo `10^9 + 6`. If `s[k-1]` is 'R', `res[k]` is the product of the remaining elements in `arr` from the right side (excluding the last `k` elements) modulo `m` and then modulo `10^9 + 6`. The function prints the list `res` for each test case.

