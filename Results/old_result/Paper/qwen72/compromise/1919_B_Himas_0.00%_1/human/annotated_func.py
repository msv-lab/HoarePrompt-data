#State of the program right berfore the function call: s is a string of length n where 1 ≤ n ≤ 5000, consisting only of the characters '+' and '-'. t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases.
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
        
    #State: The loop has finished executing all iterations. The variable `s` remains unchanged as a string of length n where 1 ≤ n ≤ 5000, consisting only of the characters '+' and '-'. The variable `t` is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. The loop has printed the result of `P - M` for each test case, where `P` is the count of '+' characters and `M` is the count of '-' characters in the string `e` for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `s` (which is not used) and a string `e` consisting of '+' and '-' characters. It then calculates the difference between the number of '+' characters and the number of '-' characters in `e` and prints this difference. The function does not return any value and does not modify any input parameters. After the function concludes, the variable `t` remains unchanged, and the input string `e` for each test case has been processed and the result printed.

