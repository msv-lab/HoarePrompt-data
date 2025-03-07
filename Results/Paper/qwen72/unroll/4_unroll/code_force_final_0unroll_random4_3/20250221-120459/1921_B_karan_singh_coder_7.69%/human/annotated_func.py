#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10^5, s and f are strings of n characters where each character is either '0' or '1', and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The values of `t` and `n` remain unchanged. The strings `s` and `f` also remain unchanged. The loop iterates `t` times, and for each iteration, it processes the input values `n`, `s`, and `t` to compute and print the result based on the conditions provided in the loop. The variables `s1`, `t1`, and `cnt` are used within the loop to count the number of '1's in `s` and `t`, and to count the number of differing characters between `s` and `t`, respectively. After the loop completes, these variables are no longer in scope and do not affect the final output state.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and two strings `s` and `t` of length `n`, where each character is either '0' or '1'. It then calculates the number of differing characters between `s` and `t` and the number of '1's in each string. If the number of '1's in `s` and `t` is the same, it prints the number of '1's if there are any differing characters; otherwise, it prints 0. If the number of '1's in `s` and `t` is different, it calculates and prints a result based on the difference in the number of '1's and the number of differing characters. The function does not return any value; it only prints the results for each test case. The input variables `t`, `n`, `s`, and `t` (not `f`) are processed within the loop but are not modified or retained after the function completes.

