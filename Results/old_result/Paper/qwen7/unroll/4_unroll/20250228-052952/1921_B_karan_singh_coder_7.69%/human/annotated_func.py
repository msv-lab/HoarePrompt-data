#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and both s and f are strings of length n consisting of '0' and '1'. Additionally, the sum of n over all test cases does not exceed 10^5.
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
        
    #State: Output State: The output state consists of the result printed for each test case after executing the given loop. For each test case, if the number of '1's in strings `s` and `t` are equal (`s1 == t1`), the output is `s1` if the number of differing positions (`cnt`) is zero, otherwise it is `0`. If the number of '1's in `s` and `t` are different (`s1 != t1`), the output is `(cnt - d) // 2 + d`, where `d` is the absolute difference between `s1` and `t1`.
    #
    #In simpler terms, the output state is a series of integers representing the results of the described logic for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two binary strings `s` and `t` of length `n`, counts the number of '1's in each string, and calculates the number of differing positions between the two strings. Based on whether the counts of '1's are equal or not, it prints either the count of '1's or a calculated value involving the count of differing positions and the absolute difference in '1's. The function does not return any value but prints the results for each test case.

