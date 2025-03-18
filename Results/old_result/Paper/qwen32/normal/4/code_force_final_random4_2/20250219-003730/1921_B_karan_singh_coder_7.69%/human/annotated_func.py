#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5. s and f are strings of length n, where each character is either '0' or '1'. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The output state is a sequence of integers, each corresponding to the result of a test case, printed one per line.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two binary strings `s` and `t` of the same length `n`. For each test case, it calculates and prints an integer based on the number of differing positions between the two strings and the balance of '1's in each string.

