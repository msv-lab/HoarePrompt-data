#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-', where the i-th character represents a_i = 1 if s_i = '+' and a_i = -1 if s_i = '-'.
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
        
    #State: Output State: After the loop executes all the iterations, `P` will be equal to the total number of '+' characters in the string `e`, and `M` will be equal to the total number of '-' characters in `e`. The variable `i` will be equal to the length of `e` plus one (since `i` starts at 1 and increments by 1 with each iteration, it will be one more than the length of `e`). The variable `q` will be the last character of `e`. The variable `s` will be the input integer received before the loop started.
    #
    #In simpler terms, after the loop finishes running, `P` contains the count of '+' characters, `M` contains the count of '-' characters, `i` is the length of the string `e` plus one, `q` is the last character of `e`, and `s` is the integer input received at the start of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `t`, another integer `n`, and a string `s` of length `n` containing characters '+' and '-'. For each test case, it counts the number of '+' characters and the number of '-' characters in the string `s`. It then prints the difference between these two counts. The function does not return any value but prints the result for each test case.

