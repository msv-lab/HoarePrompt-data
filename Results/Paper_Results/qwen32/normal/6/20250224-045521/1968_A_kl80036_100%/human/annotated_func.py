#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the following t lines, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: The loop has executed `t` times, and for each iteration, an integer `x` was read such that 2 ≤ x ≤ 1000, `y` was calculated as `x - 1`, and `y` was printed. The value of `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `x` and prints `x - 1`.

