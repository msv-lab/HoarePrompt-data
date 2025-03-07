#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case contains an integer n such that 1 ≤ n ≤ 10^5, and two strings s and f of length n where each character is either '0' or '1'. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        s1 = s.count('1')
        
        t1 = t.count('1')
        
        cnt = 0
        
        for i in range(n):
            cnt += s[i] != t[i]
        
        if s1 == t1:
            print(s1 if cnt else 0)
        else:
            d = abs(s1 - t1)
            print((cnt - d) // 2 + d)
        
    #State: After all iterations of the loop, `t` is decremented by the number of iterations that have been completed, `n` is an integer such that 1 ≤ n ≤ 10^5, `s` and `t` are strings of length `n` where each character is either '0' or '1', `f` remains unchanged, `s1` is the number of '1' characters in `s`, `t1` is the number of '1' characters in `t`, `cnt` is the number of positions where the characters in `s` and `t` differ, and `i` is `n-1`. For each test case, if `s1` is equal to `t1`, the number of '1' characters in `s` is printed if `cnt` is non-zero, otherwise 0 is printed. If `s1` is not equal to `t1`, `d` is the absolute difference between `s1` and `t1`, and the value `(cnt - d) // 2 + d` is printed.
#Overall this is what the function does:The function processes `t` test cases, each containing an integer `n` and two strings `s` and `t` of length `n` (where each character is either '0' or '1'). For each test case, it calculates the number of positions where the characters in `s` and `t` differ (`cnt`). If the number of '1' characters in `s` (`s1`) is equal to the number of '1' characters in `t` (`t1`), it prints `s1` if `cnt` is non-zero, otherwise it prints 0. If `s1` is not equal to `t1`, it calculates the absolute difference `d` between `s1` and `t1`, and prints the value `(cnt - d) // 2 + d`. The function does not return any value, but it prints the result for each test case.

