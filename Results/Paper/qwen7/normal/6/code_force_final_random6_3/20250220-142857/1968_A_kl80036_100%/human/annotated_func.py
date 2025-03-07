#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: Output State: The loop will execute `i` up to the value of `t` minus 1. After all iterations, `i` will be equal to `t - 1`, `t` must still be within the range 1 to 1000, `x` will be the last input integer provided, and `y` will be `x - 1`.
    #
    #In more detail, after the loop has executed all its iterations:
    #- `i` will be set to `t - 1`.
    #- `t` remains within the range 1 to 1000.
    #- `x` will be the last integer input during the loop's execution.
    #- `y` will be `x - 1`.
#Overall this is what the function does:The function reads an integer `t` and then reads `t` integers `x`. For each `x`, it calculates `x - 1` and prints the result. After processing all inputs, the function does not return any value.

