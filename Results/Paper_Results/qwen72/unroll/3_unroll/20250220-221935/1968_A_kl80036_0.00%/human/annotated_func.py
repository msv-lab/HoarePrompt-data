#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: For each test case, the value of `y` is printed, where `y` is the integer division of `x` by 2. The value of `x` is read from input for each iteration, and `i` iterates from 0 to `t-1`. The value of `t` remains unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` from input, which represents the number of test cases, where `1 ≤ t ≤ 1000`. For each test case, it reads an integer `x` from input, where `2 ≤ x ≤ 1000`, and prints the result of the integer division of `x` by 2. The function does not return any value. After the function concludes, the value of `t` remains unchanged, and the values of `x` and `y` are not retained.

