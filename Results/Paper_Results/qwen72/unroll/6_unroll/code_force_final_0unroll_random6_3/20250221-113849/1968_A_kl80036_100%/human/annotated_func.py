#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 1000, and x is an integer such that 2 <= x <= 1000 for each test case.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: t is a non-negative integer such that 1 <= t <= 1000, and x is an integer such that 2 <= x <= 1000 for each test case. The loop prints the value of x - 1 for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads another integer `x` from the input, where `2 <= x <= 1000`. It then calculates `x - 1` and prints this value. The function does not return any value. After the function concludes, the input values `t` and `x` are no longer relevant, and the program has printed `t` lines, each containing the value of `x - 1` for the corresponding test case.

