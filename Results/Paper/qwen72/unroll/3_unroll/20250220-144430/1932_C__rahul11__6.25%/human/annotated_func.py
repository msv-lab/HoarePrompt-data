#State of the program right berfore the function call: The function processes multiple test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, m is a positive integer such that 1 ≤ m ≤ 10^4, a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^4, and s is a string of length n consisting only of the characters 'L' and 'R'. The total sum of n across all test cases does not exceed 2·10^5.
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
        
    #State: After the loop executes all the iterations, the `res` list contains the results of the computations for each test case, and the variables `ans`, `c`, `l`, and `r` are in their final states for the last test case processed. Specifically, `ans` will be 1 (or 0 if any division by zero occurred), `c` will be equal to `n`, `l` will be equal to `n` if all characters in `s` were 'R', or some value between 0 and `n-1` otherwise, and `r` will be -1 if all characters in `s` were 'L', or some value between 0 and `n-1` otherwise. The `res` list will have been printed for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` (1 ≤ n ≤ 2·10^5), a positive integer `m` (1 ≤ m ≤ 10^4), a list `a` of `n` integers where each integer `a_i` satisfies 1 ≤ a_i ≤ 10^4, and a string `s` of length `n` consisting only of the characters 'L' and 'R'. For each test case, it computes a list `res` of length `n` where the first element is the product of all integers in `a` modulo `m` and then further modulo `10^9 + 6`. Subsequent elements in `res` are computed by iteratively dividing the current product by elements in `a` based on the direction specified by the characters in `s` ('L' for left, 'R' for right), and then applying the same modulo operations. The function prints the `res` list for each test case. After processing all test cases, the `res` list for the last test case is printed, and the variables `ans`, `c`, `l`, and `r` are in their final states, with `ans` being 1 (or 0 if any division by zero occurred), `c` equal to `n`, `l` equal to `n` if all characters in `s` were 'R' or some value between 0 and `n-1` otherwise, and `r` equal to -1 if all characters in `s` were 'L' or some value between 0 and `n-1` otherwise.

