#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and both s and f are strings of length n consisting of '0' and '1'. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: After the loop executes all its iterations, `a` will hold the total count of indices where the character in `s` is greater than the corresponding character in `t`, and `b` will hold the total count of indices where the character in `s` is less than the corresponding character in `t`. The variable `i` will be equal to `n`, and `n` will be the total number of iterations the loop executed, which is the sum of `n` from all test cases. The variable `t` will remain as the string input by the user and will not change.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three inputs: a positive integer \( t \), a positive integer \( n \), and two strings \( s \) and \( f \) of length \( n \) consisting of '0' and '1'. It then compares the characters of \( s \) and \( f \) at each position, counting how many times a character in \( s \) is greater than or less than the corresponding character in \( f \). Finally, it prints the maximum of these two counts.

