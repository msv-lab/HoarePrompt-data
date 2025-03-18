#State of the program right berfore the function call: t is an integer such that 1 \le t \le 10^4, representing the number of test cases. For each test case, n and m are integers such that 1 \le n \le 2\cdot10^5 and 1 \le m \le 10^4, representing the initial length of the array a and the value to take the remainder by, respectively. a is a list of n integers such that 1 \le a_i \le 10^4, representing the elements of the array a. s is a string of length n consisting only of the characters 'L' and 'R', representing the commands to be executed. The sum of the values of n for all test cases does not exceed 2\cdot10^5.
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
        
    #State: For each test case, the variable `res` is a list of length `n` where `res[i]` (0 ≤ i < n) is the result of the product of the elements in `arr` from index `l` to `r` (inclusive) after `i` iterations of the loop, taken modulo `m` and then modulo `MOD`. The values of `l` and `r` are such that `l` starts at 0 and `r` starts at `n-1`, and they are updated in each iteration based on the command in `s`. The variable `c` is equal to `n`, and `ans` is the product of the remaining elements in `arr` after the final iteration, modulo `m` and then modulo `MOD`.
#Overall this is what the function does:The function processes multiple test cases, each with an array `a` and a command string `s`. For each test case, it computes a list `res` of length `n` where each element `res[i]` (0 ≤ i < n) represents the product of the elements in `a` from the current left index `l` to the current right index `r` (inclusive), taken modulo `m` and then modulo `10^9 + 6`, after `i` iterations of the command string `s`. The commands in `s` dictate whether to update the product by removing the element at the left or right end of the array. The function prints the list `res` for each test case.

