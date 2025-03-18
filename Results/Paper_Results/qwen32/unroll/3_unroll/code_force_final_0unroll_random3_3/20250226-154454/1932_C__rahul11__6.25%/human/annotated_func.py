#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4. a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^4. s is a string of length n consisting only of the characters 'L' and 'R'. The sum of all n across all test cases does not exceed 2·10^5.
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
        
    #State: For each test case, `res` is a list of length `n` where each element is the product of the remaining elements in `arr` after processing the corresponding character in `s`, taken modulo `m` and `MOD`. The other variables (`t`, `n`, `m`, `arr`, `s`, `MOD`) remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a corresponding string of directions ('L' and 'R'). For each test case, it calculates a list where each element represents the product of the remaining integers in the list after sequentially removing elements based on the directions, modulo two given values. The result for each test case is printed as a space-separated list of integers.

