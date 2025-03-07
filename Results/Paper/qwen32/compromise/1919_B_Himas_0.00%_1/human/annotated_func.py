#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 5000, and s is a string of length n consisting only of the characters '+' and '-'.
def func():
    for i in range(int(input())):
        s = int(input())
        
        e = input()
        
        P = 0
        
        M = 0
        
        for q in e:
            if q == '+':
                P += 1
            else:
                M += 1
        
        print(P - M)
        
    #State: t is an integer such that 1 <= t <= 1000, s is the integer from the last test case, e is the string from the last test case, P is the count of '+' characters in the last test case's string, M is the count of '-' characters in the last test case's string.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting only of '+' and '-' characters. It then calculates and prints the difference between the number of '+' and '-' characters in the string `s`.

