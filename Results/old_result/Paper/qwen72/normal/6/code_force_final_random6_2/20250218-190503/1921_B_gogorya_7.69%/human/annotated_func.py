#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10^5, s and f are strings of length n consisting of characters '0' and '1', and the sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        a1 = s1.count('1')
        
        a2 = s2.count('1')
        
        hd = a1 - a2
        
        res = abs(a1 - a2)
        
        for i in range(n):
            if hd > 0:
                hd -= 1
                continue
            if s1[i] == '1' and s2[i] == '0':
                res += 1
        
        print(res)
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `_` is incremented by `t`, `n` is the final input integer, `s1` is the final input string, `s2` is the final input string, `a1` is the number of '1' characters in the final `s1`, `a2` is the number of '1' characters in the final `s2`, `i` is `n-1`, `hd` is the final value of `a1 - a2` after all iterations, and `res` is the absolute value of `a1 - a2` plus the number of positions where `s1[i]` is '1' and `s2[i]` is '0' for all `i` from 0 to `n-1` where `hd` was not greater than 0.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads two integers `t` and `n`, and two strings `s1` and `s2` of length `n` consisting of characters '0' and '1'. It calculates the Hamming distance (number of differing positions) between `s1` and `s2` with a specific adjustment: if the number of '1's in `s1` is greater than in `s2`, it reduces the Hamming distance by the difference in the number of '1's. Otherwise, it increments the Hamming distance for each position where `s1` has '1' and `s2` has '0'. The function prints the adjusted Hamming distance for each test case. After processing all test cases, the function concludes without returning any value.

