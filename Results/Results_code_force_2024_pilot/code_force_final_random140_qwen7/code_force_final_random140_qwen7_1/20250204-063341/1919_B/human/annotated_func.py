#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 5000, and s is a string consisting of '+' and '-' characters with length n.
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
        
        print(abs(P - M))
        
    #State: Output State: After the loop executes all the iterations, `M` will be equal to the total number of '-' characters in the string `e`, and `P` will be equal to the total number of '+' characters in the string `e`. The variable `q` will be the last character in the string `e` (if the string is not empty), and `i` will be equal to the total number of iterations minus one, which is `int(input()) - 1`. The variable `s` will retain its initial value since it is not affected by the loop.
    #
    #In simpler terms, after all iterations of the loop, `P` will contain the count of '+' characters, `M` will contain the count of '-' characters, `q` will be the last character of the string `e` (or an empty string if `e` is empty), `i` will be the total number of test cases minus one, and `s` will keep the value it had before the loop started.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `s`, a string `e` consisting of '+' and '-' characters, and calculates the absolute difference between the counts of '+' and '-' characters in `e`. It then prints this difference for each test case. The function does not return any value but prints the result for each test case.

