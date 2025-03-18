#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string consisting of '+' and '-' characters with length n.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string consisting of '+' and '-' characters with length n. After the loop executes all iterations, for each test case, P and M are integers representing the count of '+' and '-' characters in the string s respectively, and the output is the result of P - M printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t`, an integer `n`, and a string `s` consisting of '+' and '-' characters. It then counts the number of '+' and '-' characters in `s`, calculates the difference between these counts, and prints the result for each test case.

