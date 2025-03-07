#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all i; the string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: Output State: After the loop executes all iterations, `c` will be equal to `n`, indicating that the loop has executed `n-1` times. The list `res` will contain `n` elements, where each element represents the value of `ans` after performing the division operations specified by the string `s` up to that point, modulo `MOD`. Specifically, `res[n-1]` will hold the final value of `ans % m % MOD`, which is the result of dividing the initial product of all elements in `arr` by the elements in `arr` as directed by `s`, modulo `MOD`. The variable `ans` will no longer be used after the loop, and the pointers `l` and `r` will have moved such that `l` is `n` and `r` is `-1`, indicating that all elements in `arr` have been processed. The values of `n`, `m`, `arr`, `s`, and `MOD` will remain unchanged from their initial states.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes a list of integers `arr`, an integer `n`, and a string `s` of length `n` consisting of 'L' and 'R'. It calculates the product of all elements in `arr` and then iteratively divides this product by the elements in `arr` based on the direction indicated by `s`. Specifically, if `s[i]` is 'L', it divides the product by the leftmost remaining element in `arr`; if 'R', it divides by the rightmost remaining element. The result of each division is taken modulo `10^9 + 6` and stored in a list `res`. After processing all elements in `arr` according to `s`, the function prints the list `res`, which contains the results of each division operation.

