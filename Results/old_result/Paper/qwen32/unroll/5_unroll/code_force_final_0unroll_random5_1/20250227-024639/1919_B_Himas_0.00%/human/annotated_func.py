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
        
    #State: The output state consists of t lines, where each line is the difference between the number of '+' and '-' characters in the corresponding input string e.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting only of the characters '+' and '-'. It then outputs the difference between the number of '+' and '-' characters in the string `s` for each test case.

