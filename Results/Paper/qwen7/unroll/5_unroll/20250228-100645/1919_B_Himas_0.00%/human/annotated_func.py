#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-', where '+' represents 1 and '-' represents -1 in an array a of length n.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is an integer, e is a string of length n consisting of characters '+' and '-', where '+' represents 1 and '-' represents -1 in an array a of length n. After all iterations of the loop, for each test case, P and M are integers representing the count of '+' and '-' characters in the string e respectively, and the output is the value of P - M printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `s`, a string `e` consisting of '+' and '-' characters, and calculates the difference between the count of '+' characters (each counted as 1) and '-' characters (each counted as -1). It then prints this difference for each test case. The function does not return any value but prints the result for each test case.

