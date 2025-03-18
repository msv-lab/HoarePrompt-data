#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n <= 2*10^5 and 1 <= m <= 10^4. a is a list of n integers such that 1 <= a_i <= 10^4 for each i. s is a string of length n consisting of the characters 'L' and 'R'. The sum of all n values across all test cases does not exceed 2*10^5.
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
        
    #State: For each test case, `res` is a list of `n` integers where the first `n-1` elements are the results of the operations described in the loop, and the last element is `0`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers and a corresponding string of directions ('L' or 'R'). It calculates a series of values based on these inputs and prints a list of results for each test case.

