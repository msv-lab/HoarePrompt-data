#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, x is an integer such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: `i` is `t - 1`, `x` is an input integer such that 2 <= x <= 1000, `y` is `x - 1`.
#Overall this is what the function does:The function `func` processes an implicit input `t` (1 <= t <= 1000) representing the number of test cases. For each test case, it reads an integer `x` (2 <= x <= 1000) and prints the value `x - 1`. The function does not return any value. After the function concludes, the program state includes the number of test cases processed (`t`), and for each test case, the input integer `x` and the printed value `x - 1`.

