#State of the program right berfore the function call: The function should be called within a loop that processes t test cases, where t is a non-negative integer such that 1 <= t <= 100. For each test case, x and y are integers such that 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop will execute `x` times, where `x` is the input integer for each test case. During each iteration, the values of `x` and `y` will be updated based on user input. If `x` is greater than `y`, the loop will print `x` followed by `y`. Otherwise, it will print `y` followed by `x`. After all iterations, the values of `x` and `y` will be the last values input by the user, and the loop will have printed the results for each iteration. The variable `i` will be equal to `x - 1` at the end of the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. It first reads an integer `x` from the user, which determines the number of test cases to process. For each test case, it reads two integers `x` and `y` from the user, ensuring that both are between 0 and 9. It then prints the two integers in ascending order. After processing all test cases, the function does not return any value, but the last values of `x` and `y` input by the user are retained.

