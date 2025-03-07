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
        
    #State: For each iteration of the loop, the variable `res` is calculated and printed. After all iterations, the values of `t`, `n`, `s1`, `s2`, `a1`, `a2`, and `hd` are not retained as they are re-initialized in each iteration. The only persistent state is the sequence of printed values of `res` for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. For each test case, it reads two integers `t` and `n`, and two strings `s1` and `s2` of length `n` consisting of '0' and '1' characters. It calculates the absolute difference between the number of '1' characters in `s1` and `s2`, and then adjusts this difference based on the positions of '1' in `s1` and '0' in `s2`. The function prints the adjusted difference for each test case. The function does not return any value, and the only persistent state after the function concludes is the sequence of printed values for each test case.

