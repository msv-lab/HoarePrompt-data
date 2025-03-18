#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is an integer such that 1 <= t <= 100. For each iteration, x and y are integers provided as input, and they satisfy 0 <= x, y <= 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop will execute t times, and for each iteration, it will read a new pair of integers (x, y) from the input. If x is greater than y, it will print x followed by y. Otherwise, it will print y followed by x. After all iterations, the values of x and y will be the last pair of integers read from the input, and the loop variable i will be equal to x-1.
#Overall this is what the function does:The function `func` is designed to be called within a loop that iterates `t` times, where `t` is an integer such that 1 <= t <= 100. For each iteration, it reads an integer `x` from the input, and then for each integer from 0 to `x-1`, it reads a pair of integers `x` and `y` (0 <= x, y <= 9) from the input. It then prints the pair in ascending order. After all iterations, the last values of `x` and `y` read from the input will be retained, and the loop variable `i` will be equal to `x-1`. The function does not return any value.

