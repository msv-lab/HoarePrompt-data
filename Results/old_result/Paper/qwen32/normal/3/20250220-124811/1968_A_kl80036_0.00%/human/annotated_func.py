#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: `t` is an integer such that 1 <= t <= 1000, `i` is equal to `t`, and for each of the `t` test cases, `x` is the integer input by the user such that 2 <= x <= 1000, and `y` is the integer value of `x // 2` such that 1 <= y <= 500.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each test case, it reads an integer `x` and prints the integer division result of `x` by 2.

