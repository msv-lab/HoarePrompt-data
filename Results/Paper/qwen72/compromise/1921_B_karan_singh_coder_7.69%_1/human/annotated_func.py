#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n is an integer where 1 <= n <= 10^5, s and f are strings of length n consisting of '0' and '1' characters, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: t is an integer where 1 <= t <= 10^4, n is an integer where 1 <= n <= 10^5, s and f are strings of length n consisting of '0' and '1' characters, and the sum of n over all test cases does not exceed 10^5. The loop has completed its iterations, and the final values of `s1`, `t1`, and `cnt` are calculated based on the input strings `s` and `t` for each test case. The output for each test case is printed based on the conditions specified in the loop.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads two integers `n` and `t`, and two strings `s` and `t` of length `n` consisting of '0' and '1' characters. It then calculates the number of differing positions between the strings `s` and `t` and the counts of '1' characters in each string. Based on these calculations, it prints a result for each test case. The result is the number of '1' characters in `s` if the counts of '1' characters in `s` and `t` are equal and there are differing positions; otherwise, it prints a calculated value based on the difference in counts and the number of differing positions. The function does not return any value.

