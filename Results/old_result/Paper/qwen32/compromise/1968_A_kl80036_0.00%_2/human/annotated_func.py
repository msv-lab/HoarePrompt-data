#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, y is an integer which is the result of integer division of the corresponding x by 2, where x is an integer such that 2 <= x <= 1000.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case consists of an integer `x` such that 2 <= x <= 1000. For each test case, it calculates the integer division of `x` by 2 and prints the result.

