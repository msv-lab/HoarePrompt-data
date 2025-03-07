#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^5. s and f are strings of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: the output of the last test case processed by the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings `s` and `t` of the same length `n`. For each test case, it calculates and prints a value based on the number of differing positions between the two strings and the count of '1's in each string. Specifically, if the number of '1's in both strings is the same, it prints the number of differing positions if there are any, or 0 if the strings are identical. If the number of '1's differs, it calculates and prints a value that accounts for the necessary changes to make the strings identical in terms of both differing positions and '1' counts.

