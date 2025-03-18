#State of the program right berfore the function call: The function should be called within a loop that processes t test cases, where t is a non-negative integer such that 1 <= t <= 100. For each test case, x and y are non-negative integers such that 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop will execute t times, processing each test case. For each iteration, the values of x and y will be updated based on the input provided. The loop will print the larger value followed by the smaller value for each test case. After all iterations, the values of x and y will be the last input values provided for the final test case. The value of t remains unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each with two non-negative integer inputs `x` and `y` where 0 <= x, y <= 9. For each test case, it prints the larger value followed by the smaller value. The function does not return any value. After the function concludes, the values of `x` and `y` will be the last input values provided for the final test case, and the value of `t` (the number of test cases) remains unchanged.

