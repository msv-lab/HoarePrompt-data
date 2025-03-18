#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^4. s is a string of length n consisting of the characters 'L' and 'R'. The sum of all n across all test cases does not exceed 2·10^5.
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
        
    #State: For each test case, the output is a list `res` of length `n` where each element is the result of the computations described above, printed in a single line. The state of other variables like `t`, `n`, `m`, `arr`, `s`, `ans`, `c`, `l`, `r` does not need to be specified as they are not part of the output.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a corresponding string of 'L' and 'R' characters. For each test case, it computes a sequence of values based on the product of the integers and the operations specified by the string, and prints the results.

