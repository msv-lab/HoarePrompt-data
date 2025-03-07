#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is a non-negative integer such that 1 <= t <= 100. For each iteration, the function receives two integers x and y as input, where 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are assigned new integer values from the input, and `i` is `x-1`. For each iteration, if the new `x` > the new `y`, `x` is greater than `y`. Otherwise, `x` is less than or equal to `y`. The loop has executed `x` times, and `x` must be greater than or equal to 1.
#Overall this is what the function does:The function `func` is designed to be called within a loop that iterates `t` times, where `t` is a non-negative integer between 1 and 100. For each call, the function reads an integer `x` from the user, and then for each integer `i` from 0 to `x-1`, it reads two integers `x` and `y` from the user. The function then prints the larger of the two integers followed by the smaller one. After the function concludes, the final state of the program is that `x` and `y` have been reassigned multiple times during the execution, and the loop has executed `x` times for each call to the function. The function does not return any value.

