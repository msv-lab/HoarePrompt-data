#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: Output State: t test cases are executed, and for each test case, the value of x-1 is printed.
#Overall this is what the function does:The function reads a number of test cases (t) and for each test case, it reads an integer (x) within the range [2, 1000], calculates x-1, and prints the result. After completing all test cases, the function ends without returning any value.

