#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x and y are integers such that 0 <= x, y <= 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: For each test case, the loop prints the value of `z` after processing the input values `x` and `y`. The values of `t` and `a` remain unchanged. The values of `x` and `y` are updated with each iteration based on the input, and `z` and `m` are recalculated for each test case.
#Overall this is what the function does:The function `func` processes `a` test cases, where `a` is an integer input by the user. For each test case, it reads two integers `x` and `y` from the user input, performs calculations to determine a value `z`, and prints `z`. The function does not return any value. After the function concludes, the values of `x` and `y` are not retained, and the value of `a` remains unchanged. The function's primary purpose is to compute and print a specific value `z` for each test case based on the provided inputs `x` and `y`.

