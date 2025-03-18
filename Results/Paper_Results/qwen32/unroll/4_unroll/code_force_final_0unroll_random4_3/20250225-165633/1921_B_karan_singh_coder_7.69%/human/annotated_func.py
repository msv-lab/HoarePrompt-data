#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, s is a string of length n consisting of '0's and '1's, and f is a string of length n consisting of '0's and '1's. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: the variables `n`, `s`, `t`, `s1`, `t1`, and `cnt` hold the values from the last test case, but they do not affect the overall output as the output is printed immediately after processing each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings `s` and `t` of the same length `n`. For each test case, it calculates and prints a value based on the number of differing positions between the two strings and the count of '1's in each string.

