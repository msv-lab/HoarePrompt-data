#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 1000, and for each test case, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: t is a non-negative integer such that 1 <= t <= 1000, and for each test case, x is an integer such that 2 <= x <= 1000. The loop prints the value of x - 1 for each test case.
#Overall this is what the function does:The function `func` accepts no parameters and reads input from the user. It expects the first input to be a non-negative integer `t` such that 1 <= t <= 1000, representing the number of test cases. For each test case, it reads another integer `x` such that 2 <= x <= 1000. The function then calculates `x - 1` and prints the result for each test case. After the function concludes, `t` test cases have been processed, and the value of `x - 1` has been printed for each of these test cases. The function does not return any value.

