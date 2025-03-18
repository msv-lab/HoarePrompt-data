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
        
    #State: Output State: After the loop executes all iterations, `P` will be equal to the total number of '+' characters in the string `e`, and `M` will be equal to the total number of '-' or any other character in the string `e`. The variable `i` will be equal to the number of test cases `t`, `s` will remain as the initial integer input, and `e` will be the last string input after all iterations.
    #
    #In simpler terms, `P` will count all the '+' characters, and `M` will count all other characters (including '-') from the last input string `e`. The variable `i` will reflect the total number of test cases, `s` will keep its initial value, and `e` will be the string input corresponding to the last test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `s`, a string `e` consisting of '+' and '-' characters, and calculates the difference between the number of '+' characters and the number of '-' or any other characters in `e`. It prints this difference for each test case. The function implicitly takes the number of test cases `t` as input, along with the values of `s` and `e` for each test case. After processing all test cases, it does not return any value but prints the result for each test case.

