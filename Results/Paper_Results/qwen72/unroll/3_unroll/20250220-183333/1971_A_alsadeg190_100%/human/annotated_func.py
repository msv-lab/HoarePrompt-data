#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is a non-negative integer (1 ≤ t ≤ 100). For each iteration, x and y are integers (0 ≤ x, y ≤ 9) provided as space-separated inputs.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop will execute t times, where for each iteration, the values of x and y will be read from the input. If x is less than y, it will print x followed by y. Otherwise, it will print y followed by x. The values of x and y will be updated with each iteration, but the number of iterations t remains unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `x` from the input, and then for each iteration from 0 to `x-1`, it reads two integers `x` and `y` (both between 0 and 9) from the input. For each pair of integers, it prints the smaller integer followed by the larger integer. The function does not return any value. After the function concludes, the values of `x` and `y` are the last values read from the input, and the program state is unchanged in terms of the number of iterations `t`.

