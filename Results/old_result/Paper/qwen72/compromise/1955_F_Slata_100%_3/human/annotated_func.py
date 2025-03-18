#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each of the four integers p_i in the test cases is an integer such that 0 <= p_i <= 200.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The loop iterates t times, and for each iteration, it reads four integers (a, b, c, d) and prints the result of the expression `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3)`. The value of t remains unchanged, and the values of a, b, c, and d are not retained between iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from the user input, where `1 <= t <= 10^4`. It then iterates `t` times, and in each iteration, it reads four integers `a`, `b`, `c`, and `d` (where `0 <= p_i <= 200` for each `p_i` in `a`, `b`, `c`, and `d`). For each set of four integers, it calculates the sum of their integer divisions by 2, plus an additional 1 if exactly three of the first three integers (`a`, `b`, `c`) are odd. The result of this calculation is printed for each iteration. The function does not return any value, and the state of the program remains unchanged except for the printed output.

