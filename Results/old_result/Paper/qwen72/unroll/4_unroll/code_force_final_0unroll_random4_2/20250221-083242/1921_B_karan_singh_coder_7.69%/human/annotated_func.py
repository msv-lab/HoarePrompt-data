#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10^5 for each test case, s and f are strings of length n consisting of '0' and '1' characters, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The values of `t`, `n`, `s`, and `f` remain unchanged. The loop iterates `t` times, and for each iteration, it processes the input strings `s` and `t` of length `n`, calculates the number of '1's in each string, counts the number of differing positions between `s` and `t`, and prints the result based on the conditions specified in the loop. After all iterations, the values of `t`, `n`, `s`, and `f` are the same as they were before the loop started.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and two strings `s` and `t` of length `n` consisting of '0' and '1' characters. For each test case, it calculates the number of '1's in `s` and `t`, counts the number of differing positions between `s` and `t`, and prints a result based on the following conditions: if the number of '1's in `s` and `t` are equal, it prints the number of '1's if there are any differing positions, otherwise it prints 0. If the number of '1's in `s` and `t` are not equal, it calculates the absolute difference `d` between the counts of '1's, and prints the result of `(cnt - d) // 2 + d`, where `cnt` is the number of differing positions. The function does not return any value; it only prints the results for each test case. The values of `t`, `n`, `s`, and `f` are not modified by the function.

