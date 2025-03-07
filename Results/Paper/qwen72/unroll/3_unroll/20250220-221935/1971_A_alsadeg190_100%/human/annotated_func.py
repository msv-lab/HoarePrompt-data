#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is a non-negative integer such that 1 <= t <= 100. For each iteration, x and y are integers provided as input, and they satisfy 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop will execute `x` times, and for each iteration, it will read two integers `x` and `y` from the input. If `x` is less than `y`, it will print `x` and `y` in that order. Otherwise, it will print `y` and `x` in that order. After the loop finishes, the value of `x` will be the last value of `x` read from the input, and the value of `y` will be the last value of `y` read from the input. The value of `i` will be `x - 1`.
#Overall this is what the function does:The function `func` reads an integer `x` from the input, then iterates `x` times. In each iteration, it reads two integers `x` and `y` from the input. It prints the smaller of the two integers first, followed by the larger one. After the function completes, the value of `x` will be the last value of `x` read from the input, and the value of `y` will be the last value of `y` read from the input. The function does not return any value.

