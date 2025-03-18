#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4. The array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n. The string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `MOD` is 1000000006, `res` is a list of integers obtained after processing each test case, where each element is calculated based on the given operations within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes in the number of elements `n`, the modulus value `m`, an array `a` of `n` integers, and a string `s` of length `n` containing 'L' and 'R'. It calculates a result array `res` where each element is derived from the product of elements in `a` based on the direction specified in `s`. Specifically, if `s[i]` is 'L', it divides the current product by the leftmost element in `a` and updates the result; if 'R', it divides by the rightmost element and updates the result. After processing all elements, it prints the result array `res` for each test case.

