#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: i is t-1, x is the last input integer, y is the integer division of the last input integer by 2.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `x` and prints the result of integer division of `x` by 2.

