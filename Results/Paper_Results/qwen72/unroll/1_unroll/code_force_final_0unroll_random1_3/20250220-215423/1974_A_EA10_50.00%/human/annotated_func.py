#State of the program right berfore the function call: The function should accept two parameters, x and y, where x and y are integers such that 0 <= x, y <= 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: The values of `x` and `y` are updated based on user input for each iteration of the loop, and `z` is calculated and printed for each iteration. The value of `a` remains unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `a` from user input, and for each of the `a` iterations, it reads two integers `x` and `y` from user input. For each iteration, it calculates a value `z` based on `x` and `y`, and prints `z`. The values of `x` and `y` are updated with each iteration, and the value of `a` remains unchanged throughout the function execution.

