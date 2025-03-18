#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10^5, s and f are strings of length n consisting of '0' and '1' characters, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: `t` is 0, `n` is an input integer greater than 0, `s1` and `s2` are input strings, `a1` is the number of '1' characters in `s1`, `a2` is the number of '1' characters in `s2`, `i` is `n - 1`, `hd` is the greater of 0 or `a1 - a2 - n`, and `res` is the absolute value of `a1 - a2` plus the number of positions where `s1` has '1' and `s2` has '0' in the range from 0 to `n-1`.
#Overall this is what the function does:The function reads multiple test cases from standard input. For each test case, it reads two integers `t` and `n`, and two strings `s1` and `s2` of length `n` consisting of '0' and '1' characters. It calculates the absolute difference between the number of '1' characters in `s1` and `s2`, and then adjusts this difference based on the positions where `s1` has '1' and `s2` has '0'. The function prints the adjusted difference for each test case. After processing all test cases, the function terminates.

