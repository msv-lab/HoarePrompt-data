#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, the output consists of t lines where each line contains an integer y such that 1 ≤ y ≤ 999. Each y is calculated as x - 1 for the corresponding input x within the range 2 ≤ x ≤ 1000.
#Overall this is what the function does:The function reads a number of test cases (t) and for each test case, it reads an integer (x) and prints the value of x - 1. After processing all test cases, it outputs t lines where each line contains an integer y such that 1 ≤ y ≤ 999.

