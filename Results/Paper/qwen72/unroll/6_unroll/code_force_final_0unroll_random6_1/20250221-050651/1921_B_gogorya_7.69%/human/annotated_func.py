#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10^5 for each test case, s and f are strings of length n consisting of '0' and '1' characters, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop has finished executing for all test cases. For each test case, the variable `res` is printed, which represents the adjusted Hamming distance between the strings `s1` and `s2`. The values of `t`, `n`, `s1`, and `s2` for each test case are unchanged, but the final value of `res` for each test case is determined and printed.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads two integers `t` and `n`, and two strings `s1` and `s2` of length `n` consisting of '0' and '1' characters. It calculates the adjusted Hamming distance between `s1` and `s2` by first computing the difference in the number of '1' characters between the two strings. Then, it iterates through the strings, adjusting the distance based on specific conditions. Finally, it prints the adjusted Hamming distance for each test case. The function does not return any value; it only prints the results. The values of `t`, `n`, `s1`, and `s2` for each test case are unchanged after the function completes.

