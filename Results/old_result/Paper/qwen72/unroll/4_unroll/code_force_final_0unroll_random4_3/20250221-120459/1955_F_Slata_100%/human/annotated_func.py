#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each p_i is an integer such that 0 <= p_i <= 200.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The loop will execute t times, and for each iteration, it will read four integers (a, b, c, d) and print the sum of their integer divisions by 2, plus 1 if exactly three of them are odd. The values of t and each p_i remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 10^4`. For each of the `t` iterations, it reads four integers `a`, `b`, `c`, and `d` from the input, where `0 <= a, b, c, d <= 200`. It then calculates and prints the sum of the integer divisions of `a`, `b`, `c`, and `d` by 2, plus 1 if exactly three of these integers are odd. The function does not return any value, and the values of `t` and the input integers remain unchanged after the function execution.

