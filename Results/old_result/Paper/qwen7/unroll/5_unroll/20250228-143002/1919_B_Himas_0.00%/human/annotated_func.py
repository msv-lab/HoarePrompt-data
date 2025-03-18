#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-'.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+', '-', where for each test case, the output is the difference between the number of '+' and '-' characters in the string s.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads an integer `n` and a string `s` of length `n` consisting of '+' and '-' characters. It then calculates and prints the difference between the number of '+' and '-' characters in the string `s`. The function implicitly accepts inputs through variables `t`, `n`, and `s`, and does not return any value explicitly.

