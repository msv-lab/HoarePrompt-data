#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array a is a list of n integers such that 1 ≤ a_i ≤ 10^4; the string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `m` are integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array `a` is a list of n integers such that 1 ≤ a_i ≤ 10^4; the string `s` is a string of length n consisting only of the characters 'L' and 'R'; `MOD` is 10; the array `res` is a list of n integers calculated based on the operations inside the loop; `ans` is an integer initialized to 1 and updated during the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes an integer `n`, an integer `m`, an array `a` of `n` integers, and a string `s` of length `n` consisting of 'L' and 'R'. It calculates a result array `res` of length `n` based on the values in `a` and the direction indicated by `s`. Specifically, it computes the product of elements in `a` up to a certain point, updates this product as it traverses the string `s` (multiplying or dividing by elements in `a` based on 'L' or 'R'), and stores these intermediate results in `res`. Finally, it prints the array `res` for each test case.

